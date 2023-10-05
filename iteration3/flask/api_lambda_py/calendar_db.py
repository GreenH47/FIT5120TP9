
import pandas as pd
import json
from datetime import date,datetime
import mysql.connector

'''


'''


def check_schedule(json_input):
    try:
        json_input = json.loads(json_input)
    except ValueError:
        return {
            'statusCode': 400,
            'body': 'Invalid request format please use json!'
        }

    required_keys = ['current_date', 'suburb', 'region', 'street']

    if not all(key in json_input for key in required_keys):
        return {
            'statusCode': 400,
            'body': 'Invalid input data please contains current_date suburb region and street keys !'
        }

    if json_input['region'].lower() != 'victoria':
        return {
            'statusCode': 400,
            'body': 'Invalid region only include victoria!'
        }

    # Connect to the database
    try:
        # Root database credentials
        root_username = 'greenh47'
        root_password = 'RRCgwXAfWw53cej'

        # Database credentials
        host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
        port = 3306
        database = 'council'

        username = root_username
        password = root_password
        connection = mysql.connector.connect(host=host, port=port, database=database,
                                             user=username, password=password)

    except mysql.connector.Error as err:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to connect to database!')
        }

    cursor = connection.cursor()
    # print("database connected")

    request_street = json_input['street']
    request_council = json_input['suburb']

    # Construct the SQL query with the parameters
    sql_query = """
    SELECT landfill_frequency, landfill_next, recycle_frequency, recycle_next, green_frequency, green_next
    FROM calendar
    WHERE council_name = %s AND street_name = %s
    LIMIT 1;
    """

    # Execute the query with the provided values
    cursor.execute(sql_query, (request_council, request_street))

    result = cursor.fetchone()

    # Check if the result is None
    if result is None:
        return {
            'statusCode': 404,
            'body': json.dumps('No matching schedule found!')
        }

    # convert the date format
    current_date = datetime.strptime(json_input['current_date'], '%Y-%m-%d').date().strftime('%Y-%m-%d')
    landfill_frequency = result[0]
    landfill_next = datetime.strptime(result[1], "%d/%m/%Y").date().strftime('%Y-%m-%d')
    recycle_frequency = result[2]
    recycle_next = datetime.strptime(result[3], "%d/%m/%Y").date().strftime('%Y-%m-%d')
    green_frequency = result[4]
    green_next = datetime.strptime(result[5], "%d/%m/%Y").date().strftime('%Y-%m-%d')

    #print("database query done")

    if current_date < landfill_next:
        next_landfill_date = landfill_next
    else:
        diff = (date.fromisoformat(current_date) - date.fromisoformat(landfill_next)).days
        weeks = diff // 7
        landfill_frequency_multiplier = 1 if 'weekly' in landfill_frequency else 2
        next_landfill_date = (date.fromisoformat(landfill_next) + pd.DateOffset(
            weeks=int(weeks) + 1) * landfill_frequency_multiplier).strftime('%Y-%m-%d')

    if current_date < recycle_next:
        next_recycle_date = recycle_next
    else:
        diff = (date.fromisoformat(current_date) - date.fromisoformat(recycle_next)).days
        weeks = diff // 7
        recycle_frequency_multiplier = 1 if 'weekly' in recycle_frequency else 2
        next_recycle_date = (
                date.fromisoformat(recycle_next) + pd.DateOffset(
            weeks=int(weeks) + 1) * recycle_frequency_multiplier).strftime('%Y-%m-%d')

    if current_date < green_next:
        next_green_date = green_next
    else:
        diff = (date.fromisoformat(current_date) - date.fromisoformat(green_next)).days
        weeks = diff // 7
        green_frequency_multiplier = 1 if 'weekly' in green_frequency else 2
        next_green_date = (
                date.fromisoformat(green_next) + pd.DateOffset(
            weeks=int(weeks) + 1) * green_frequency_multiplier).strftime('%Y-%m-%d')

    response = {
        'current_date': current_date,
        'landfill_frequency': landfill_frequency,
        'next_landfill_date': next_landfill_date,
        'recycle_frequency': recycle_frequency,
        'next_recycle_date': next_recycle_date,
        'green_frequency': green_frequency,
        'next_green_date': next_green_date
    }

    return {
        'statusCode': 200,
        'body': response
    }


def user_input():
    # Example JSON input for testing
    json_input = {
        "longitude": 144.962974,
        "latitude": -37.810294,
        "current_date": "2023-10-20",
        "suburb": "Burwood",
        "region": "Victoria",
        "street": "Ardenne Close"
    }

    result = check_schedule(json.dumps(json_input))
    if result:
        print(json_input)
        print(result)
    else:
        print("No matching schedule found.")


if __name__ == '__main__':
    user_input()
