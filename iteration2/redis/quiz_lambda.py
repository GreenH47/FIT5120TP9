import boto3
import random


def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2', aws_secret_access_key='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')


    # Retrieve all items from the DynamoDB table
    response = dynamodb.scan(
        TableName='Quiz'
    )

    # Extract the items from the response
    items = response['Items']

    # Shuffle the items randomly
    random.shuffle(items)

    # Initialize an empty list to store the selected questions
    selected_questions = []

    # Iterate through the shuffled items and select three questions with different topics
    for item in items:
        # Extract the topic and check if it is already present in the selected questions
        topic = item['topic']['S']
        if topic not in [q['topic'] for q in selected_questions]:
            # Add the question to the selected questions list
            selected_questions.append({
                'quiz_id': item['quiz_id']['S'],
                'question': item['question']['S'],
                'option1': item['option1']['S'],
                'option2': item['option2']['S'],
                'answer': item['answer']['S'],
                'topic': topic
            })

            # Break the loop if three questions with different topics are selected
            if len(selected_questions) == 3:
                break

    # Return the selected questions as the response
    return {
        'statusCode': 200,
        'body': selected_questions
    }

    # return error
    return {
        'statusCode': 500,
        'body': 'Error while retrieving questions'
    }


print(lambda_handler(None, None))