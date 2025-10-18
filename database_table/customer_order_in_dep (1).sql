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
-- Table structure for table `customer_order_in_dep`
--

CREATE TABLE `customer_order_in_dep` (
  `id` int(255) NOT NULL,
  `rep_id` varchar(255) NOT NULL,
  `pro_id` varchar(255) NOT NULL,
  `dep_id` varchar(255) NOT NULL,
  `art_id` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL,
  `new_id` int(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `emp_id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `clear_date` date DEFAULT NULL,
  `clear_time` varchar(255) NOT NULL,
  `clear_user` varchar(255) NOT NULL,
  `voucher` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_in_dep`
--

INSERT INTO `customer_order_in_dep` (`id`, `rep_id`, `pro_id`, `dep_id`, `art_id`, `qty`, `new_id`, `user`, `emp_id`, `date`, `time`, `comments`, `status`, `clear_date`, `clear_time`, `clear_user`, `voucher`) VALUES
(1, '1-1-1', '1-5', 'DEP-26', '1-1', 10, 1, '6', 'EMP-75', '2023-08-04', '06:11 AM', '1-10', 1, '2023-08-28', '03:40 PM', '1', ''),
(2, '1-1-2', '1-5', 'DEP-26', '1-1', 10, 2, '6', 'EMP-118', '2023-08-04', '06:11 AM', '1-10', 0, NULL, '', '', ''),
(3, '1-2-1', '1-5', 'DEP-26', '1-2', 5, 1, '6', 'EMP-75', '2023-08-04', '06:13 AM', '', 0, NULL, '', '', ''),
(4, '1-2-2', '1-5', 'DEP-26', '1-2', 5, 2, '6', 'EMP-75', '2023-08-04', '06:13 AM', '', 0, NULL, '', '', ''),
(5, '1-3-1', '1-5', 'DEP-26', '1-3', 30, 1, '6', 'EMP-118', '2023-08-04', '06:13 AM', '', 0, NULL, '', '', ''),
(6, '1-3-2', '1-5', 'DEP-26', '1-3', 6, 2, '6', 'EMP-75', '2023-08-04', '06:13 AM', '', 0, NULL, '', '', ''),
(7, '1-4-1', '1-5', 'DEP-26', '1-4', 10, 1, '6', 'EMP-75', '2023-08-06', '05:07 AM', '', 0, NULL, '', '', ''),
(8, '1-5-1', '1-9', 'DEP-26', '1-5', 5, 1, '6', 'EMP-285', '2023-08-06', '05:08 AM', '', 0, NULL, '', '', ''),
(9, '1-5-2', '1-5', 'DEP-26', '1-5', 5, 2, '6', 'EMP-75', '2023-08-06', '05:08 AM', '', 0, NULL, '', '', ''),
(10, '1-4-2', '1-9', 'DEP-26', '1-4', 5, 2, '6', 'EMP-285', '2023-08-06', '05:10 AM', '', 0, NULL, '', '', ''),
(11, '1-7-1', '1-9', 'DEP-26', '1-7', 2, 1, '6', 'EMP-285', '2023-08-06', '05:11 AM', '', 0, NULL, '', '', ''),
(12, '1-7-2', '1-9', 'DEP-26', '1-7', 2, 2, '6', 'EMP-75', '2023-08-06', '05:11 AM', '', 0, NULL, '', '', ''),
(13, '1-7-3', '1-9', 'DEP-26', '1-7', 1, 3, '6', 'EMP-285', '2023-08-06', '05:11 AM', '', 0, NULL, '', '', ''),
(15, '1-1-4', '1-4', 'DEP-28', '1-1', 5, 4, '6', 'EMP-157', '2023-08-07', '03:21 PM', '1 to 5', 0, NULL, '', '', ''),
(16, '1-1-5', '1-4', 'DEP-28', '1-1', 5, 5, '6', 'EMP-159', '2023-08-07', '03:21 PM', '1 to 5', 0, NULL, '', '', ''),
(17, '1-1-6', '1-4', 'DEP-28', '1-1', 5, 6, '6', 'EMP-158', '2023-08-07', '03:22 PM', '1 to 5', 0, NULL, '', '', ''),
(18, '1-1-7', '1-4', 'DEP-28', '1-1', 5, 7, '6', 'EMP-156', '2023-08-07', '03:22 PM', '1 to 5', 0, NULL, '', '', ''),
(19, '2-1-1', '2-1', 'DEP-1', '2-1', 25, 1, '6', 'EMP-73', '2023-09-04', '09:01 PM', '1-25', 0, NULL, '', '', ''),
(20, '2-1-2', '2-1', 'DEP-1', '2-1', 25, 2, '6', 'EMP-75', '2023-09-04', '09:01 PM', '1-25', 0, NULL, '', '', ''),
(21, '2-2-1', '2-1', 'DEP-1', '2-2', 30, 1, '6', 'EMP-98', '2023-09-04', '09:01 PM', '', 0, NULL, '', '', ''),
(22, '2-2-2', '2-1', 'DEP-1', '2-2', 20, 2, '6', 'EMP-73', '2023-09-04', '09:02 PM', '', 0, NULL, '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_in_dep`
--
ALTER TABLE `customer_order_in_dep`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rep_id` (`rep_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_in_dep`
--
ALTER TABLE `customer_order_in_dep`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
