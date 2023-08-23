import json
import urllib.request
def search(search_keyword):
    # read the json file from internet
    # Download the JSON file

    url = "https://carbonvic.s3.amazonaws.com/document.json"
    response = urllib.request.urlopen(url)
    json_data = response.read().decode()
    documents = json.loads(json_data)

    # # Read the JSON file from local
    # with open('document.json', 'r') as file:
    #     documents = json.load(file)



    # Creating a list to store the matching documents
    matching_documents = []


    # Loop through each document to check for matches
    for document in documents:
        title = document['title']
        topic = document.get('topic', [])
        context = document.get('context', [])


        # Calculate combined matches and weight factor
        combined_title_matches = title.count(search_keyword)
        combined_topic_matches = sum(topic.count(search_keyword) for topic in topic)
        combined_context_matches = sum(item.count(search_keyword) for item in context)
        combined_matches = combined_title_matches + combined_topic_matches + combined_context_matches
        combined_weight_fact = ((combined_title_matches * 10) + (combined_topic_matches * 8) + (
                    combined_context_matches * 2))*10

        # Calculate separate matches and weight factor
        separate_matches = 0
        separate_weight_fact = 0
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
                "combine_matches": combined_matches,
                "combine_weight_fact": combined_weight_fact,
                "separate_matches": separate_matches,
                "separate_weight_fact": separate_weight_fact,
                "total_weight_fact": combined_weight_fact+ separate_weight_fact
            })

    # Sort the matching_documents list based on the total weight factor (descending order)
    matching_documents.sort(key=lambda d: d['total_weight_fact'], reverse=True)

    # Print the search results
    # for document in matching_documents:
    #     print("URL:", document['URL'])
    #     print("Title:", document['title'])
    #     print("Combine Matches:", document['combine_matches'])
    #     print("Combine Weight Fact:", document['combine_weight_fact'])
    #     print("Separate Matches:", document['separate_matches'])
    #     print("Separate Weight Fact:", document['separate_weight_fact'])
    #     print("Total Weight Fact:", document['total_weight_fact'])
    #     print("------------------")



    # Prepare the search results JSON object
    search_results = {
        "search_keyword": search_keyword,
        "results": matching_documents
    }

    # Convert the search results to JSON string
    json_results = json.dumps(search_results, indent=4)



    # Print the search results JSON
    print(json_results)


def input_keyword():
    search_keyword = input("Enter the search keyword: ")
    # check if the search keyword is empty
    # and the search keyword can only have alphabets and numbers and spaces
    # if search_keyword == "" or not search_keyword.replace(" ", "").isalnum():
    #     print("Invalid search keyword")
    #     input_keyword()
    search(search_keyword)


input_keyword()