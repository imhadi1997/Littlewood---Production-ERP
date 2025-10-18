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
-- Table structure for table `factory_requisition`
--

CREATE TABLE `factory_requisition` (
  `id` int(255) NOT NULL,
  `req_id` int(255) NOT NULL,
  `req_no` varchar(255) NOT NULL,
  `dep_id` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `add_by` varchar(255) NOT NULL,
  `add_date` date NOT NULL,
  `add_time` varchar(255) NOT NULL,
  `approve_status` tinyint(1) NOT NULL,
  `approve_by` varchar(255) NOT NULL,
  `approve_date` date NOT NULL,
  `approve_time` varchar(255) NOT NULL,
  `clear_status` tinyint(1) NOT NULL,
  `clear_date` date NOT NULL,
  `clear_time` varchar(255) NOT NULL,
  `clear_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `factory_requisition`
--

INSERT INTO `factory_requisition` (`id`, `req_id`, `req_no`, `dep_id`, `details`, `add_by`, `add_date`, `add_time`, `approve_status`, `approve_by`, `approve_date`, `approve_time`, `clear_status`, `clear_date`, `clear_time`, `clear_by`) VALUES
(1, 1, '1-1', 'DEP-24', 'Messagebox.showerror(parent=self.root2,title=\"empty\", message=\"fill required fields\")\n', '1', '2023-07-24', '06:10 PM', 1, '3', '2023-08-01', '10:10 AM', 0, '0000-00-00', '', ''),
(2, 2, '1-2', 'DEP-26', 'Messagebox.showerror(parent=self.root2,title=\"empty\", message=\"fill required fields\")\n', '1', '2023-07-24', '06:12 PM', 0, '', '0000-00-00', '', 0, '0000-00-00', '', ''),
(3, 3, '1-3', 'DEP-1', 'Messagebox.showerror(parent=self.root2,title=\"empty\", message=\"fill required fields\")\n', '1', '2023-07-24', '06:12 PM', 0, '', '0000-00-00', '', 0, '0000-00-00', '', ''),
(4, 4, '1-4', 'DEP-24', '3 desktop systems \n1- main store\n2 - glove store\n3 - receipt system\n', '1', '2023-08-01', '04:22 AM', 0, '', '0000-00-00', '', 0, '0000-00-00', '', ''),
(5, 5, '1-5', 'DEP-29', 'Customer po: 611897\nfactory po: c-78, c-79\nblack cordura for cutting \nqty : 650yards\n', '1', '2023-08-01', '03:33 PM', 0, '', '0000-00-00', '', 0, '0000-00-00', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `factory_requisition`
--
ALTER TABLE `factory_requisition`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `req_no` (`req_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `factory_requisition`
--
ALTER TABLE `factory_requisition`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
