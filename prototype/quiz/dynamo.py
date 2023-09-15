import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2', aws_secret_access_key='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')

response = dynamodb.query(
    TableName='Quiz',
    KeyConditionExpression='#quiz_id = :id',
    ExpressionAttributeNames={'#quiz_id': 'quiz_id'},
    ExpressionAttributeValues={':id': {'S': '1'}}
)

items = response['Items']

print(items)