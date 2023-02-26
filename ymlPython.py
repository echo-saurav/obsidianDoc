import os
import yaml

# The directory containing the Markdown files
directory = './docs'
layout = "default"

def readOldYml(path):
    # Read the existing YAML front matter, if any
    with open(path, 'r') as f:
        content = f.read()
        try:
            existing_front_matter = yaml.safe_load(
                content.split('---')[1])
            print(f"path:{path} yml:{existing_front_matter}")                
            return existing_front_matter,content
        except (IndexError, yaml.parser.ParserError):
            existing_front_matter = {}
            return existing_front_matter,content

def writeUpdatedYml(path,front_matter,existing_front_matter,content):
    # Write the updated front matter and content to the file
    with open(path, 'w') as f:
        f.write('---\n')
        yaml.dump(front_matter, f, default_flow_style=False)
        f.write('---\n')
        if existing_front_matter:
            content = content.split('---', 2)[2].lstrip()
        f.write(content)




def print_directory_tree(path, prefix=''):
    """
    Prints the directory tree structure starting from the given path.
    """
    # Print the current directory name
    # print(prefix + os.path.basename(path) + '/')
    
    # Get the list of files and directories in the current directory
    files = os.listdir(path)
    
    # Iterate over the files and directories and print them
    for file in files:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            # Recursive call to print the subdirectory tree
            print_directory_tree(filepath, prefix=prefix + '  ')
        else:
            if file.endswith(".md"):
                print(f"File: {file} : Parent:  {os.path.basename(path)} , FullPath:{path}")
                existing_front_matter,content = readOldYml(path+"/"+file)
                # get the base name and extension of the file
                base_name, extension = os.path.splitext(file)

                # remove the extension
                title = base_name
                if os.path.basename(path)!="docs":
                    parent = os.path.basename(path)
                else:
                    parent = ""    

                # Update the front matter fields
                if (parent != ''):
                    front_matter = {
                        'layout': layout,
                        'title': title,
                        'parent': parent
                    }
                else:
                    front_matter = {
                        'layout': layout,
                        'title': title,
                    }
                writeUpdatedYml(path+"/"+file, front_matter, existing_front_matter,content)
            else:
                print(f"{file}:not a md file")  


print_directory_tree(directory)



# # Loop over each file in the directory and its subdirectories
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.md'):
            # Set the page title to the file name
            title = os.path.splitext(filename)[0]
            parent = os.path.basename(os.path.dirname(root))
            print(f"{title}: parent: {parent} , root: {root} ")


# def old():
#     # Loop over each file in the directory and its subdirectories
#     for root, _, files in os.walk(directory):
#         for filename in files:
#             if filename.endswith('.md'):
#                 # Set the page title to the file name
#                 title = os.path.splitext(filename)[0]

#                 # Set the layout and parent directory based on the file location
#                 parent = ''
#                 if root.endswith('/docs'):
#                     layout = 'default'
#                     # parent = ''
#                 else:
#                     layout = 'default'
#                     parent = os.path.basename(os.path.dirname(root))

#                 # Read the existing YAML front matter, if any
#                 with open(os.path.join(root, filename), 'r') as f:
#                     content = f.read()
#                     try:
#                         existing_front_matter = yaml.safe_load(
#                             content.split('---')[1])
#                     except (IndexError, yaml.parser.ParserError):
#                         existing_front_matter = {}

#                 # Update the front matter fields
#                 if (parent != ''):
#                     front_matter = {
#                         'layout': existing_front_matter.get('layout', layout),
#                         'title': existing_front_matter.get('title', title),
#                         'parent': existing_front_matter.get('parent', parent)
#                     }
#                 else:
#                     front_matter = {
#                         'layout': existing_front_matter.get('layout', layout),
#                         'title': existing_front_matter.get('title', title),
#                     }

#                 # Write the updated front matter and content to the file
#                 with open(os.path.join(root, filename), 'w') as f:
#                     f.write('---\n')
#                     yaml.dump(front_matter, f, default_flow_style=False)
#                     f.write('---\n')
#                     if existing_front_matter:
#                         content = content.split('---', 2)[2].lstrip()
#                     f.write(content)
