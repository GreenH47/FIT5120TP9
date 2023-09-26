import json
import random
import boto3

def lambda_handler(event, context):
    # try to connect to dynamodb
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                                  aws_secret_access_key='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')

        table = dynamodb.Table('Quiz')

        # Get the total number of available questions in the Quiz table
        total_questions = table.scan(Select='COUNT')['Count']
    except Exception as e:
        return {
            'statusCode': 503,
            'body': 'Could not connect to the database. ' + str(e)
        }

    # Retrieve the value of "get_quiz_num" from the event
    try:
        get_quiz_num = int(event['get_quiz_num'])
    except:
        return {
            'statusCode': 400,
            'body': 'Please provide a value for "get_quiz_num" in the request body.'
        }

    # Check if the value of "get_quiz_num" is valid
    if get_quiz_num > total_questions:
        return {
            'statusCode': 405,
            'body': 'The number of questions requested exceeds the total number of questions available.'
        }

    # Generate a random set of three unique indices
    random_indices = random.sample(range(total_questions), get_quiz_num)

    # Retrieve the questions using the generated random indices
    questions = []
    for index in random_indices:
        response = table.scan(Select='ALL_ATTRIBUTES', FilterExpression='quiz_id = :q_id',
                              ExpressionAttributeValues={':q_id': str(index + 1)})
        question = response['Items'][0]
        questions.append(question)

    # Check if the number of questions retrieved is equal to the number of questions requested
    if len(questions) == 0:
        return {
            'statusCode': 500,
            'body': 'An error occurred while retrieving the questions.'
        }
    else:
        return {
            'statusCode': 200,
            'body': questions
        }



event = {"get_quiz_num": "2"}
print(lambda_handler(event, None))