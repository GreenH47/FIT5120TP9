import boto3
import json
from decimal import Decimal
# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2', aws_secret_access_key='r7WNIZx59YHHQVlzkxw2zfgdfw83TRlQZK3UPJ8e')

# Get a reference to your DynamoDB table
table = dynamodb.Table('Map')

# Load the JSON file
with open('random_locations1.json') as file:
    data = json.load(file)

# Convert float values to Decimal types
data = json.loads(json.dumps(data), parse_float=Decimal)

# Iterate over the data and put each item into the table
for item in data:
    table.put_item(Item=item)

print("Data imported successfully to DynamoDB.")
