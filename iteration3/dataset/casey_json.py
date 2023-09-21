import csv
import json

csv_file = 'casey.csv'  # Path to the CSV file
json_file = 'casey.json'  # Path to the output JSON file

data = []  # List to store the converted data

# Read the CSV file and convert each row into a dictionary
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Write the converted data to the JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print("Conversion to JSON complete.")
