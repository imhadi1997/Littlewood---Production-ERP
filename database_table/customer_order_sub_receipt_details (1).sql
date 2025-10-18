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
-- Table structure for table `customer_order_sub_receipt_details`
--

CREATE TABLE `customer_order_sub_receipt_details` (
  `id` int(255) NOT NULL,
  `sub_req` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `rate` int(255) NOT NULL,
  `voucher` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_sub_receipt_details`
--

INSERT INTO `customer_order_sub_receipt_details` (`id`, `sub_req`, `qty`, `date`, `time`, `user`, `status`, `rate`, `voucher`) VALUES
(1, '1-1-4-1', 2, '2023-08-29', '05:42 PM', '6', 0, 0, ''),
(2, '1-1-4-1', 2, '2023-08-29', '05:43 PM', '6', 0, 0, ''),
(3, '1-1-4-1', 1, '2023-08-29', '05:43 PM', '6', 0, 0, ''),
(4, '1-1-4-2', 2, '2023-08-29', '05:43 PM', '6', 0, 0, ''),
(5, '1-1-4-2', 1, '2023-08-29', '05:43 PM', '6', 0, 0, ''),
(6, '1-1-4-3', 2, '2023-08-29', '05:43 PM', '6', 0, 0, ''),
(7, '1-1-5-1', 5, '2023-08-29', '06:58 PM', '6', 0, 0, ''),
(8, '1-1-6-1', 4, '2023-08-29', '07:37 PM', '6', 0, 0, ''),
(9, '1-1-6-2', 3, '2023-08-29', '07:37 PM', '6', 0, 0, ''),
(10, '2-1-1-1', 20, '2023-09-04', '09:05 PM', '6', 0, 0, ''),
(11, '2-1-1-1', 5, '2023-09-04', '09:05 PM', '6', 0, 0, ''),
(12, '2-1-1-2', 25, '2023-09-04', '09:05 PM', '6', 0, 0, ''),
(13, '2-1-1-3', 15, '2023-09-04', '09:05 PM', '6', 0, 0, ''),
(14, '2-1-1-3', 10, '2023-09-04', '09:05 PM', '6', 0, 0, ''),
(15, '2-1-1-4', 20, '2023-09-04', '09:06 PM', '6', 0, 0, ''),
(16, '2-1-1-5', 5, '2023-09-04', '09:06 PM', '6', 0, 0, ''),
(17, '2-1-1-6', 10, '2023-09-04', '09:06 PM', '6', 0, 0, ''),
(18, '2-1-1-6', 5, '2023-09-04', '09:06 PM', '6', 0, 0, ''),
(19, '2-1-1-7', 10, '2023-09-04', '09:06 PM', '6', 0, 0, ''),
(20, '2-2-1-1', 30, '2023-09-04', '09:10 PM', '6', 0, 0, ''),
(21, '2-1-2-1', 1, '2023-09-05', '07:12 PM', '6', 0, 0, ''),
(22, '2-1-2-2', 1, '2023-09-05', '07:12 PM', '6', 0, 0, ''),
(23, '2-1-2-3', 1, '2023-09-05', '07:12 PM', '6', 0, 0, ''),
(24, '2-1-2-4', 1, '2023-09-05', '07:12 PM', '6', 0, 0, ''),
(25, '2-1-2-5', 1, '2023-09-05', '07:12 PM', '6', 0, 0, ''),
(26, '2-1-2-1', 1, '2023-09-05', '07:13 PM', '6', 0, 0, ''),
(27, '2-1-2-4', 1, '2023-09-05', '07:13 PM', '6', 0, 0, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_sub_receipt_details`
--
ALTER TABLE `customer_order_sub_receipt_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_sub_receipt_details`
--
ALTER TABLE `customer_order_sub_receipt_details`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
