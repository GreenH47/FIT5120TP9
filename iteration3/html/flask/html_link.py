import os


def update_resource_links():
    templates_path = 'templates'
    static_path = 'static'
    file_extension = '.html'

    # Loop through all files in the templates folder
    for filename in os.listdir(templates_path):
        if filename.endswith(file_extension):
            file_path = os.path.join(templates_path, filename)

            # Read the content of the file with utf-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Update the resource link
            updated_content = content.replace('href="css/', 'href="/static/css/')
            updated_content = updated_content.replace('src="js/', 'src="/static/js/')
            # Update the resource links for images
            updated_content = updated_content.replace('src="images/', 'src="/static/images/')

            updated_content = updated_content.replace('srcset="images/', 'srcset="/static/images/')

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

    print('Resource links updated successfully.')


# Call the function to update the resource links
update_resource_links()
