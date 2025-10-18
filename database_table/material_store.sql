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
-- Table structure for table `material_store`
--

CREATE TABLE `material_store` (
  `id` int(255) NOT NULL,
  `store_id` varchar(255) NOT NULL,
  `mat_id` varchar(255) NOT NULL,
  `art_id` varchar(255) NOT NULL,
  `qty` float NOT NULL,
  `details` varchar(255) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `material_store`
--

INSERT INTO `material_store` (`id`, `store_id`, `mat_id`, `art_id`, `qty`, `details`, `price`) VALUES
(1, '2', '2-9', '2-9-1', 44.58, 'Room #1 rack # 6', 0),
(2, '2', '2-15', '2-15-1', 909.75, 'Room# 1 rack # 3', 0),
(7, '2', '2-25', '2-25-1', 3054.42, 'Room # 1 rack #2', 0),
(8, '2', '2-22', '2-22-1', 294.09, 'Room # 2 rack # 6', 0),
(9, '2', '2-22', '2-22-5', 437.44, 'Room # 1 rack # 8', 0),
(10, '2', '2-22', '2-22-3', 437.44, 'Room # 1 rack # 8', 0),
(11, '2', '2-22', '2-22-2', 782, 'Store 3', 0),
(12, '2', '2-28', '2-28-1', 524.94, 'Store 2', 0),
(13, '2', '3-3', '3-3-2', 167.32, 'Room # 1 rack # 1', 0),
(14, '2', '3-3', '3-3-1', 377.27, 'Room # 1 rack # 4', 0),
(15, '2', '2-10', '2-10-1', 3973.07, 'Room # 2 rack # 2 /5', 0),
(16, '2', '2-12', '2-12-1', 436, 'Room # rack # 9', 0),
(17, '2', '2-23', '2-23-1', 79, 'Room #  rack # ', 0),
(18, '2', '3-2', '3-2-1', 201.9, 'Room # 1 rack # 3,6', 0),
(19, '2', '3-2', '3-2-2', 438.9, 'Room # 1 rack # 4', 0),
(20, '2', '3-2', '3-2-3', 295.9, 'Room # 1 rack # 7', 0),
(21, '2', '3-3', '3-3-4', 54.68, 'Room # 1 rack # 8', 0),
(22, '2', '2-22', '2-22-6', 2127.67, 'Room # 2 rack # 3', 0),
(23, '2', '3-1', '3-1-1', 254.9, 'Room # 1 rack # 1', 0),
(24, '2', '3-5', '3-5-1', 122.5, 'Room # 2 rack # 4', 0),
(25, '2', '3-4', '3-4-1', 197, 'Room # 1 rack #6', 0),
(26, '2', '3-5', '3-5-2', 140.6, 'Room # 2 rack # 4', 0),
(27, '2', '2-20', '2-20-3', 2882.08, 'Room # 1 rack # 8', 0),
(28, '2', '2-24', '2-24-1', 558.82, 'Room # 2 rack # 2', 0),
(29, '2', '2-14', '2-14-1', 814.2, 'Room # 1 rack # 9', 0),
(30, '2', '2-26', '2-26-1', 2826.4, 'Room # 1 store 2 store 3 rack 9', 0),
(31, '2', '2-2', '2-2-1', 102, 'Room # 2 rack # 4', 0),
(32, '2', '1-3', '1-3-4', 125, 'Abc', 0),
(33, '2', '1-1', '1-1-6', 2050, 'Abc', 0),
(34, '2', '1-6', '1-6-1', 25336, 'Fbf', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `material_store`
--
ALTER TABLE `material_store`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `material_store`
--
ALTER TABLE `material_store`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
