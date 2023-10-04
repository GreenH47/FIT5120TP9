import pandas as pd

def find_collection_frequency(json_input):
    # Read the Excel file
    df = pd.read_csv("calendar_test.csv", encoding='utf-8')

    # Filter the data based on the given region
    df_region = df[df['region'] == json_input['region']]

    # Filter the data based on the given suburb and street
    df_suburb = df_region[df_region['suburb'] == json_input['suburb']]
    df_street = df_suburb[df_suburb['street'].str.contains(json_input['street'])]

    if not df_street.empty:
        # Get the current date in yyyy-mm-dd format
        #current_date = pd.to_datetime('today').strftime('%Y-%m-%d')

        # Extract the collection frequencies
        landfill_frequency = df_street['landfill_frequency'].iloc[0]
        recycle_frequency = df_street['recycle_frequency'].iloc[0]
        green_frequency = df_street['green_frequency'].iloc[0]

        # Create the result dictionary
        result = {

            'landfill_frequency': landfill_frequency,
            'recycle_frequency': recycle_frequency,
            'green_frequency': green_frequency
        }

        return result
    else:
        return None

json_input = {
    "longitude": 144.962974,
    "latitude": -37.810294,
    "suburb": "Burwood",
    "region": "Victoria",
    "street": "Ardenne Close"
}

result = find_collection_frequency(json_input)

if result:
    print(result)
else:
    print("No matching data found.")
