-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2023 at 02:50 PM
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
-- Table structure for table `customer_order_rate`
--

CREATE TABLE `customer_order_rate` (
  `id` int(255) NOT NULL,
  `pro_no` varchar(255) NOT NULL,
  `order_id` int(255) NOT NULL,
  `dep_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `new_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_rate`
--

INSERT INTO `customer_order_rate` (`id`, `pro_no`, `order_id`, `dep_id`, `name`, `user`, `new_id`) VALUES
(1, '1-1', 1, 'DEP-29', 'Cutting(body/lining)', '1', 1),
(2, '1-2', 1, 'DEP-27', 'All marking', '1', 2),
(3, '1-3', 1, 'DEP-23', 'Bartake/sealing', '1', 3),
(4, '1-4', 1, 'DEP-28', 'Astar/koti', '1', 4),
(5, '1-5', 1, 'DEP-26', 'Body stitching', '1', 5),
(6, '1-6', 1, 'DEP-7', 'Printing', '1', 6),
(7, '1-7', 1, 'DEP-17', 'Palloy', '1', 7),
(8, '1-8', 1, 'DEP-4', 'Finishing', '1', 8),
(9, '1-9', 1, 'DEP-26', 'Stitching(out source)', '1', 9),
(10, '2-1', 2, 'DEP-1', 'Stitching - in house', '1', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_rate`
--
ALTER TABLE `customer_order_rate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pro_no` (`pro_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_rate`
--
ALTER TABLE `customer_order_rate`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
