-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 15, 2020 at 02:13 PM
-- Server version: 5.7.30
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `breizhibus`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `country_hos` (IN `con` CHAR(20))  BEGIN
SELECT Name, HeadOfState
FROM Country
WHERE Continent = con;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `arrets`
--

CREATE TABLE `arrets` (
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL,
  `id_arret` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets`
--

INSERT INTO `arrets` (`nom`, `adresse`, `id_arret`) VALUES
('Korrigan', '1 impasse du Korrigan', 19),
('Morgana', '2 plage Morgana', 20),
('L\'Ankou', '3 place du L\'Ankou', 21),
('Ys', '4 rue de l\'ile d\'Ys', 22),
('Viviane', '5 avenu de Viviane', 23),
('Guénolé', '6 rue Saint Guénolé', 24);

-- --------------------------------------------------------

--
-- Table structure for table `arrets_lignes`
--

CREATE TABLE `arrets_lignes` (
  `id_ligne` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets_lignes`
--

INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`) VALUES
(1, 19),
(1, 20),
(3, 21),
(2, 20),
(2, 22),
(2, 23),
(3, 22),
(3, 23),
(3, 24),
(3, 19),
(4, 19),
(4, 21),
(4, 23);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numeros` varchar(4) NOT NULL,
  `immatriculation` varchar(50) DEFAULT NULL,
  `nombre_place` int(11) DEFAULT NULL,
  `id_ligne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numeros`, `immatriculation`, `nombre_place`, `id_ligne`) VALUES
(1, 'BB01', 'AA', 20, 1),
(2, 'BB02', 'NO 123 EL', 30, 2),
(3, 'BB03', 'JE 123 UX', 20, 3),
(4, 'BB04', 'RE 123 PA', 30, 1),
(5, 'BB05', 'PU 123 ZZ', 20, 4);

-- --------------------------------------------------------

--
-- Table structure for table `lignes`
--

CREATE TABLE `lignes` (
  `id_ligne` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lignes`
--

INSERT INTO `lignes` (`id_ligne`, `nom`) VALUES
(1, 'Rouge'),
(2, 'Vert'),
(3, 'Bleu'),
(4, 'Noir');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`id_arret`);

--
-- Indexes for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD KEY `arrets_lignes_ibfk_1` (`id_ligne`),
  ADD KEY `id_arret` (`id_arret`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Indexes for table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`id_ligne`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `id_ligne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD CONSTRAINT `arrets_lignes_ibfk_1` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`),
  ADD CONSTRAINT `arrets_lignes_ibfk_2` FOREIGN KEY (`id_arret`) REFERENCES `arrets` (`id_arret`);

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);
