CREATE DATABASE  IF NOT EXISTS `dvdstore_new` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dvdstore_new`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dvdstore_new
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Account Number` int NOT NULL AUTO_INCREMENT,
  `First Name` varchar(50) NOT NULL,
  `Last name` varchar(45) NOT NULL,
  PRIMARY KEY (`Account Number`),
  UNIQUE KEY `Account Number_UNIQUE` (`Account Number`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Pamela','Foley'),(2,'Camilla','Dean'),(3,'Teddy','Hewitt'),(4,'Zachery','Wong'),(5,'Beatrix','Warren'),(6,'Adelaide','Robles'),(7,'Steve','Snow'),(8,'Frederick','Merrill'),(9,'Ffion','Velazquez'),(10,'Paula','Stanley'),(11,'Armaan','Greer'),(12,'Albert','Underwood');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dvdcopies`
--

DROP TABLE IF EXISTS `dvdcopies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dvdcopies` (
  `dvd id` int NOT NULL AUTO_INCREMENT,
  `Movie ID` int NOT NULL,
  PRIMARY KEY (`dvd id`),
  KEY `Movie ID_idx` (`Movie ID`),
  CONSTRAINT `Movie ID` FOREIGN KEY (`Movie ID`) REFERENCES `movie` (`Movie ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dvdcopies`
--

LOCK TABLES `dvdcopies` WRITE;
/*!40000 ALTER TABLE `dvdcopies` DISABLE KEYS */;
INSERT INTO `dvdcopies` VALUES (1,1),(2,2),(3,2),(4,2),(5,2),(6,3),(7,3),(8,4),(9,5),(10,5),(11,5),(12,5),(13,5),(14,6),(15,6),(16,6),(17,7),(18,8),(19,8),(20,8),(21,9),(22,9),(23,9),(24,9),(25,9),(26,10),(27,10),(28,10),(29,10);
/*!40000 ALTER TABLE `dvdcopies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movie name` varchar(250) NOT NULL,
  `Stars name` mediumtext NOT NULL,
  `Producer` varchar(50) NOT NULL,
  `Director` varchar(50) NOT NULL,
  `Production Company` varchar(50) NOT NULL,
  `Copies` int NOT NULL,
  `Movie ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Movie ID`),
  UNIQUE KEY `Movie ID_UNIQUE` (`Movie ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES ('The Way Way Back','Steve Carell,  Toni Collette, Maya Rudolph, Liam James','Kevin J. Walsh','Nat Faxon','Sycamore Pictures',1,1),('High School Musical','Zac Efron, Vanessa, Hudgens Ashley, Tisdale, Alyson Reed','Don Schain','Kenny Ortega','Salty Pictures',4,2),('Star Trek Beyond','Simon Pegg, Chris Pine, Zoe Saldana, Karl Urban, Anton Yelchi ','Justin Lin','Justin Lin','Paramount Pictures',2,3),('Cloud Atlas','Tom Hanks, Halle Berry, Jim Broadbent, Hugo Weaving','Grant Hill','Lana Wachowski','X Filme Creative Pool',2,4),('The Grand Budapest Hotel','Ralph Fiennes, F. Murray, Abraham, Mathieu Amalric, Adrien Brody','Wes Anderson','Wes Anderson','Fox Searchlight Pictures',5,5),('Jojo Rabbit','Roman Griffin, Davis Thomasin McKenzie, Taika Waititi','Carthew Neal','Taika Waititi','Fox Searchlight Pictures',3,6),('Stargate','Kurt Russel, James Spader','Joel B. Michaels','Roland Emmerich','Centropolis Film',1,7),('The Shawshank Redemption','Tim Robbins,Morgan Freeman,Bob Gunton','Niki Marvin','Frank Darabont','Castle Rock Entertainment',3,8),('Alien','Tom Skerritt, Sigourney Weaver, Veronica Cartwright','Gordon Carroll','Ridley Scott','20th Century Fox',5,9),('WALL-E','Ben Burtt,Elissa Knight','Jim Morris','Andrew Stanton','Walt Disney Pictures',4,10);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pasttransactions`
--

DROP TABLE IF EXISTS `pasttransactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pasttransactions` (
  `transaction id` int NOT NULL,
  `Account` int NOT NULL,
  `dvd id` int DEFAULT NULL,
  `checkout date` date DEFAULT NULL,
  `checkin date` date DEFAULT NULL,
  PRIMARY KEY (`transaction id`),
  KEY `Account Number_idx` (`Account`),
  CONSTRAINT `account` FOREIGN KEY (`Account`) REFERENCES `customer` (`Account Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pasttransactions`
--

LOCK TABLES `pasttransactions` WRITE;
/*!40000 ALTER TABLE `pasttransactions` DISABLE KEYS */;
INSERT INTO `pasttransactions` VALUES (3,3,2,'2023-02-17','2023-02-17'),(6,8,4,'2023-02-11','2023-02-17'),(10,9,16,'2023-02-01','2023-02-11'),(11,10,27,'2023-02-16','2023-02-19'),(15,12,3,'2023-01-29','2023-02-17'),(20,8,29,'2023-01-20','2023-02-13'),(21,4,28,'2023-01-19','2023-02-16'),(45,1,5,'2023-02-11','2023-02-11'),(49,1,25,'2023-02-13','2023-02-19'),(50,3,20,'2023-02-13','2023-02-16'),(67,1,29,'2023-02-19','2023-02-19'),(68,3,25,'2023-02-19','2023-02-19');
/*!40000 ALTER TABLE `pasttransactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rented`
--

DROP TABLE IF EXISTS `rented`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rented` (
  `rental id` int NOT NULL AUTO_INCREMENT,
  `Account Number` int NOT NULL,
  `dvd id` int NOT NULL,
  `checkout date` date DEFAULT NULL,
  PRIMARY KEY (`rental id`),
  UNIQUE KEY `rental id_UNIQUE` (`rental id`),
  KEY `Account Number_idx` (`Account Number`),
  KEY `dvd id_idx` (`dvd id`),
  CONSTRAINT `Account Number` FOREIGN KEY (`Account Number`) REFERENCES `customer` (`Account Number`),
  CONSTRAINT `dvd id` FOREIGN KEY (`dvd id`) REFERENCES `dvdcopies` (`dvd id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rented`
--

LOCK TABLES `rented` WRITE;
/*!40000 ALTER TABLE `rented` DISABLE KEYS */;
INSERT INTO `rented` VALUES (5,5,23,'2023-02-09'),(14,12,6,'2023-02-03'),(46,9,8,'2023-02-13'),(51,5,12,'2023-02-13'),(52,1,11,'2023-02-13'),(53,1,15,'2023-02-13'),(54,3,16,'2023-02-13'),(55,7,17,'2023-02-15'),(58,6,18,'2023-02-15'),(59,3,10,'2023-02-16'),(60,10,4,'2023-02-17');
/*!40000 ALTER TABLE `rented` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-19 18:14:53
