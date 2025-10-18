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
-- Table structure for table `employee_ledger`
--

CREATE TABLE `employee_ledger` (
  `id` int(255) NOT NULL,
  `emp_id` varchar(255) NOT NULL,
  `amount` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_ledger`
--

INSERT INTO `employee_ledger` (`id`, `emp_id`, `amount`, `name`, `date`, `time`, `type`, `category`, `user`) VALUES
(1, 'EMP-14', 5000, 'August weekly salary short term', '2023-08-22', '08:05 PM', 'Short Term', 'Debit', '1'),
(2, 'EMP-14', 6000, 'August 2nd week salary short term', '2023-08-23', '08:06 PM', 'Short Term', 'Debit', '1'),
(3, 'EMP-14', 3000, 'Deduction from salary', '2023-08-24', '08:06 PM', 'Short Term', 'Credit', '1'),
(4, 'EMP-14', 8500, 'Cash in hand received (but due to lack of cash can\'t return)', '2023-08-25', '08:07 PM', 'Short Term', 'Credit', '1'),
(5, 'EMP-14', 500, 'Cash return to him from wages payment', '2023-08-26', '08:21 PM', 'Short Term', 'Debit', '1'),
(6, 'EMP-14', 130000, 'Long term order by asim butt saab.', '2023-09-18', '02:48 AM', 'Long Term', 'Debit', '1'),
(7, 'EMP-14', 10000, 'Deduction from salary sept-20223', '2023-09-18', '02:49 AM', 'Long Term', 'Credit', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee_ledger`
--
ALTER TABLE `employee_ledger`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee_ledger`
--
ALTER TABLE `employee_ledger`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
