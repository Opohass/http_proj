CREATE DATABASE `flask_proj`;
USE `flask_proj`;
CREATE TABLE IF NOT EXISTS `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) NOT NULL,
  `passwordHash` varchar(4500) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `userName_UNIQUE` (`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `models` (
  `model_id` INT NOT NULL AUTO_INCREMENT,
  `model_name` VARCHAR(45) NOT NULL,
  `pickle` VARBINARY(3072) NOT NULL,
  PRIMARY KEY (`model_id`),
  UNIQUE INDEX `model_name_UNIQUE` (`model_name` ASC) VISIBLE,
  UNIQUE INDEX `model_id_UNIQUE` (`model_id` ASC) VISIBLE,
  UNIQUE INDEX `pickle_UNIQUE` (`pickle` ASC) VISIBLE);
LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'admin','admin');
UNLOCK TABLES;

