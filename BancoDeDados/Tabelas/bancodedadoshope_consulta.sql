CREATE DATABASE  IF NOT EXISTS `bancodedadoshope` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bancodedadoshope`;

DROP TABLE IF EXISTS `consulta`;

CREATE TABLE `consulta` (
  `consultaID` int NOT NULL AUTO_INCREMENT,
  `pacienteID` int DEFAULT NULL,
  `psicologoID` int DEFAULT NULL,
  `dataHoraConsulta` datetime DEFAULT NULL,
  PRIMARY KEY (`consultaID`),
  KEY `psicologoID` (`psicologoID`),
  KEY `pacienteID` (`pacienteID`),
  CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`psicologoID`) REFERENCES `psicologos` (`psicologoID`),
  CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`pacienteID`) REFERENCES `pacientes` (`pacienteID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;