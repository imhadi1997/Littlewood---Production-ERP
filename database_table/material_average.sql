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
-- Table structure for table `material_average`
--

CREATE TABLE `material_average` (
  `id` int(255) NOT NULL,
  `order_id` varchar(255) NOT NULL,
  `mat_id` varchar(255) NOT NULL,
  `art_id` varchar(255) NOT NULL,
  `std_avg` float NOT NULL,
  `est_avg` float NOT NULL,
  `use_in` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `material_average`
--

INSERT INTO `material_average` (`id`, `order_id`, `mat_id`, `art_id`, `std_avg`, `est_avg`, `use_in`, `details`, `user`, `status`) VALUES
(1, '1', '2-25', '2-25-1', 0.97, 122.5, '2', '', '1', 0),
(2, '1', '2-22', '2-22-6', 1.94, 244.99, '1', '', '1', 0),
(3, '1', '2-11', '2-11-1', 0.03, 3.53, '1', '', '1', 0),
(4, '1', '2-9', '2-9-1', 0.02, 2.42, '1', '', '1', 0),
(5, '1', '2-22', '2-22-1', 0.39, 48.99, '1', '', '1', 0),
(6, '1', '2-15', '2-15-1', 1.56, 195.99, '2', '', '1', 0),
(7, '1', '2-1', '2-1-1', 0.33, 42, '2', '', '1', 0),
(8, '1', '2-3', '2-3-1', 0.05, 6.3, '1', '', '1', 0),
(9, '1', '2-22', '2-22-4', 0.06, 6.99, '1', '', '1', 0),
(10, '1', '3-3', '3-3-1', 0.17, 20.99, '2', '', '1', 0),
(11, '1', '4-1', '4-1-3', 0.15, 19.2, '4', 'Use in body', '1', 0),
(12, '1', '4-2', '4-2-3', 0.64, 80.01, '4', 'Use in body', '1', 0),
(13, '1', '4-1', '4-1-5', 0.15, 19.2, '4', 'Use in body', '1', 0),
(14, '1', '4-2', '4-2-5', 0.64, 80.01, '4', 'Use in body', '1', 0),
(15, '1', '4-1', '4-1-2', 1.02, 128.02, '4', 'Use in lining + body', '1', 0),
(16, '1', '4-2', '4-2-2', 1.02, 128.02, '4', 'Use in lining + body', '1', 0),
(17, '1', '1-12', '1-12-2', 1, 10, '3', 'Only for 52 size article (body)', '1', 0),
(18, '1', '1-12', '1-12-4', 1, 15, '3', 'Only for 56 size article (body)', '1', 0),
(19, '1', '1-12', '1-12-8', 1, 5, '3', 'Only for 60 size article (body)', '1', 0),
(20, '1', '1-12', '1-12-11', 1, 10, '3', 'Only for 58 size article (body)', '1', 0),
(21, '1', '1-12', '1-12-7', 1, 5, '3', 'Only for 64 size article (body)', '1', 0),
(22, '1', '1-12', '1-12-13', 1, 36, '3', 'Only for 54 size article (body)', '1', 0),
(23, '1', '1-11', '1-11-1', 1, 126, '3', 'For all size (body)', '1', 0),
(24, '1', '1-9', '1-9-2', 1, 126, '3', 'For all size (body)', '1', 0),
(25, '1', '1-4', '1-4-11', 2, 252, '3', 'For all size (body)', '1', 0),
(26, '1', '1-19', '1-19-1', 1, 126, '3', 'For all size (lining)', '1', 0),
(27, '1', '1-20', '1-20-1', 1, 10, '3', 'Only for 52 size article (lining)', '1', 0),
(28, '1', '1-20', '1-20-2', 1, 36, '3', 'Only for 54 size article (lining)', '1', 0),
(29, '1', '1-20', '1-20-3', 1, 15, '3', 'Only for 56 size article (lining)', '1', 0),
(30, '1', '1-20', '1-20-4', 1, 10, '3', 'Only for 58 size article (lining)', '1', 0),
(31, '1', '1-20', '1-20-5', 1, 30, '3', 'Only for 60 size article (lining)', '1', 0),
(32, '1', '1-20', '1-20-7', 1, 5, '3', 'Only for 64 size article (lining)', '1', 0),
(33, '1', '2-20', '2-20-3', 1.5, 189, '2', '', '1', 0),
(34, '1', '3-5', '3-5-2', 0.04, 5.04, '1', '', '1', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `material_average`
--
ALTER TABLE `material_average`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `material_average`
--
ALTER TABLE `material_average`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
