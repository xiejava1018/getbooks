class Book(object):

    def __init__(self,bookcategory,bookname,bookauthor,bookurl,bookdownloadurl,booksavepath,booksource,booktype):
        self.bookcategory=bookcategory
        self.bookname=bookname
        self.bookauthor=bookauthor
        self.bookurl=bookurl
        self.bookdownloadurl=bookdownloadurl
        self.booksavepath=booksavepath
        self.booksource=booksource
        self.booktype=booktype

    def toString(self):
        return {"bookcategory":self.bookcategory,"bookname":self.bookname,"bookauthor":self.bookauthor,"bookurl":self.bookurl,"bookdownloadurl":self.bookdownloadurl,"booksavepath":self.booksavepath,"booksource":self.booksource,"booktype":self.booktype}

