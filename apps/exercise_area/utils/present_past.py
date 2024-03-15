import os
import time
import schedule
import shutil
from datetime import datetime
from pdf import create_questions_pdf

EXERCISE = os.path.join('structure', 'Server', 'non_cust', 'exercise')
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
COMPUTER_EXERCISE_PATH = os.path.join(COMPUTER_DESK, EXERCISE)
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
NOTEBOOK_EXERCISE_PATH = os.path.join(NOTEBOOK_DESK, EXERCISE)

def present_to_past(subject):
    '''時間期限到, 把present裡的當期資料夾整個搬遷至past
       並重建present的結構'''
       
    # 把present資料夾移到past
    present_path = os.path.join(COMPUTER_EXERCISE_PATH, subject, 'present')
    in_present_folder_path = os.path.join(present_path, os.listdir(present_path)[0])
    past_path = os.path.join(COMPUTER_EXERCISE_PATH, subject, 'past')
    shutil.move(in_present_folder_path, past_path)
    print('移植成功')
     
    # 重新創建present的結構
    current_time = datetime.now().strftime('%Y%m%d') # 測試階段才要小時跟分, 正式的就到日即可
    new_in_present_folder = os.path.join(present_path, current_time)
    os.makedirs(new_in_present_folder) # 創建第一層資料夾(以創建日期為名)
    answer_area = os.path.join(new_in_present_folder, 'answer')
    os.makedirs(answer_area) # 創建答案區資料夾
    for i in range(1, 13):
        # 在答案區資料夾裡面創建1~12題的資料夾
        os.makedirs(os.path.join(answer_area, str(i)))
    print('成功重構present')

def periodically():
    ''' 每兩週要自動執行這個函數一次 '''
    present_to_past('calculus') # 期限到把present移植到past, 並重構present的結構
    create_questions_pdf('calculus', False) # 創建本期試題
    
    # 有幾門科目就要執行幾組, 並且參數是科目的名稱
    present_to_past('linear_algebra')
    create_questions_pdf('linear_algebra', False)
    
    present_to_past('general_physics')
    create_questions_pdf('general_physics', False)
    
    return None

schedule.every(2).hours.do(periodically) # 自動執行函數

 # 主迴圈，用來不斷檢查是否有定時任務需要執行
while True:
    schedule.run_pending()
    time.sleep(60*30)  # 每隔30分鐘檢查一次
    
