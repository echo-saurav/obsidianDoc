import os
import re
import requests
import json

path = "/home/saurav/media/obsidian/Eternal/"

url_pattern = re.compile(r'\[(.*?)\]\((https?://.*?)\)')
tag_pattern = r'(#\w+)'


# Define a function to recursively search for URLs in a directory
def find_urls_in_directory(dir_path):
    urls = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file has a .md extension
            if file.endswith('.md'):
                # Open the file and read its contents
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()
                    # Use the pattern to find all matches in the file contents
                    url_matches = re.findall(url_pattern, contents)
                    # Loop through the URL matches and extract the tags
                    for url_match in url_matches:
                        # url_text, url_link = url_match
                        url_text, url_link, *_ = url_match

                        tag_matches = re.findall(tag_pattern, contents)
                        # tags = ''.join(tag_matches)
                        # print(type(tag_matches))
                        urls.append((url_link, tag_matches))

    return urls


# Call the function with the directory path as argument
urls = find_urls_in_directory(path)

# Print out all the URLs and their corresponding tags
# for url, tags in urls:
#     print(url, tags)


api="http://192.168.0.120:8102/addlink"
# for url, tags in urls:
for i, (url, tags) in enumerate(urls[:10]):    
# url="https://www.youtube.com/watch?v=bVeOdNi6e-k"
# tags=["#one","#two"]

    if isinstance(tags, list) and len(tags)>0:
        params = {
            'url':url,
            'tags':tags
        }
    else:
        print("not list")
        params = {
            'url':url,
            'tags': [""]
        }

    print(params)
    resp = requests.get(url=api,  json=params)
    print(f"Response content: {resp.content}")




