import json
import mysql.connector
import re


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
    json_request = event

    # Extract the postcode value from the request
    postcode = json_request.get('postcode')

    # check if postcode is four digits number
    if not re.match(r"^\d{4}$", postcode):
        return {
            'statusCode': 400,
            'body': 'Invalid postcode!'
        }

    try:
        # Connect to the database
        connection = mysql.connector.connect(host=host, port=port, database=database,
                                             user=username, password=password)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Query 1: Bin details
        bin_query = """
        SELECT p.council_name, p.postcode, b.landfill_no, b.landfill_yes, b.recycle_no, b.recycle_yes, b.green_no, b.green_yes
        FROM Bin b, Postcode p
        WHERE b.council_name = p.council_name
        AND p.postcode = %s
        LIMIT 1
        """

        bin_params = (postcode,)
        cursor.execute(bin_query, bin_params)
        bin_rows = cursor.fetchall()

        if len(bin_rows) != 0:
            # Query 2: Waste policies
            policy_query = """
            SELECT c.postcode, p.council_name, p.waste_type, p.waste_policy
            FROM Policy p, Postcode c
            WHERE p.council_name = c.council_name
            AND c.postcode = %s
            """

            policy_params = (postcode,)
            cursor.execute(policy_query, policy_params)
            policy_rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the query results as a JSON response
        if len(bin_rows) == 0:
            return {
                'statusCode': 404,
                'body': 'Postcode not found!'
            }
        else:
            # Format the results
            bin_results = {
                'council_name': bin_rows[0][0],
                'postcode': bin_rows[0][1],
                'landfill_no': bin_rows[0][2],
                'landfill_yes': bin_rows[0][3],
                'recycle_no': bin_rows[0][4],
                'recycle_yes': bin_rows[0][5],
                'green_no': bin_rows[0][6],
                'green_yes': bin_rows[0][7]
            }

            waste_results = []
            for row in policy_rows:
                waste_results.append({
                    'waste_type': row[2],
                    'waste_policy': row[3]
                })

            results = {
                'council_name': bin_rows[0][0],
                'postcode': bin_rows[0][1],
                'policy': {
                    'landfill_no': bin_rows[0][2],
                    'landfill_yes': bin_rows[0][3],
                    'recycle_no': bin_rows[0][4],
                    'recycle_yes': bin_rows[0][5],
                    'green_no': bin_rows[0][6],
                    'green_yes': bin_rows[0][7]
                },
                'waste': waste_results
            }

            if len(waste_results) == 0:
                return{
                    'statusCode': 404,
                    'body': 'No waste policy found!'
                }
            else:
                return {
                    'statusCode': 200,
                    'body': results
                }

    except Exception as e:
        # Return an error message if an exception occurs
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

# event = {'postcode': '3352'}
# print(lambda_handler(event, None))