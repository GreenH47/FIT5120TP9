import os
import json
import glob
from bs4 import BeautifulSoup
import boto3


# Function to convert HTML page to JSON format
def convert_html_to_json(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data from HTML content
    url = os.path.join(os.path.dirname(html_file), os.path.basename(html_file).replace('.cshtml', '')).replace('\\', '/')

    # Convert title to lowercase
    title = soup.title.string.lower() if soup.title else None

    # Convert time to lowercase
    time = soup.find(class_="time").string.split("create at ")[1].lower() if soup.find(class_="time") else None

    # Convert topics to lowercase
    topics = [topic.string.lower() for topic in soup.find(class_="topic").ul.find_all("li")] if soup.find(class_="topic") else None

    # Convert context to lowercase
    context = [p.get_text(strip=True).lower() for p in soup.find_all('p')]

    # Convert image URLs to lowercase
    images = [img['src'].lower() for img in soup.find_all('img')]

    # Create JSON object
    data = {
        "URL": url,
        "title": title,
        "time": time,
        "topic": topics,
        "context": context,
        "images": images
    }

    print(data)
    return data



# Function to search for CSHTML files and update the index
def search_index():
    # Search for CSHTML files in the current directory and its subdirectories
    cshtml_files = glob.glob("**/*.cshtml", recursive=True)

    # Check if the document.json file exists
    json_file_exists = os.path.exists("document.json")

    if json_file_exists:
        # Load existing JSON data from the file
        with open("document.json", 'r') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = []

    output_data = []

    # Convert each CSHTML file to JSON and update existing data
    for cshtml_file in cshtml_files:
        if not cshtml_file.endswith(('_ViewStart.cshtml', '_ViewImports.cshtml')) and not cshtml_file.startswith(
                ('Home', 'Shared', 'SearchResults')):
            data = convert_html_to_json(cshtml_file)
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

    # Upload the index to DynamoDB
    user_input = input("Do you want to upload the index? (Y/N): ")
    if user_input.lower() == "y" or user_input.lower() == "Y":
        upload_index()
    else:
        print("Index not upload.")

# Function to upload the index to DynamoDB
def upload_index():
    # Initialize the DynamoDB client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
                              aws_secret_access_key='r7WNIZx59YHHQVlzkxw2zfgdfw83TRlQZK3UPJ8e')

    # Get a reference to your DynamoDB table
    table = dynamodb.Table('search_index')

    # Load the JSON file
    with open('document.json') as file:
        data = json.load(file)

    # Iterate over the data and put each item into the table
    for item in data:
        # Store the item in DynamoDB without specifying the Key parameter
        table.put_item(Item=item)

    print("Data imported successfully to DynamoDB.")


def start():
    user_input = input("Do you want to update the index? (Y/N): ")
    if user_input.lower() == "y":
        search_index()
    else:
        print("Index not updated.")

start()