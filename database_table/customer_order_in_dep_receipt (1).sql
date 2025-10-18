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
-- Table structure for table `customer_order_in_dep_receipt`
--

CREATE TABLE `customer_order_in_dep_receipt` (
  `id` int(255) NOT NULL,
  `req_id` varchar(255) NOT NULL,
  `sub_pro` varchar(255) NOT NULL,
  `emp_id` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL,
  `new_id` int(255) NOT NULL,
  `sub_req_id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_in_dep_receipt`
--

INSERT INTO `customer_order_in_dep_receipt` (`id`, `req_id`, `sub_pro`, `emp_id`, `qty`, `new_id`, `sub_req_id`, `date`, `time`, `user`, `comments`, `status`) VALUES
(1, '1-1-4', '1-4-1', 'EMP-1', 5, 1, '1-1-4-1', '2023-08-29', '03:23 PM', '6', '', 0),
(2, '1-1-4', '1-4-2', 'EMP-2', 3, 2, '1-1-4-2', '2023-08-29', '03:24 PM', '6', '', 0),
(3, '1-1-4', '1-4-2', 'EMP-4', 2, 3, '1-1-4-3', '2023-08-29', '03:24 PM', '6', '', 0),
(4, '1-1-5', '1-4-1', 'EMP-5', 5, 1, '1-1-5-1', '2023-08-29', '06:58 PM', '6', '', 0),
(5, '1-1-5', '1-4-2', 'EMP-5', 5, 2, '1-1-5-2', '2023-08-29', '06:58 PM', '6', '', 0),
(6, '1-1-6', '1-4-1', 'EMP-6', 5, 1, '1-1-6-1', '2023-08-29', '07:37 PM', '6', '', 0),
(7, '1-1-6', '1-4-2', 'EMP-3', 5, 2, '1-1-6-2', '2023-08-29', '07:37 PM', '6', '', 0),
(8, '2-1-1', '2-1-1', 'EMP-3', 25, 1, '2-1-1-1', '2023-09-04', '09:03 PM', '6', '', 0),
(9, '2-1-1', '2-1-2', 'EMP-3', 25, 2, '2-1-1-2', '2023-09-04', '09:03 PM', '6', '', 0),
(10, '2-1-1', '2-1-3', 'EMP-3', 25, 3, '2-1-1-3', '2023-09-04', '09:03 PM', '6', '', 0),
(11, '2-1-1', '2-1-4', 'EMP-3', 20, 4, '2-1-1-4', '2023-09-04', '09:03 PM', '6', '', 0),
(12, '2-1-1', '2-1-4', 'EMP-2', 5, 5, '2-1-1-5', '2023-09-04', '09:03 PM', '6', '', 0),
(13, '2-1-1', '2-1-5', 'EMP-1', 15, 6, '2-1-1-6', '2023-09-04', '09:03 PM', '6', '', 0),
(14, '2-1-1', '2-1-5', 'EMP-2', 10, 7, '2-1-1-7', '2023-09-04', '09:03 PM', '6', '', 0),
(15, '2-2-1', '2-1-1', 'EMP-5', 30, 1, '2-2-1-1', '2023-09-04', '09:09 PM', '6', '', 0),
(16, '2-2-1', '2-1-2', 'EMP-5', 15, 2, '2-2-1-2', '2023-09-04', '09:09 PM', '6', '', 0),
(17, '2-2-1', '2-1-3', 'EMP-4', 30, 3, '2-2-1-3', '2023-09-04', '09:09 PM', '6', '', 0),
(18, '2-2-1', '2-1-2', 'EMP-6', 15, 4, '2-2-1-4', '2023-09-04', '09:09 PM', '6', '', 0),
(19, '2-2-1', '2-1-4', 'EMP-6', 30, 5, '2-2-1-5', '2023-09-04', '09:10 PM', '6', '', 0),
(20, '2-2-1', '2-1-5', 'EMP-6', 30, 6, '2-2-1-6', '2023-09-04', '09:10 PM', '6', '', 0),
(21, '2-1-2', '2-1-1', 'EMP-3', 25, 1, '2-1-2-1', '2023-09-05', '07:11 PM', '6', '', 0),
(22, '2-1-2', '2-1-2', 'EMP-1', 25, 2, '2-1-2-2', '2023-09-05', '07:11 PM', '6', '', 0),
(23, '2-1-2', '2-1-3', 'EMP-5', 25, 3, '2-1-2-3', '2023-09-05', '07:11 PM', '6', '', 0),
(24, '2-1-2', '2-1-4', 'EMP-1', 25, 4, '2-1-2-4', '2023-09-05', '07:11 PM', '6', '', 0),
(25, '2-1-2', '2-1-5', 'EMP-1', 25, 5, '2-1-2-5', '2023-09-05', '07:12 PM', '6', '', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_in_dep_receipt`
--
ALTER TABLE `customer_order_in_dep_receipt`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sub_req_id` (`sub_req_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_in_dep_receipt`
--
ALTER TABLE `customer_order_in_dep_receipt`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
