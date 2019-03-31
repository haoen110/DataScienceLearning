-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: MOSHOU
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `MOSHOU`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `MOSHOU` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `MOSHOU`;

--
-- Table structure for table `hero`
--

DROP TABLE IF EXISTS `hero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hero` (
  `id` int(11) DEFAULT NULL,
  `name` char(15) DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `country` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hero`
--

LOCK TABLES `hero` WRITE;
/*!40000 ALTER TABLE `hero` DISABLE KEYS */;
INSERT INTO `hero` VALUES (1,'曹操','男','魏国'),(2,'小乔','女','吴国'),(3,'诸葛亮','男','蜀国'),(4,'貂蝉','女','东汉'),(5,'赵子龙','男','蜀国'),(6,'魏延','男','蜀国');
/*!40000 ALTER TABLE `hero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo`
--

DROP TABLE IF EXISTS `sanguo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sanguo` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `gongji` int(11) DEFAULT NULL,
  `fangyu` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo`
--

LOCK TABLES `sanguo` WRITE;
/*!40000 ALTER TABLE `sanguo` DISABLE KEYS */;
INSERT INTO `sanguo` VALUES (1,'诸葛亮',120,20,'男','蜀国'),(2,'司马懿',119,25,'男','魏国'),(3,'关羽',188,60,'男','蜀国'),(4,'赵云',360,68,'男','蜀国'),(5,'孙权',100,60,'男','吴国'),(6,'貂蝉',666,10,'女','魏国'),(7,NULL,1000,99,'男','蜀国'),(8,'',1005,88,'女','蜀国');
/*!40000 ALTER TABLE `sanguo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `db3`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `db3` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `db3`;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `c_name` varchar(15) DEFAULT NULL,
  `cfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,131100,'石家庄市',130000),(2,131101,'沧州市',130000),(3,131102,'廊坊市',130000),(4,131103,'西安市',140000),(5,131104,'成都市',150000),(6,131105,'重庆市',150000),(7,131106,'广州市',160000),(8,131107,'济南市',170000),(9,131108,'武汉市',180000),(10,131109,'郑州市',190000),(11,131110,'北京市',320000),(12,131111,'天津市',320000),(13,131112,'上海市',320000),(14,131113,'哈尔滨',320001),(15,131114,'雄安新区',320002);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scoretab`
--

DROP TABLE IF EXISTS `scoretab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `scoretab` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(15) DEFAULT NULL,
  `score` float(5,2) DEFAULT NULL,
  `number` bigint(20) DEFAULT NULL,
  `class` char(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scoretab`
--

LOCK TABLES `scoretab` WRITE;
/*!40000 ALTER TABLE `scoretab` DISABLE KEYS */;
INSERT INTO `scoretab` VALUES (1,'大空翼',98.50,13016880001,'AID1709'),(2,'松人',98.00,13016880002,'AID1709'),(3,'水冰月',98.00,13016880003,'AID1709'),(4,'星矢',97.50,13016880004,'AID1709'),(5,'紫龙',96.50,13016880005,'AID1709'),(6,'张飞',96.00,13016880006,'AID1709'),(7,'关羽',94.50,13016880007,'AID1709'),(8,'刘备',94.50,13016880008,'AID1709'),(9,'金花婆婆',94.00,13016880009,'AID1709'),(10,'紫衫龙王',93.00,13016880010,'AID1709'),(11,'青翼蝠王',92.50,13016880011,'AID1709'),(12,'白眉鹰王',92.50,13016880012,'AID1709'),(13,'金毛狮王',92.50,13016880013,'AID1709'),(14,'张三丰',92.00,13016880014,'AID1709'),(15,'张无忌',92.00,13016880015,'AID1709'),(16,'赵敏',91.50,13016880016,'AID1709'),(17,'小昭',91.50,13016880017,'AID1709'),(18,'周芷若',91.50,13016880018,'AID1709'),(19,'足球小将',91.00,13016880019,'AID1709'),(20,'圣斗士',90.50,13016880020,'AID1709'),(21,'黄金圣衣',90.00,13016880021,'AID1709'),(22,'胡亥',90.00,13016880022,'AID1709'),(23,'杨贵妃',89.00,13016880023,'AID1709'),(24,'叮当猫',88.50,13016880024,'AID1709'),(25,'吻别',88.50,13016880025,'AID1709'),(26,'抖音',87.50,13016880026,'AID1709'),(27,'火山',87.50,13016880027,'AID1709'),(28,'火箭',87.00,13016880028,'AID1709'),(29,'骑士',86.00,13016880029,'AID1709'),(30,'小可乐',85.00,13016880030,'AID1709'),(31,'小雪碧',83.50,13016880031,'AID1709'),(32,'美年达',82.50,13016880032,'AID1709'),(33,'小甜甜',81.00,13016880033,'AID1709'),(34,'欢欢',81.00,13016880034,'AID1709'),(35,'乐乐',81.00,13016880035,'AID1709'),(36,'秋秋',80.00,13016880036,'AID1709'),(37,'辉辉',79.50,13016880037,'AID1709'),(38,'军军',77.00,13016880038,'AID1709'),(39,'阳阳',74.50,13016880039,'AID1709'),(40,'白眉大侠',73.00,13016880040,'AID1709'),(41,'杨过',68.00,13016880041,'AID1709'),(42,'小龙女',66.00,13016880042,'AID1709'),(43,'郭襄',64.50,13016880043,'AID1709'),(44,'周芷若',60.00,13016880044,'AID1709'),(45,'神雕',60.00,13016880045,'AID1709'),(46,'战神',60.00,13016880046,'AID1709'),(47,'只手遮天',60.00,13016880047,'AID1709'),(48,'王者荣耀',60.00,13016880048,'AID1709');
/*!40000 ALTER TABLE `scoretab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheng`
--

DROP TABLE IF EXISTS `sheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sheng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) DEFAULT NULL,
  `s_name` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheng`
--

LOCK TABLES `sheng` WRITE;
/*!40000 ALTER TABLE `sheng` DISABLE KEYS */;
INSERT INTO `sheng` VALUES (1,130000,'河北省'),(2,140000,'陕西省'),(3,150000,'四川省'),(4,160000,'广东省'),(5,170000,'山东省'),(6,180000,'湖北省'),(7,190000,'河南省'),(8,200000,'海南省'),(9,200001,'云南省'),(10,200002,'山西省');
/*!40000 ALTER TABLE `sheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `userinfo` (
  `username` varchar(50) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  `UID` varchar(50) DEFAULT NULL,
  `des` varchar(50) DEFAULT NULL,
  `dir` varchar(50) DEFAULT NULL,
  `lm` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xian`
--

DROP TABLE IF EXISTS `xian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `xian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x_id` int(11) DEFAULT NULL,
  `x_name` varchar(15) DEFAULT NULL,
  `xfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xian`
--

LOCK TABLES `xian` WRITE;
/*!40000 ALTER TABLE `xian` DISABLE KEYS */;
INSERT INTO `xian` VALUES (1,132100,'正定县',131100),(2,132102,'浦东新区',131112),(3,132103,'武昌区',131108),(4,132104,'哈哈',131115),(5,132105,'安新县',131114),(6,132106,'容城县',131114),(7,132107,'雄县',131114),(8,132108,'嘎嘎',131115);
/*!40000 ALTER TABLE `xian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-28 11:48:46
