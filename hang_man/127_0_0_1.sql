-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2021 at 05:15 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hang_man`
--
CREATE DATABASE IF NOT EXISTS `hang_man` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `hang_man`;

-- --------------------------------------------------------

--
-- Table structure for table `player_data`
--

CREATE TABLE `player_data` (
  `player_name` varchar(30) NOT NULL,
  `play_date` date DEFAULT NULL,
  `play_time` time DEFAULT NULL,
  `word` varchar(20) DEFAULT NULL,
  `turns_provided` int(2) DEFAULT NULL,
  `turns_used` int(2) DEFAULT NULL,
  `status` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `player_data`
--

INSERT INTO `player_data` (`player_name`, `play_date`, `play_time`, `word`, `turns_provided`, `turns_used`, `status`) VALUES
('sandeep', '2021-12-15', '05:32:41', 'speaker', 7, 0, 'WON'),
('sandeep', '2021-12-15', '05:33:09', 'laptop', 6, 6, 'LOST'),
('sandeep', '2021-12-15', '05:37:56', 'pencil', 6, 6, 'LOST'),
('daham', '2021-12-15', '05:49:17', 'lorry', 5, 0, 'WON'),
('daham', '2021-12-15', '05:54:03', 'eraser', 6, 0, 'WON'),
('jason', '2021-12-15', '06:13:16', 'calender', 8, 1, 'WON'),
('jason', '2021-12-15', '06:13:29', 'information', 11, 3, 'WON'),
('sandeep', '2021-12-15', '06:14:05', 'eraser', 6, 0, 'WON'),
('sandeep', '2021-12-15', '06:14:14', 'mouse', 5, 5, 'LOST'),
('sandeep', '2021-12-15', '06:14:47', 'apple', 5, 0, 'WON'),
('sandeep', '2021-12-15', '06:14:58', 'stethoscope', 11, 2, 'WON'),
('sandeep', '2021-12-15', '06:15:08', 'calender', 8, 4, 'WON'),
('sandeep', '2021-12-15', '06:15:18', 'speaker', 7, 0, 'WON'),
('sandeep', '2021-12-15', '06:15:26', 'tomato', 6, 1, 'WON'),
('sandeep', '2021-12-15', '06:15:57', 'computer', 8, 0, 'WON'),
('sandeep', '2021-12-15', '06:16:07', 'monkey', 6, 6, 'LOST'),
('sandeep', '2021-12-15', '06:45:14', 'speaker', 7, 0, 'WON'),
('daham', '2021-12-15', '06:49:18', 'electricity', 11, 0, 'WON'),
('jason', '2021-12-15', '06:51:22', 'lorry', 5, 5, 'LOST');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
