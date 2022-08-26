CREATE DATABASE `flask_proj`;
USE `flask_proj`;
CREATE TABLE IF NOT EXISTS `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) NOT NULL,
  `passwordHash` varchar(45) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `userName_UNIQUE` (`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'admin','admin');
UNLOCK TABLES;