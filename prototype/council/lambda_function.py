import json
import mysql.connector

def lambda_handler(event, context):
    root_username = 'greenh47'
    root_password = 'RRCgwXAfWw53cej'

    # Database credentials
    host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
    port = 3306
    database = 'test'
    # username = 'yuntao'
    # password = 'MzA4NDA0MDNjNjkxOTVi'
    username = root_username
    password = root_password

    # JSON object representing the input data
    #json_object = '{"Subarea":"Subarea 4","Electricity":2,"Gas":3,"Carbon":5.36}'
    #test_object = event
    #print("event input:",test_object)
    json_object = json.dumps(event)
    print(json_object)
    input_data = json.loads(json_object)

    try:
        # Connect to the database
        connection = mysql.connector.connect(host=host, port=port, database=database,
                                     user=username, password=password)

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query to fetch data based on Subarea match
        # Parameterized queries ensure that the input values are properly 
        # escaped and treated as data, not as part of the SQL syntax.
        cursor.execute("SELECT * FROM bill WHERE subarea = %s", (input_data['Subarea'],))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Prepare the output JSON object
        output_json = {
            "user_input": input_data,
            "average": None
        }

        if rows:
            for row in rows:
                output_json["average"] = {
                    "Subarea": row[1],
                    "Electricity": row[2],
                    "Gas": row[3],
                    "Carbon": row[4]
                }
                print(json.dumps(output_json))  # Print the output JSON
        else:
            if rows:
                for row in rows:
                    output_json["average"] = {
                        "Subarea": row[1],
                        "Electricity": row[2],
                        "Gas": row[3],
                        "Carbon": row[4]
                    }
                    print(json.dumps(output_json))  # Print the output JSON
            else:
                print(json.dumps(output_json))  # Print the output JSON with average as an empty dictionary


    except mysql.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(output_json)
    }
