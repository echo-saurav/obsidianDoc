import os
import yaml

# The directory containing the Markdown files
directory = './docs'
layout = "default"


def addIndex(filename, title):
    default_frontmatter = {
        'layout': layout,
        'title': title,
        "has_children": True
    }

    try:
        # open the file for writing, but raise an error if it already exists
        with open(filename, "x") as f:
            # write some data to the file
            f.write('---\n')
            yaml.dump(default_frontmatter, f, default_flow_style=False)
            f.write('---\n')

    except FileExistsError:
        # if the file already exists, open it for writing instead
        with open(filename, "w") as f:
            # write some data to the file
            f.write('---\n')
            yaml.dump(default_frontmatter, f, default_flow_style=False)
            f.write('---\n')


def readOldYml(path):
    # Read the existing YAML front matter, if any
    with open(path, 'r') as f:
        content = f.read()
        try:
            existing_front_matter = yaml.safe_load(
                content.split('---')[1])
            # print(f"path:{path} yml:{existing_front_matter}")
            return existing_front_matter, content
        except (IndexError, yaml.parser.ParserError):
            existing_front_matter = {}
            return existing_front_matter, content


def updateYmlAndTitle(path, front_matter, existing_front_matter, content):
    # Write the updated front matter and content to the file
    with open(path, 'w+') as f:
        f.write('---\n')
        yaml.dump(front_matter, f, default_flow_style=False)
        f.write('---\n')

        # Add the line to the file if it doesn't already exist
        line_to_write= f"# {front_matter.get('title')}"
        contents = f.read()
        if line_to_write not in contents:
            f.write(f"{line_to_write}\n")

        if existing_front_matter:
            content = content.split('---', 2)[2].lstrip()
        f.write(content)



def print_directory_tree(path, prefix=''):
    # Get the list of files and directories in the current directory
    files = os.listdir(path)

    # Iterate over the files and directories and print them
    for file in files:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            # Recursive call to print the subdirectory tree
            print_directory_tree(filepath, prefix=prefix + '  ')
            base_name, extension = os.path.splitext(file)
            # remove the extension
            title = base_name

            if title!="media":
                addIndex(filepath+"/index.md", title)
        else:
            if file.endswith(".md"):
                # print(
                #     f"File: {file} : Parent:  {os.path.basename(path)} , FullPath:{path}")
                existing_front_matter, content = readOldYml(path+"/"+file)
                # get the base name and extension of the file
                base_name, extension = os.path.splitext(file)

                # remove the extension
                title = base_name
                if os.path.basename(path) != "docs":
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
                updateYmlAndTitle(path+"/"+file, front_matter,
                                existing_front_matter, content)


print_directory_tree(directory)


# # Loop over each file in the directory and its subdirectories
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.md'):
            # Set the page title to the file name
            title = os.path.splitext(filename)[0]
            parent = os.path.basename(os.path.dirname(root))
            # print(f"{title}: parent: {parent} , root: {root} ")

