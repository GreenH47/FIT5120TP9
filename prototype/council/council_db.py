import json
import boto3


# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                              aws_secret_access_key='r7WNIZx59YHHQVlzkxw2zfgdfw83TRlQZK3UPJ8e')
table = dynamodb.Table('council')  # Replace 'YourTableName' with the actual table name in DynamoDB

# Read the JSON file
with open('knowyouare_json.json', 'r') as file:
    json_data = json.load(file)

# Store each item from the JSON data into DynamoDB
for item in json_data:
    response = table.put_item(Item=item)
    print('Item stored successfully:', response)
