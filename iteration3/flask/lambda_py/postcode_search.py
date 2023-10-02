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

    # print(postcode)

    try:
        # Connect to the database
        connection = mysql.connector.connect(host=host, port=port, database=database,
                                             user=username, password=password)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query
        query = """
        select p.council_name,p.postcode,b.landfill_no,b.landfill_yes,b.recycle_no,b.recycle_yes,b.green_no,b.green_yes
        from Bin b, Postcode p
        where b.council_name = p.council_name
        and p.postcode = %s
        group by b.council_name,p.postcode,b.landfill_no,b.landfill_yes,b.recycle_no,b.recycle_yes,b.green_no,b.green_yes
        limit 1
        """

        params = (postcode,)
        cursor.execute(query, params)

        # Fetch all the rows returned by the query as dictionaries
        rows = cursor.fetchall()
        # desc = cursor.description

        # print(rows)

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the query results as a JSON response
        if len(rows) == 0:
            return {
                'statusCode': 404,
                'body': 'Postcode not found!'
            }
        else:
            # Format the results
            results = {
                'council_name': rows[0][0],
                'postcode': rows[0][1],
                'landfill_no': rows[0][2],
                'landfill_yes': rows[0][3],
                'recycle_no': rows[0][4],
                'recycle_yes': rows[0][5],
                'green_no': rows[0][6],
                'green_yes': rows[0][7]
            }

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
