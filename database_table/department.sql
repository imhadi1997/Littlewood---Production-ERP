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
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `id` int(255) NOT NULL,
  `dep_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`id`, `dep_id`, `name`) VALUES
(1, 'DEP-1', 'Stitching(leather)'),
(2, 'DEP-2', 'L-folding'),
(3, 'DEP-3', 'L-lining'),
(4, 'DEP-4', 'Packing'),
(5, 'DEP-5', 'Office'),
(6, 'DEP-6', 'Sample hall'),
(7, 'DEP-7', 'Printing'),
(8, 'DEP-8', 'Sweepers'),
(9, 'DEP-9', 'Main store'),
(10, 'DEP-10', 'Reception'),
(11, 'DEP-11', 'Logo printer'),
(12, 'DEP-12', 'Button'),
(13, 'DEP-13', 'Drivers'),
(14, 'DEP-14', 'Electricians'),
(15, 'DEP-15', 'Security guards'),
(16, 'DEP-16', 'L-cutting'),
(17, 'DEP-17', 'Palloy'),
(18, 'DEP-18', 'Molding'),
(19, 'DEP-19', 'Checking'),
(20, 'DEP-20', 'Pattern'),
(21, 'DEP-21', 'Mechanics'),
(22, 'DEP-22', 'Pressing'),
(23, 'DEP-23', 'Bartake/sealing'),
(24, 'DEP-24', 'Information technology'),
(25, 'DEP-25', 'Extra'),
(26, 'DEP-26', 'T-stitching'),
(27, 'DEP-27', 'T-tracing'),
(28, 'DEP-28', 'T-lining'),
(29, 'DEP-29', 'T-cutting');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dep_id` (`dep_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
