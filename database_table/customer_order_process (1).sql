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
-- Table structure for table `customer_order_process`
--

CREATE TABLE `customer_order_process` (
  `id` int(255) NOT NULL,
  `sub_pro_id` varchar(255) NOT NULL,
  `pro_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `new_id` int(255) NOT NULL,
  `rate` int(255) NOT NULL,
  `start_process` varchar(255) NOT NULL,
  `end_process` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_process`
--

INSERT INTO `customer_order_process` (`id`, `sub_pro_id`, `pro_id`, `name`, `new_id`, `rate`, `start_process`, `end_process`) VALUES
(1, '1-1-1', '1-1', 'Body cutting', 1, 35, '', ''),
(2, '1-1-2', '1-1', 'Lining cutting', 2, 25, '', ''),
(3, '1-2-1', '1-2', 'Printing marking', 1, 26, '', ''),
(4, '1-2-2', '1-2', 'Body marking', 2, 60, '', ''),
(5, '1-2-3', '1-2', 'Lining marking', 3, 20, '', ''),
(6, '1-3-1', '1-3', 'Sealing', 1, 25, '', ''),
(7, '1-3-2', '1-3', 'Bartake', 2, 36, '', ''),
(8, '1-4-1', '1-4', 'Astar', 1, 300, '', ''),
(9, '1-4-2', '1-4', 'Koti', 2, 75, '', ''),
(10, '1-5-1', '1-5', 'Arm', 1, 240, '', ''),
(11, '1-5-2', '1-5', 'Front', 2, 500, '', ''),
(12, '1-5-3', '1-5', 'Back', 3, 90, '', ''),
(13, '1-5-4', '1-5', 'Side', 4, 125, '', ''),
(14, '1-5-5', '1-5', 'Final prepration', 5, 145, '', ''),
(15, '1-6-1', '1-6', 'Heat transfer', 1, 130, '', ''),
(16, '1-6-2', '1-6', 'Embroidery', 2, 65, '', ''),
(17, '1-6-3', '1-6', 'Printing', 3, 70, '', ''),
(18, '1-7-1', '1-7', 'Palloy', 1, 18, '', ''),
(19, '1-8-1', '1-8', 'Article cleaning', 1, 35, '', ''),
(20, '1-9-1', '1-9', 'Complete pc', 1, 1100, '', ''),
(21, '1-9-2', '1-9', 'Makeri', 2, 400, '', ''),
(22, '2-1-1', '2-1', 'Arm', 1, 240, '', ''),
(23, '2-1-2', '2-1', 'Front', 2, 500, '', ''),
(24, '2-1-3', '2-1', 'Back', 3, 90, '', ''),
(25, '2-1-4', '2-1', 'Side', 4, 125, '', ''),
(26, '2-1-5', '2-1', 'Final prepration', 5, 145, '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_process`
--
ALTER TABLE `customer_order_process`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pro_id` (`sub_pro_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_process`
--
ALTER TABLE `customer_order_process`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
