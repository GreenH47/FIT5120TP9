import boto3

def search_items_by_suburb(suburb):
    # Initialize the DynamoDB resource
    dynamodb = boto3.client('dynamodb', region_name='us-east-1',
                              aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                              aws_secret_access_key='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')

    # Define the search parameters
    params = {
        'TableName': 'Map',
        'FilterExpression': 'suburb = :suburb',
        'ExpressionAttributeValues': {
            ':suburb': {'S': suburb}
        }
    }

    # Perform the DynamoDB query
    response = dynamodb.scan(**params)

    # Retrieve the matching items
    items = response['Items']

    # Process the items into the desired format
    processed_items = []
    for item in items:
        processed_item = {
            'id': int(item['id']['N']),
            'latitude': float(item['latitude']['N']),
            'longitude': float(item['longitude']['N']),
            'suburb': item['suburb']['S'],
            'type': item['type']['S'],
            'description': item['description']['S'],
            'collected_date': item['collected_date']['S']
        }
        processed_items.append(processed_item)

    return processed_items

# Usage example
suburb = 'Hawthorn'
results = search_items_by_suburb(suburb)
print(results)
