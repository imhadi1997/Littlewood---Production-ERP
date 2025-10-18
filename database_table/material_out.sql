-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2023 at 02:51 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `new_littlewood`
--

-- --------------------------------------------------------

--
-- Table structure for table `material_out`
--

CREATE TABLE `material_out` (
  `id` int(255) NOT NULL,
  `art_id` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `req_id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `qty` float NOT NULL,
  `type` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `user` int(255) NOT NULL,
  `order_id` varchar(255) NOT NULL,
  `balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `material_out`
--

INSERT INTO `material_out` (`id`, `art_id`, `amount`, `req_id`, `date`, `time`, `qty`, `type`, `category`, `user`, `order_id`, `balance`) VALUES
(1, '2-25-1', 0, '1-1-4', '2023-09-08', '07:04 PM', 120, 'Receipt', 'Credit', 2, '1', 3174.42),
(2, '2-22-6', 0, '1-1-4', '2023-09-08', '07:39 PM', 124.68, 'Receipt', 'Credit', 2, '1', 2252.35);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `material_out`
--
ALTER TABLE `material_out`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `material_out`
--
ALTER TABLE `material_out`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
