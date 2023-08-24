import json
import urllib.request

def search(search_obj):
    with open('document.json', 'r') as file:
        documents = json.load(file)

    search_obj = json.loads(search_obj)  # Convert JSON string to object
    search_keyword = search_obj["searchWord"]
    search_range = search_obj["searchRange"]

    matching_documents = []

    for document in documents:
        title = document['title']
        topic = document.get('topic', [])
        context = document.get('context', [])

        separate_matches = 0
        separate_weight_fact = 0

        if search_range == "topic":
            combined_matches = sum(topic.count(search_keyword) for topic in topic)
            combined_weight_fact = combined_matches * 8

            for word in search_keyword.split():
                separate_matches += sum(topic.count(word) for topic in topic)
                separate_weight_fact += separate_matches * 8

        elif search_range == "title":
            combined_matches = title.count(search_keyword)
            combined_weight_fact = combined_matches * 10


            for word in search_keyword.split():
                separate_matches += title.count(word)
                separate_weight_fact += separate_matches * 10

        else:
            combined_title_matches = title.count(search_keyword)
            combined_topic_matches = sum(topic.count(search_keyword) for topic in topic)
            combined_context_matches = sum(item.count(search_keyword) for item in context)
            combined_matches = combined_title_matches + combined_topic_matches + combined_context_matches
            combined_weight_fact = (combined_title_matches * 10) + (combined_topic_matches * 8) + (combined_context_matches * 2)

            for word in search_keyword.split():
                title_matches = title.count(word)
                topic_matches = sum(topic.count(word) for topic in topic)
                context_matches = sum(item.count(word) for item in context)
                separate_matches += title_matches + topic_matches + context_matches
                separate_weight_fact += (title_matches * 10) + (topic_matches * 8) + (context_matches * 2)

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






input = {"searchWord":"green waste","searchRange":"topic"}
input_json = json.dumps(input)
print(search(input_json))
