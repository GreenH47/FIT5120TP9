import json
import boto3


def lambda_handler(event, context):
    # Get the council value from the JSON request
    council = event['council']

    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                              aws_secret_access_key='r7WNIZx59YHHQVlzkxw2zfgdfw83TRlQZK3UPJ8e')
    table = dynamodb.Table('council')  # Replace 'YourTableName' with the actual table name in DynamoDB

    # Search the DynamoDB table for a matching council value
    response = table.scan(FilterExpression='council = :council', ExpressionAttributeValues={':council': council})

    # Extract the matching result(s)
    items = response.get('Items', [])

    # Return the result as a JSON response
    if len(items) > 0:
        return {
            'statusCode': 200,
            'body': items
        }
    else:
        return {
            'statusCode': 404,
            'body': 'Not found'
        }


json_request = { "council": "Monash City Council" }
print(lambda_handler(json_request, None))