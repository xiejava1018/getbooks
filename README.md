# python爬虫爬取电子书 getbooks

**代码详细说明见：**  http://xiejava.ishareread.com/posts/eab21fe5/

Python爬虫获取电子书资源实战的全部代码，包括爬取->分析、解析->保存至本地及数据库。[下载](https://download.csdn.net/download/fullbug/10468606)
# 一、安装依赖

pip install requests

pip install pymysql

pip install beautifulsoup4

pip install lxml


# 二、导入数据库表

```
DROP TABLE IF EXISTS `ishare_collect_book`;
CREATE TABLE `ishare_collect_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookcategory` varchar(255) DEFAULT NULL,
  `bookname` varchar(255) DEFAULT NULL,
  `bookauthor` varchar(255) DEFAULT NULL,
  `bookurl` varchar(255) DEFAULT NULL,
  `bookdownloadurl` varchar(255) DEFAULT NULL,
  `booktype` varchar(255) DEFAULT NULL,
  `booksource` varchar(255) DEFAULT NULL,
  `booksavepath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5820 DEFAULT CHARSET=utf8;
```
# 三、修改savebooktodb.py中的数据库连接串
根据自己的环境savebooktodb.py中的修改数据库连接串参数
```
db = pymysql.connect(host='localhost',user='root', password='mnbvvbnm', port=3306,db="bookdb",charset="utf8")
```

# 四、运行getkgbooks.py
根据自己的实际情况修改getkgbooks.py中电子书资源保存的本地路径
```
savepath="J://kgbook//books//"
```
运行getkgbooks.py

# 五、运行效果
运行效果如下：

1、爬取过程
![爬取过程](http://xiejava.gitee.io/xiejavaimagesrc/images/2021/20211120/爬取过程.png)

2、爬取记录的json信息
data.json的信息如下：
![爬取记录](http://xiejava.gitee.io/xiejavaimagesrc/images/2021/20211120/爬取记录的json信息.png)

3、爬取获取的资源
按目录都已经整理好了，够你看的了。
![获取的资源](http://xiejava.gitee.io/xiejavaimagesrc/images/2021/20211120/获取的资源.png)

Python爬虫获取电子书资源实战的全部代码，包括爬取->分析、解析->保存至本地及数据库。[下载](https://download.csdn.net/download/fullbug/10468606)

