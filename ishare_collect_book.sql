/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50625
Source Host           : localhost:3306
Source Database       : bookdb

Target Server Type    : MYSQL
Target Server Version : 50625
File Encoding         : 65001

Date: 2021-11-20 18:04:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ishare_collect_book
-- ----------------------------
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
