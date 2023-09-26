import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2', aws_secret_access_key='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')

table = dynamodb.Table('Quiz')

# print how many items are in the table
print("Table item count before import:", len(table.scan())-1)

# Read the quiz data from the JSON file
with open('quiz.json') as file:
    quiz_data = json.load(file)

# Iterate through the quiz items and put them into the DynamoDB table
for item in quiz_data:
    quiz_id = item['quiz_id']
    question = item['question']
    topic = item['topic']
    choice_type = item['choice_type']
    correct_answer = item['correct_answer']
    options = item['options']

    # Prepare the item to be inserted into the table
    quiz_item = {
        'quiz_id': quiz_id,
        'question': question,
        'topic': topic,
        'choice_type': choice_type,
        'correct_answer': correct_answer,
        'options': options
    }

    # Insert the item into the DynamoDB table
    table.put_item(Item=quiz_item)



print("Quiz data imported successfully.")
# how many items imported
print("Imported", len(quiz_data), "items into DynamoDB Table.")
# Print how many items are in the table
print("Table item count after import:", len(table.scan())-1)
