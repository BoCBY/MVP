import os
import fitz
import random
from datetime import datetime

COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
EXERCISE = os.path.join('structure', 'Server', 'non_cust', 'exercise')

COMPUTER_EXERCISE_PATH = os.path.join(COMPUTER_DESK, EXERCISE)
NOTEBOOK_EXERCISE_PATH = os.path.join(NOTEBOOK_DESK, EXERCISE)

def create_questions_pdf(subject, one_button=False):
    easy_path = os.path.join(subject, 'pool', 'easy.pdf')
    medium_path = os.path.join(subject, 'pool', 'medium.pdf')
    med_up_path = os.path.join(subject, 'pool', 'med_up.pdf')
    hard_path = os.path.join(subject, 'pool', 'hard.pdf')

    # Define the file paths for the PDF files
    pdf_files = {
        'easy': os.path.join(COMPUTER_EXERCISE_PATH, easy_path),
        'medium': os.path.join(COMPUTER_EXERCISE_PATH, medium_path),
        'med_up': os.path.join(COMPUTER_EXERCISE_PATH, med_up_path),
        'hard': os.path.join(COMPUTER_EXERCISE_PATH, hard_path)
    }

    # Initialize a new PDF document for the exam
    question_doc = fitz.open()

    for difficulty in pdf_files.keys():
        pdf_path = pdf_files[difficulty]
        doc = fitz.open(pdf_path)
        page_num = random.randint(0, doc.page_count - 1) # pymupdf操作pdf檔案的頁數是有offset的(0-based)
        page = doc.load_page(page_num)
        pix = page.get_pixmap() # 把此份pdf檔隨機挑選到的這頁內容寫成一張圖片
        question_page = question_doc.new_page(width=pix.width, height=pix.height)
        question_page.insert_image((0, 0, pix.width, pix.height), pixmap=pix) # 將剛剛挑到的那一頁的圖片檔插入新的這個pdf檔裡
        doc.close()

    # Save the exam document to a new PDF file
    if one_button:
        one_button_path = os.path.join(subject, 'one_button', 'random_questions.pdf')
        question_doc_path = os.path.join(COMPUTER_EXERCISE_PATH, one_button_path)
        question_doc.save(question_doc_path)
        question_doc.close()
        print('one_button檔案創建成功')
        return question_doc_path

    current_time = datetime.now().strftime('%Y%m%d')
    regular_path = os.path.join(subject, 'present', current_time, current_time + '.pdf')
    question_doc_path = os.path.join(COMPUTER_EXERCISE_PATH, regular_path)
    question_doc.save(question_doc_path)
    question_doc.close()
    print('regular檔案創建成功')
    return question_doc_path
    
#create_questions_pdf('linear_algebra')
#create_questions_pdf('general_physics')
 