import json
import mysql.connector

def lambda_handler(event, context):
    # Root database credentials
    root_username = 'greenh47'
    root_password = 'RRCgwXAfWw53cej'

    # Database credentials
    host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
    port = 3306
    database = 'council'

    username = root_username
    password = root_password

    # Parse the JSON request
    json_request = json.loads(event)

    # Extract the council name from the request
    council_name = json_request.get('council')

    try:
        # Connect to the database
        connection = mysql.connector.connect(host=host, port=port, database=database,
                                             user=username, password=password)

        # Create a cursor object
        cursor = connection.cursor()

        # Fetch the council_id for the given council_name
        cursor.execute("SELECT council_id FROM Council WHERE council_name = %s", (council_name,))
        council_id = cursor.fetchone()
        if council_id is None:
            return {
                'statusCode': 404,
                'body': json.dumps('Council not found!')
            }

        # Fetch the waste data for the given council_id
        cursor.execute("SELECT year, waste_pp, diversion_rate, collect_type, amount FROM Waste WHERE council_id = %s",
                       (council_id[0],))
        rows = cursor.fetchall()

        # Format the results
        results = {}
        for row in rows:
            waste_pp = row[1]

            if waste_pp not in results:
                # Create an initial result dictionary for the waste_pp
                results[waste_pp] = {
                    'council_name': council_name,
                    'year': row[0],
                    'waste_pp': waste_pp,
                    'diversion_rate': row[2],
                    'details': []
                }

            # Add the collect_type and amount as a detail dictionary
            collect_type = row[3]
            amount = row[4]
            if collect_type and amount:
                detail = {
                    'collect_type': collect_type,
                    'amount': amount
                }
                results[waste_pp]['details'].append(detail)

        # Convert the dictionary of results into a list
        results_list = list(results.values())

        # Return the results
        return {
            'statusCode': 200,
            'body': results_list
        }

    except mysql.connector.Error as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error connecting to MySQL: {e}")
        }

    finally:
        # Close the connection
        if connection:
            connection.close()


request_body = {
    'council': 'Knox City Council'
}
request_json = json.dumps(request_body)
print(lambda_handler(request_json, None))