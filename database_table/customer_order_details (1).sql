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
-- Table structure for table `customer_order_details`
--

CREATE TABLE `customer_order_details` (
  `id` int(255) NOT NULL,
  `art_id` varchar(255) NOT NULL,
  `factory_po` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `size` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL,
  `new_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order_details`
--

INSERT INTO `customer_order_details` (`id`, `art_id`, `factory_po`, `details`, `size`, `color`, `qty`, `new_id`) VALUES
(1, '1-1', '1', '113580-50', '50', 'Black/light gray', 20, 1),
(2, '1-2', '1', '113580-52', '52', 'Black/light gray', 10, 2),
(3, '1-3', '1', '113580-54', '54', 'Black/light gray', 36, 3),
(4, '1-4', '1', '113580-56', '56', 'Black/light gray', 15, 4),
(5, '1-5', '1', '113580-58', '58', 'Black/light gray', 10, 5),
(6, '1-6', '1', '113580-60', '60', 'Black/light gray', 30, 6),
(7, '1-7', '1', '113580-64', '64', 'Black/light gray', 5, 7),
(8, '2-1', '2', '105656-38', '38', 'Pink/white', 50, 1),
(9, '2-2', '2', '105656-40', '40', 'Yellow/blue', 50, 2),
(10, '3-1', '3', '5611-52', '52', 'Black / white', 50, 1),
(11, '3-2', '3', '5611-54', '54', 'Blacl / white', 50, 2),
(12, '3-3', '3', '5611-56', '56', 'Black / white', 50, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_order_details`
--
ALTER TABLE `customer_order_details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `art_id` (`art_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_order_details`
--
ALTER TABLE `customer_order_details`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
