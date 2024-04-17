import os

# 學習區的路徑
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
USER_INFO = os.path.join('structure', 'Server', 'cust', 'user_info')
# PATH = os.path.join('C:\\', 'Users', 'admin', 'Desktop', 'structure', 'Server', 'cust', 'user_info') # 所有的用戶到這邊的路徑都一樣
COMPUTER_USER_INFO_PATH = os.path.join(COMPUTER_DESK, USER_INFO)
NOTEBOOK_USER_INFO_PATH = os.path.join(NOTEBOOK_DESK, USER_INFO)

LEARNING = os.path.join('email#1', 'learning') # 根據用戶所註冊的email來修改email#1, 也就是email#1要是動態的
LEARNING_COMPUTER_PATH = os.path.join(COMPUTER_USER_INFO_PATH, LEARNING) # 到達此用戶學習區用來放置各個影片的筆記空間 -> 一個url對應一個資料夾
LEARNING_NOTEBOOK_PATH = os.path.join(NOTEBOOK_USER_INFO_PATH, LEARNING)

# 習題區的路徑
INDIVIDUAL_EXERCISE_ANSWER_AREA = os.path.join('email#1', 'note', 'exercise_answer') # email#1替換成個別用戶註冊的信箱, 就是個別用戶的專屬路徑了
EXERCISE_ANSWER_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, INDIVIDUAL_EXERCISE_ANSWER_AREA)

# 自定義區的路徑
SELF_DEFINED_PATH = os.path.join('email#1', 'note', 'self_defined')
SELF_DEFINED_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, SELF_DEFINED_PATH)

# 科目英文名轉中文名的映射
ENG_TO_CH = {
    'calculus': '微積分',
    'linear_algebra': '線性代數',
    'general_physics': '普通物理',
    'data_structure': '資料結構',
}
# 中文轉英文的映射
CH_TO_ENG ={v:k for k, v in ENG_TO_CH.items()}

def clean_learning(root_directory_path=LEARNING_COMPUTER_PATH):
    video_list = []
    for root, dirs, files in os.walk(root_directory_path):
        relative_root = os.path.relpath(root, root_directory_path)
        if relative_root == '.':
            continue
        video = {}
        video_info = {}
        thumbnail = {}
        lecturer = relative_root.split('[]')[0]
        course = relative_root.split('[]')[1]
        video_id = relative_root.split('[]')[2]
        video_info['lecturer'] = lecturer
        video_info['course'] = course
        for item in files:
            img_content, caption = os.path.splitext(item)[0].replace(';', ':', 4).split('-')
            thumbnail[img_content] = caption
        video_info['thumbnail'] = thumbnail
        video[video_id] = video_info
        video_list.append(video)
    return video_list
        
def clean_exercise_answer(root_directory_path=EXERCISE_ANSWER_AREA_PATH):
    subject_list = []
    for root, dirs, files in os.walk(root_directory_path):
        relative_root = os.path.relpath(root, root_directory_path)
        if relative_root == '.':
            continue
        answer_list = []
        subject = {}
        for items in files:
            unit = os.path.splitext(items)[0].split('[]') # 每一題都是一個list
            unit[1:3] = ['-'.join(unit[1:3])] # 把第二個元素(期數)和第三個元素(題號)用-連接, 合併成一個
            answer_list.append(unit)
        subject[ENG_TO_CH[relative_root]] = answer_list # 把科目名稱由英文轉成中文
        subject_list.append(subject)
    return subject_list
        
def clean_self_defined(root_directory_path=SELF_DEFINED_AREA_PATH):
    location_list = []
    for root, dirs, files in os.walk(root_directory_path):
        relative_root = os.path.relpath(root, root_directory_path)
        relative_root = '首頁' if relative_root == '.' else '首頁\\' + relative_root
        relative_root = relative_root.replace('\\', ' > ')
        location = {}
        files_list = []
        for items in files:
            files_list.append(os.path.splitext(items)[0])
        location[relative_root] = files_list
        location_list.append(location)
    return location_list


video_list = clean_learning()
print(video_list, '\n')
subject_list = clean_exercise_answer()
print(subject_list, '\n')
location_list = clean_self_defined()
print(location_list, '\n')
