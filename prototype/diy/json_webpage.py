import json
import os


def generate_cshtml(filename, data):
    title = f'How to create {data["Project_Names"]} with your waste'
    topic_links = ['waste recycle', 'DIY']
    time = 'create at 2023-08-25'
    tools = data['Tools']
    materials = data['materials']
    steps = data['Steps']
    link = data['link']
    image = data['image']

    cshtml = f'''<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}

        h1 {{
            text-align: center;
        }}

        .topic {{
            font-weight: bold;
            margin-top: 15px;
        }}

        .subtitle {{
            font-weight: bold;
            margin-top: 10px;
        }}

        img {{
            display: block;
            margin: 20px auto;
            max-width: 400px;
        }}
    </style>

</head>
<body>
    <h1 class="title">{title}</h1>

    <div class="time">create at {time}</div>

    <div class="topic">
        <h2>Topics:</h2>
        <ul>
            {"".join(f'<li><a href="#" class="topic-link">{topic}</a></li>' for topic in topic_links)}
        </ul>
    </div>

    <h3 class="subtitle">Tools:</h3>
    <p>{", ".join(tools)}</p>

    <h3 class="subtitle">Materials:</h3>
    <p>{", ".join(materials)}</p>

    <h3 class="subtitle">Steps:</h3>
    <ol>
        {"".join(f'<li>{step}</li>' for step in steps)}
    </ol>

    <h3 class="subtitle">Link:</h3>
    <a href="{link}">{link}</a>

    {"".join(f'<img src="{img}" alt="Step Image">' for img in image)}
</body>
'''

    # Append the JavaScript code
    cshtml += f'''
<script>
    document.addEventListener("DOMContentLoaded", function () {{
        var topicLinks = document.getElementsByClassName("topic-link");

        function handleTopicLinkClick(event) {{
            event.preventDefault();

            var topic = this.textContent.trim();

            // Redirect to the search results page with the topic as the search query and "topic" as the search range
            var redirectUrl = "/SearchResults/Index?search=" + encodeURIComponent(topic) + "&range=topic";
            window.location.href = redirectUrl;
        }}

        for (var i = 0; i < topicLinks.length; i++) {{
            topicLinks[i].addEventListener("click", handleTopicLinkClick);
        }}
    }});
</script>
'''

    # Create the Diy directory if it doesn't exist
    if not os.path.exists('Diy'):
        os.mkdir('Diy')

    with open(f'Diy/{filename}.cshtml', 'w') as file:
        file.write(cshtml)


# Load the JSON file
with open('recipe.json') as file:
    recipes = json.load(file)

# Iterate through each recipe and generate the cshtml file
for recipe in recipes:
    filename = recipe['Project_Names'].replace(' ', '_')
    generate_cshtml(filename, recipe)
