

CREATE DATABASE  IF NOT EXISTS `bancodedadoshope` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bancodedadoshope`;

DROP TABLE IF EXISTS `psicologos`;

CREATE TABLE `psicologos` (
  `psicologoID` int NOT NULL AUTO_INCREMENT,
  `nomePsicologo` varchar(60) NOT NULL,
  `dataNascPsicologo` date DEFAULT NULL,
  `psicologoCPF` varchar(15) DEFAULT NULL,
  `CRP` varchar(15) NOT NULL,
  `especialidade` varchar(30) NOT NULL,
  `descricao` varchar(150) DEFAULT NULL,
  `fotoPsicologo` blob NOT NULL,
  `horarioDeAtendimento` varchar(8) NOT NULL,
  PRIMARY KEY (`psicologoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

