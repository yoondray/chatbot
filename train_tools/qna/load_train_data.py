import pymysql
import openpyxl

from Scripts.chatbot.config.DatabaseConfig import *

def all_clear_train_data(db):
    sql='''
        delete from chatbot_train_data
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    sql='''
        alter table chatbot_train_data auto_increment=1
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)

def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql='''
        insert chatbot_train_data(intent, ner, query, answer, answer_image)
        values(
            '%s', '%s', '%s', '%s', '%s'
        )
        '''% (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

    sql=sql.replace("'None'","null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} SAVE'.format(query.value))
        db.commit()

    train_file = './train_data.xlsx'
    db = None
    try:
        db = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            db=DB_NAME,
            charset='utf8'
            )

        all_clear_train_data(db)

        wb=openpyxl.load_workbook(train_file)
        sheet = wb['Sheet1']
        for row in sheet.iter_rows(min_row=2):
            insert_data(db, row)

        wb.close()

    except Exception as e:
        print(e)

    finally:
        if db is not None:
            db.close()
            
        



    
