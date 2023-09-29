import boto3
import json
import redis
import datetime


def store_quiz_data_in_redis():
    # Initialize the DynamoDB client
    # try to connect to dynamodb
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                                  aws_secret_access_key='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')

        table = dynamodb.Table('Quiz')

        # Get the total number of available questions in the Quiz table
        total_questions = table.scan(Select='COUNT')['Count']
    except Exception as e:
        print("Error connecting to DynamoDB")
        print(e)
        return

    print("Dynamodb connected! Total questions available:", total_questions)

    # if not connected to redis then exit
    try:
        redis_client = redis.Redis(host='34.198.149.11', port=6379, password='8479f1eb312d')
        redis_client.ping()
        print("redis Connected")


    except redis.ConnectionError:
        print("redis Not Connected")
        return

    # Scan the DynamoDB table to retrieve all quiz data
    response = table.scan()

    expiration_time = datetime.datetime.now() + datetime.timedelta(hours=10)

    # Iterate through the quiz items and store them in Redis
    for item in response['Items']:
        quiz_id = item['quiz_id']
        topic = item['topic']

        # Prepare the quiz data as a dictionary (excluding quiz_id itself)
        quiz_data = {
            'quiz_id': quiz_id,
            'question': item['question'],
            'topic': topic,
            'choice_type': item['choice_type'],
            'correct_answer': json.dumps(item['correct_answer']),
            'options': json.dumps(item['options'])
        }

        # Set the quiz data using HSET in Redis
        redis_client.hset(f"quiz_id:{quiz_id}", mapping=quiz_data)
        # Add the quiz_id to the Redis Set under the topic key
        redis_client.sadd(f"topic:{topic}", quiz_id)

        # Set the expiration time for the quiz item (10 hours from now)
        # expiration_time = datetime.datetime.now() + datetime.timedelta(hours=10)
        # redis_client.expireat(quiz_id, expiration_time)

    print("Quiz data stored in Redis successfully.")
    print("redis data count: ", redis_client.dbsize())

    # Retrieve quiz data using keys
    print("Data for quiz_id:1:")
    print(redis_client.hgetall('quiz_id:1'))

    print("Data for topic:waste:")
    topic_quiz_ids = redis_client.smembers('topic:Recycled Waste')
    for quiz_id in topic_quiz_ids:
        print(redis_client.hgetall(f"quiz_id:{quiz_id.decode('utf-8')}"))

    # Get the expiration time for the quiz item
    # item_expiration_time = redis_client.ttl('1')
    # print("Expiration time for item 1 (in seconds):", item_expiration_time)

    redis_client.close()


def redis_test():
    redis_client = redis.Redis(host='34.198.149.11', port=6379, password='8479f1eb312d')

    # if not connected to redis then exit
    try:
        redis_client.ping()
        print("redis Connected")
        # return
    except redis.ConnectionError:
        print("redis Not Connected")
        return

    print("Data for quiz_id:1:")
    print(redis_client.hgetall('quiz_id:1'))


    # wildcard patterns for searching.
    # print("Data for topic:waste using key:")
    # keys = redis_client.scan_iter(match='topic:*waste*')
    # # print(key)
    # for key in keys:
    #     # Check if the key represents a set
    #     if redis_client.type(key).decode('utf-8') == 'set':
    #         quiz_ids = redis_client.smembers(key)
    #         for quiz_id in quiz_ids:
    #             quiz_key = f"quiz_id:{quiz_id.decode('utf-8')}"
    #             result = redis_client.hgetall(quiz_key)
    #             print(result)
    #     # Handle hash keys separately if needed
    #     else:
    #         topic_key = redis_client.hgetall(key)
    #         print(topic_key)

    print("Data for topic:waste using quiz id:")
    topic_quiz_ids = redis_client.smembers('topic:Recycled Waste')
    for quiz_id in topic_quiz_ids:
        print(redis_client.hgetall(f"quiz_id:{quiz_id.decode('utf-8')}"))

    # Close the Redis connection
    redis_client.close()

    print("redis closed")


if __name__ == '__main__':
    if input("storage or test? ") == "1":
        store_quiz_data_in_redis()
    else:
        redis_test()
