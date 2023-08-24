import json
import urllib.request

def lambda_handler(event, context):
    # read the json file from internet
    # Download the JSON file

    url = "https://carbonvic.s3.amazonaws.com/document.json"
    response = urllib.request.urlopen(url)
    json_data = response.read().decode()
    documents = json.loads(json_data)

    search_obj = event  # Extract search object from event body
    search_keyword = search_obj["searchWord"]
    search_range = search_obj["searchRange"]

    matching_documents = []

    # define weight factor for each search range
    title_weight_factor = 10
    topic_weight_factor = 8
    context_weight_factor = 2
    combine_weight_factor = 10

    for document in documents:
        title = document['title']
        topic = document.get('topic', [])
        context = document.get('context', [])

        separate_matches = 0
        separate_weight_fact = 0

        if search_range == "topic":
            combined_matches = sum(topic.count(search_keyword) for topic in topic)
            combined_weight_fact = combined_matches * topic_weight_factor*combine_weight_factor

            for word in search_keyword.split():
                separate_matches += sum(topic.count(word) for topic in topic)
                separate_weight_fact += separate_matches * topic_weight_factor

        elif search_range == "title":
            combined_matches = title.count(search_keyword)
            combined_weight_fact = combined_matches * combine_weight_factor * title_weight_factor

            for word in search_keyword.split():
                separate_matches += title.count(word)
                separate_weight_fact += separate_matches * title_weight_factor

        else:
            combined_title_matches = title.count(search_keyword)
            combined_topic_matches = sum(topic.count(search_keyword) for topic in topic)
            combined_context_matches = sum(item.count(search_keyword) for item in context)
            combined_matches = combined_title_matches + combined_topic_matches + combined_context_matches
            combined_weight_fact = ((combined_title_matches * title_weight_factor)\
                                   + (combined_topic_matches * topic_weight_factor) + \
                                   (combined_context_matches * context_weight_factor))*combine_weight_factor

            for word in search_keyword.split():
                title_matches = title.count(word)
                topic_matches = sum(topic.count(word) for topic in topic)
                context_matches = sum(item.count(word) for item in context)
                separate_matches += title_matches + topic_matches + context_matches
                separate_weight_fact += (title_matches * title_weight_factor) \
                                        + (topic_matches * topic_weight_factor) \
                                        + (context_matches * context_weight_factor)

        if combined_matches > 0 or separate_matches > 0:
            matching_documents.append({
                "URL": document['URL'],
                "title": document['title'],
                "topic": document['topic'],
                "time": document['time'],
                "combine_matches": combined_matches,
                "combine_weight_fact": combined_weight_fact,
                "separate_matches": separate_matches,
                "separate_weight_fact": separate_weight_fact,
                "total_weight_fact": combined_weight_fact + separate_weight_fact
            })

    matching_documents.sort(key=lambda d: d['total_weight_fact'], reverse=True)

    # Prepare the search results JSON object
    search_results = {
        "search_keyword": search_keyword,
        "search_range": search_range,
        "results": matching_documents
    }

    # json_results = json.dumps(search_results, indent=4)
    # print(json_results)

    # has more than 0 results in matching_documents
    if len(matching_documents) > 0:
        return {
            'statusCode': 200,
            'body': search_results
        }

    # has no results in matching_documents
    else:
        return {
            'statusCode': 404,
            'body': "No results found"
        }
