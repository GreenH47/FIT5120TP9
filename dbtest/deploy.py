import pymysql
import json

root_username = 'greenh47'
root_password = 'RRCgwXAfWw53cej'

# Database credentials
host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
port = 3306
database = 'test'
username = root_username
password = root_password


def lambda_handler(event):
    # JSON object representing the input data
    json_object = event['json_object']
    input_data = json.loads(json_object)

    try:
        # Connect to the database
        connection = pymysql.connect(host=host, port=port, database=database,
                                     user=username, password=password)

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query to fetch data based on Subarea match
        cursor.execute(f"SELECT * FROM bill WHERE subarea = '{input_data['Subarea']}'")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Prepare the output JSON object
        output_json = {
            "user_input": input_data,
            "average": {}
        }

        if rows:
            for row in rows:
                output_json["average"] = {
                    "Subarea": row[1],
                    "Electricity": row[2],
                    "Gas": row[3],
                    "Carbon": row[4]
                }
                return output_json

        # If no rows found, return the output JSON with average as an empty dictionary
        return output_json

    except pymysql.Error as e:
        return {
            "error": str(e)
        }

    finally:
        # Close the connection
        if connection:
            connection.close()


