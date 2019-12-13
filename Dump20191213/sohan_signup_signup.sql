-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: sohan
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `signup_signup`
--

DROP TABLE IF EXISTS `signup_signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `signup_signup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suser` varchar(50) NOT NULL,
  `semail` varchar(50) NOT NULL,
  `spassword` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup_signup`
--

LOCK TABLES `signup_signup` WRITE;
/*!40000 ALTER TABLE `signup_signup` DISABLE KEYS */;
INSERT INTO `signup_signup` VALUES (1,'Sohan','sd123@gmail.com','sohan'),(2,'Gautam ','gautham123@gmail.com',''),(4,'computer','computer123@gmail.com','python'),(5,'keerthi','keerthi123@gmail.com','frog'),(6,'keerthi2','keerthi2@gmail.com','computer'),(7,'smitha','sfasndf@asdf','smitha'),(8,'test','test@asdf','test'),(10,'test7','test7@sdf','test7'),(11,'test8','sd123@gmail.com','test8'),(12,'test9','sd123@gmail.com','test9'),(13,'test10','test12@adsf','test10'),(14,'test11','test12@adsf','test11'),(15,'Happy','happy123@gmail.com','happy'),(16,'keerthi','keerthi12@gmail.com','sik123'),(17,'sad1','sad123@gmail.com','sad'),(18,'Anish','anish123@gmail.com','12345'),(19,'sefsef','awfawef@asd.com','123'),(23,'Kohli','kohli@gmail.com','hello'),(26,'Addy','theo@gmail.com','qwerty'),(27,'table1','table@gmail.com','table'),(28,'nidhi','nidhi@gmail.com','nidhi123'),(29,'table12','t@gm','table'),(30,'Advaita','theoriginalteamavatar@gmail.com','Addy'),(32,'smithar','smitha@ravindran.kumarans.org','smithar'),(33,'anish','anish1234@asn.com','qwert'),(34,'angry','angry12@gmail.com','angry'),(35,'angry1','angry12@gmail.com','qaz'),(36,'angry1','angry12@gmail.com','qaz'),(37,'angry','angry12@gmail.com','happy'),(38,'angry234','angry123@gmail.com','sappy');
/*!40000 ALTER TABLE `signup_signup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-13 13:01:45
