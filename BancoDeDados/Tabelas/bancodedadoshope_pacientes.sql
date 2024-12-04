

CREATE DATABASE  IF NOT EXISTS `bancodedadoshope` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bancodedadoshope`;
DROP TABLE IF EXISTS `pacientes`;

CREATE TABLE `pacientes` (
  `pacienteID` int NOT NULL AUTO_INCREMENT,
  `nomePaciente` varchar(60) NOT NULL,
  `dataNascPaciente` date DEFAULT NULL,
  `pacienteCPF` varchar(15) NOT NULL,
  `fotoPaciente` blob,
  PRIMARY KEY (`pacienteID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
