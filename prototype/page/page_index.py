import os
import json
import glob
from bs4 import BeautifulSoup


# Function to convert HTML page to JSON format
def convert_html_to_json(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data from HTML content
    url = html_file.replace('.html', '')
    title = soup.title.string
    time = soup.find(class_="time").string.split("create at ")[1]
    topics = [topic.string for topic in soup.find(class_="topic").ul.find_all("li")]
    context = [p.get_text(strip=True) for p in soup.find_all('p')]
    images = [img['src'] for img in soup.find_all('img')]

    # Create JSON object
    data = {
        "URL": url,
        "title": title,
        "time": time,
        "topic": topics,
        "context": context,
        "images": images
    }

    return data


# Search for HTML files in the same folder
html_files = glob.glob("*.html")

# Check if the document.json file exists
json_file_exists = os.path.exists("document.json")

if json_file_exists:
    # Load existing JSON data from the file
    with open("document.json", 'r') as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

output_data = []

# Convert each HTML file to JSON and update existing data
for html_file in html_files:
    data = convert_html_to_json(html_file)
    existing_url = [item for item in existing_data if item["URL"] == data["URL"]]

    # Replace existing data if the URL already exists
    if existing_url:
        existing_data.remove(existing_url[0])
        existing_data.append(data)
    else:
        existing_data.append(data)

    output_data.append(data)

# Save the updated data to the JSON file
with open("document.json", 'w') as json_file:
    json.dump(existing_data, json_file)

print("Conversion to JSON completed successfully.")
