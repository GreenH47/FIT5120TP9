import json

# read the json file
with open('document.json', 'r') as file:
    documents = json.load(file)

#
search_keyword = input("Enter the search keyword: ")

# Creating a list to store the matching documents
matching_documents = []


for document in documents:
    title_matches = document['title'].count(search_keyword)
    topic_matches = sum(topic.count(search_keyword) for topic in document.get('topic', []))
    context_matches = sum(item.count(search_keyword) for item in document.get('context', []))
    total_matches = title_matches + topic_matches + context_matches
    if total_matches > 0:
        matching_documents.append({
            "URL": document['URL'],
            "title": document['title'],
            "matches": total_matches
        })

# Sort the matching_documents list based on the number of matches (descending order)
matching_documents.sort(key=lambda d: d['matches'], reverse=True)



# Prepare the search results JSON object
search_results = {
    "search_keyword": search_keyword,
    "results": matching_documents
}

# Convert the search results to JSON string
json_results = json.dumps(search_results, indent=4)

for document in matching_documents:
    print("URL:", document['URL'])
    print("Title:", document['title'])
    print("Matches:", document['matches'])
    print("------------------")
# Print the search results JSON
#print(json_results)