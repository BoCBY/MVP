import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{subindent}{file}')

# Specify the path of the folder you want to display
path = r'C:\Users\admin\Desktop\structure\Server\non_cust\exercise\calculus\past'

# Call the function to list the files and folders
list_files(path)