import boto3
import os

def upload_images_to_s3(bucket_name):
    # AWS credentials configuration
    session = boto3.Session(
        aws_access_key_id='AKIATC3T7V7PPEVK6WM2',
        aws_secret_access_key='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',
    )

    s3_client = session.client('s3')

    # Define the local 'img' folder path
    local_img_folder = 'img'

    # List all image files in the local folder
    image_files = [f for f in os.listdir(local_img_folder) if os.path.isfile(os.path.join(local_img_folder, f))]

    # Upload each image to S3 and store the image URLs
    image_urls = []
    for file in image_files:
        file_path = os.path.join(local_img_folder, file)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            key = f'img/{file}'

            # Upload the image file to your S3 bucket
            s3_client.upload_file(file_path, bucket_name, key)
            print(f"Image file '{file_path}' uploaded to S3 bucket '{bucket_name}'.")

            # Construct the S3 image URL
            s3_image_url = f"https://{bucket_name}.s3.amazonaws.com/{key}"
            image_urls.append(s3_image_url)

    # Check if the HTML file already exists
    if os.path.isfile('image_upload.html'):
        with open('image_upload.html', 'r') as html_file:
            existing_content = html_file.read()

        # Find the closing </style> tag position to insert new images after it
        style_tag_index = existing_content.index('</style>') + len('</style>')
        # insert at new line


        # Append the newly uploaded image URLs to the existing content
        new_content = existing_content[:style_tag_index] + '\n'
        for url in image_urls:
            new_content += f'<img src="{url}">\n'

        # Save the updated HTML content to the 'image_upload.html' file
        with open('image_upload.html', 'w') as html_file:
            html_file.write(new_content)
    else:
        # If the HTML file doesn't exist, create a new one with the image URLs
        html_content = '<style>img { width: 400px; height: 400px; display: block; margin-bottom: 10px; }</style>\n'

        for url in image_urls:
            html_content += f'<img src="{url}">\n'

        # Save the HTML content to the 'image_upload.html' file
        with open('image_upload.html', 'w') as html_file:
            html_file.write(html_content)



    print("Images uploaded successfully to S3 and HTML page updated.")



# Usage example:
bucket_name = 'carbonvic'
upload_images_to_s3(bucket_name)
