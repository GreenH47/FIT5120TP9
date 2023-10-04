import pandas as pd
import json
import os
from datetime import date


def check_schedule(json_input):
    try:
        json_input = json.loads(json_input)
    except ValueError:
        return {
            'statusCode': 400,
            'body': 'Invalid JSON data!'
        }
    required_keys = ['current_date', 'suburb', 'region', 'street']

    if not all(key in json_input for key in required_keys):
        return {
            'statusCode': 400,
            'body': 'Invalid input data!'
        }

    if json_input['region'].lower() != 'victoria':
        return {
            'statusCode': 400,
            'body': 'Invalid region!'
        }

    # data = pd.read_csv('calendar_test.csv')

    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, 'calendar_test.csv')
    data = pd.read_csv(csv_path)


    matching_suburb = data[data['suburb'].str.lower() == json_input['suburb'].lower()]
    if matching_suburb.empty:
        return {
            'statusCode': 404,
            'body': 'Suburb not included!'
        }

    matching_street = matching_suburb[matching_suburb['street'].str.lower() == json_input['street'].lower()]

    if matching_street.empty:
        return {
            'statusCode': 404,
            'body': 'Street not included!'
        }

    current_date = json_input['current_date']

    landfill_frequency = matching_street['landfill_frequency'].values[0]
    landfill_next = str(matching_street['landfill_next'].values[0])

    recycle_frequency = matching_street['recycle_frequency'].values[0]
    recycle_next = str(matching_street['recycle_next'].values[0])

    green_frequency = matching_street['green_frequency'].values[0]
    green_next = str(matching_street['green_next'].values[0])

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

    result = {
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
        'body': result
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

    result = check_schedule(json_input)
    if result:
        print(json_input)
        print(result)
    else:
        print("No matching schedule found.")


if __name__ == '__main__':
    user_input()
