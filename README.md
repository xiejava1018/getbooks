# python爬虫爬取电子书 getbooks

安装依赖

pip install requests

pip install pymysql

pip install beautifulsoup4

pip install lxml


数据库

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


