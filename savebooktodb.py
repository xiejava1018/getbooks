import pymysql
import json

db = pymysql.connect(host='localhost',user='root', password='mnbvvbnm', port=3306,db="bookdb",charset="utf8")

def saveBookTodb(book):
    cursor = db.cursor()
    try:
        if checkIfNoExistBookByUrl(book.bookdownloadurl):
            insertSql='insert into ishare_collect_book (booksource,booktype,bookcategory,bookname,bookauthor,bookurl,bookdownloadurl,booksavepath) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            param=(book.booksource,book.booktype,book.bookcategory,book.bookname,book.bookauthor,book.bookurl,book.bookdownloadurl,book.booksavepath)
            print(insertSql)
            cursor.execute(insertSql,param)
            db.commit()
    except Exception as e:
        print('Error:',e)

def checkIfNoExistBookByUrl(bookdownloadurl):
    cursor = db.cursor()
    try:
        selectSql="select * from ishare_collect_book where bookdownloadurl=%s"
        selectparam=(bookdownloadurl)
        cursor.execute(selectSql,selectparam)
        values = cursor.fetchall()
        if len(values)>0:
            print("已经存在："+str(values))
            return False
        else:
            return True
    except Exception as e:
        print('Error:',e)

def checkIfNoExistBookByBookUrl(bookUrl):
    cursor = db.cursor()
    try:
        selectSql="select * from ishare_collect_book where bookurl=%s"
        selectparam=(bookUrl)
        cursor.execute(selectSql,selectparam)
        values = cursor.fetchall()
        if len(values)>0:
            print("已经存在："+str(values))
            return False
        else:
            return True
    except Exception as e:
        print('Error:',e)

def checkIfNoSameBook(book):
    cursor = db.cursor()
    try:
        selectSql="select * from ishare_collect_book where booksource=%s and booktype=%s and bookname=%s and bookauthor=%s"
        selectparam=(book.booksource,book.booktype,book.bookname,book.bookauthor)
        cursor.execute(selectSql,selectparam)
        values = cursor.fetchall()
        print(values)
        if len(values)>0:
            return False
        else:
            return True
    except Exception as e:
        print('Error:',e)

def saveJSONdatetodb(db,bookstr):
    cursor = db.cursor()
    try:
        bookjson=json.loads(bookstr)
        bookcategory=bookjson.get('bookcategory')
        bookname=bookjson.get('bookname')
        bookauthor=bookjson.get('bookauthor')
        bookurl=bookjson.get('bookurl')
        booksavepath=bookjson.get('booksavepath')
        insertSql='insert into ishare_collect_book (bookcategory,bookname,bookauthor,bookurl,booksavepath) values (%s,%s,%s,%s,%s)'
        param=(bookcategory,bookname,bookauthor,bookurl,booksavepath)
        print(insertSql)
        cursor.execute(insertSql,param)
        db.commit()
    except Exception as e:
        print('Error:',e)


def readJsonData(filename):
    with open(filename, 'r') as file:
         for bookstr in file:
             print(bookstr)
             saveJSONdatetodb(db,bookstr)
    db.close()

if __name__=='__main__':
    readJsonData('data.json')

