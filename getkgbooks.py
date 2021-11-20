import requests
import os
import re
from bs4 import BeautifulSoup
import time
import json
from Book import Book
from savebooktodb import saveBookTodb,checkIfNoExistBookByUrl

savepath="J://kgbook//books//"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
main_url='https://kgbook.com/'
bookcount=0

'''
获取目录
'''
def getcategory():
    req_result=requests.get(main_url,headers=headers)
    if req_result.status_code==200:
        htmlstr=req_result.content.decode('utf-8')
        soup = BeautifulSoup(htmlstr, 'lxml')
        categorys=soup.find_all(attrs={'id': 'category'})[0].ul
        for li in categorys.find_all(name='li'):
            print('开始抓取'+li.a.attrs['href']+"--"+li.string)
            getcategroydetail(main_url+li.a.attrs['href'],li.string)
            time.sleep(1)

'''
获取目录详情创建目录
'''
def getcategroydetail(url,categroy):
    #新建目录
    categroy_path=createdir(savepath,categroy)
    getbookslist(url,categroy_path)

'''
获取书籍列表
'''
def getbookslist(bookurlstr,categroy_path):
    book_result=requests.get(bookurlstr,headers=headers)
    bookhtmlstr=book_result.content.decode('utf-8')
    soup = BeautifulSoup(bookhtmlstr, 'lxml')
    booklists=soup.select('.channel-item')
    for bookinfo_div in booklists:
        booktitle_div=bookinfo_div.select('.list-title')[0]
        bookurl=booktitle_div.a.attrs['href']
        getbookdetail(bookurl,categroy_path)
    next_pag=soup.find(name='a',text=re.compile('下一页'))
    if next_pag is not None:
        next_url=next_pag.attrs['href']
        print('爬取下一页：'+next_url)
        getbookslist(next_url,categroy_path)
        time.sleep(1)

'''
获取书籍详情
'''
def getbookdetail(bookurl,categroy_path):
    print(bookurl)
    global bookcount
    bookcount+=1
    print('bookcount:'+str(bookcount))
    if not re.match('.*?kgbook.*?',bookurl):
        bookurl=main_url+bookurl
    try:
        bookdetail_result=requests.get(bookurl,headers=headers)
        bookdetailhtmlstr=bookdetail_result.content.decode('utf-8')
        bookdetailsoup = BeautifulSoup(bookdetailhtmlstr, 'lxml')
        getbookfortype(bookurl,categroy_path,bookdetailsoup,'mobi')
        getbookfortype(bookurl,categroy_path,bookdetailsoup,'epub')
        getbookfortype(bookurl,categroy_path,bookdetailsoup,'azw3')
        getbookfortype(bookurl,categroy_path,bookdetailsoup,'pdf')
    except Exception as e:
        print('Error:',e)

'''
根据书籍资源类型下载资源
'''
def getbookfortype(bookurl,categroy_path,bookdetailsoup,booktype):
    booktitle=bookdetailsoup.select('.news_title')[0].text.strip()
    bookauthor=bookdetailsoup.select('#news_details')[0].ul.li.find(text=re.compile('作者：(.*?)')).strip()
    bookauthor=bookauthor.replace('作者：','')
    booktitleinfo="《"+booktitle+'》-'+bookauthor
    print('书籍详情：---'+booktitleinfo)
    book_url_item=bookdetailsoup.find(name='a',text=re.compile(booktype,re.I))
    if book_url_item is not None:
        downloadurl=book_url_item.attrs['href']
        print('下载地址：'+downloadurl)
        if checkIfNoExistBookByUrl(downloadurl):
            r = requests.get(downloadurl)
            if r.status_code==200:
                savepath=createdir(categroy_path,booktitleinfo)
                filename=booktitle+"."+booktype
                savebook(r.content,savepath,filename)
                p,f=os.path.split(categroy_path)
                bookcategory=f
                book=Book(bookcategory,booktitle,bookauthor,bookurl,downloadurl,savepath,"苦瓜书盘",booktype)
                print(book.toString())
                #savebooktojson(book)
                saveBookTodb(book)
            else:
                print('下载失败：status_code='+str(r.status_code))
    else:
        print('没有'+booktype+'格式的书')

'''
将获取的信息保存至文件
'''
def savebooktojson(book):
    bookdata={
        'booksource':book.booksource,
        'booktype':book.booktype,
        'bookcategory':book.bookcategory,
        'bookname':book.bookname,
        'bookauthor':book.bookauthor,
        'bookurl':book.bookurl,
        'bookdownloadurl':book.bookdownloadurl,
        'booksavepath':book.booksavepath
    }
    bookjson=json.dumps(bookdata,ensure_ascii=False) #ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了
    print(bookjson)
    with open('data.json', 'a',encoding='gbk') as file:
        file.write(bookjson+'\n')

'''
根据目录创建文件夹
'''
def createdir(savepath,dir):
    path=os.path.join(savepath,dir)
    isExists=os.path.exists(path)
    if isExists:
        print('已经存在'+dir)
    else:
        print('创建目录'+dir)
        os.mkdir(path)
    return path

'''
下载书籍资源
'''
def savebook(content,savepath,savefilename):
    savefile=os.path.join(savepath,savefilename)
    with open(savefile, "wb") as code:
       code.write(content)

if __name__=='__main__':
    getcategory()
    print('bookcount:'+str(bookcount))
