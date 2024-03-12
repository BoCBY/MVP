import os

folder_path = r'C:\Users\admin\Desktop\structure\Server\non_cust\exercise\calculus\present\202403101348\answer\7'

data_dict = {}

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            like_line = file.readline().strip()
            dislike_line = file.readline().strip()
            like = int(like_line.split(': ')[1])
            dislike = int(dislike_line.split(': ')[1])
            data_dict[file_name] = {'like': like, 'dislike': dislike}

print(data_dict)