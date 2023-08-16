import boto3
import json

def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2', aws_secret_access_key='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')

    # Retrieve all items from the DynamoDB table
    response = dynamodb.scan(
        TableName='Quiz'
    )

    # Extract the items from the response
    items = response['Items']

    # Retrieve user answers from the JSON request
    answers = event['answers']

    # Initialize score and list for wrongly answered questions
    score = 0
    wrong_answers = []

    # Compare user answers with database questions
    for answer in answers:
        # Get the quiz ID and selected option from the user answer
        quiz_id = answer['quiz_id']
        selected_option = answer['option']

        # Find the corresponding question in the database
        for item in items:
            if item['quiz_id']['S'] == quiz_id:
                # Get the correct option and check if the selected option is correct
                correct_option = item['answer']['S']
                if selected_option == correct_option:
                    # Increment score for a correct answer
                    score += 10

                else:
                    # Find the label of the correct option
                    correct_option_label = ""
                    if correct_option == 'option1':
                        correct_option_label = item['option1']['S']
                    elif correct_option == 'option2':
                        correct_option_label = item['option2']['S']

                    # Append the details of wrongly answered question with correct answer label
                    wrong_answers.append({
                        'quiz_id': quiz_id,
                        'question': item['question']['S'],
                        'correct_option': correct_option_label,
                        'topic': item['topic']['S']
                    })

    # Prepare the JSON response
    response = {
        'score': score,
        'wrong_answers': wrong_answers
    }

    # Return the response
    return {
        'statusCode': 200,
        'body': response
    }

# read answer.json file as event

with open('answer.json') as json_file:
    event = json.load(json_file)

print(lambda_handler(event,2))