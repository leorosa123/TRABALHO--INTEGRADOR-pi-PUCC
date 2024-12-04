

CREATE DATABASE  IF NOT EXISTS `bancodedadoshope` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bancodedadoshope`;

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `cadastroID` int NOT NULL AUTO_INCREMENT,
  `userID` int DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `senha` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cadastroID`),
  KEY `userID` (`userID`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `pacientes` (`pacienteID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
