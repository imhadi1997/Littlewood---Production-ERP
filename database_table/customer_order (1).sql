-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2023 at 02:49 PM
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
-- Table structure for table `customer_order`
--

CREATE TABLE `customer_order` (
  `id` int(255) NOT NULL,
  `factory_po` varchar(255) NOT NULL,
  `customer_po` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `added_date` date NOT NULL,
  `added_time` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `clear_date` date NOT NULL,
  `clear_time` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`id`, `factory_po`, `customer_po`, `name`, `qty`, `type`, `added_date`, `added_time`, `status`, `clear_date`, `clear_time`, `user`) VALUES
(1, 'Lw-01-23', '611897', 'Murano mens textile jacket', 126, 'Textile', '2023-06-07', '03:27 PM', 0, '0000-00-00', '', '1'),
(2, 'Lw-02-23', '611897', 'Murano ladies textile jacket', 100, 'Textile', '2023-06-07', '03:30 PM', 0, '0000-00-00', '', '1'),
(3, 'Lw-03-23', '611898', 'Difi leather 2pc', 150, 'Leather', '2023-09-16', '04:26 PM', 0, '0000-00-00', '', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order`
--
ALTER TABLE `customer_order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `factory_po` (`factory_po`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order`
--
ALTER TABLE `customer_order`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
