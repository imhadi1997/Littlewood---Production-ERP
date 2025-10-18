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
-- Table structure for table `material_name`
--

CREATE TABLE `material_name` (
  `id` int(255) NOT NULL,
  `mat_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `unit` varchar(255) NOT NULL,
  `type_id` varchar(255) NOT NULL,
  `new_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `material_name`
--

INSERT INTO `material_name` (`id`, `mat_id`, `name`, `color`, `unit`, `type_id`, `new_id`) VALUES
(1, '1-1', 'Coil zip no 3 open end da slider', 'Black/ykk', 'Pc', '1', 1),
(2, '1-2', 'Coil zip no 3 close end auto lock rubber slider', 'Red/ykk', 'Pc', '1', 2),
(3, '1-3', 'Coil zip no 3 close end da slider', 'Black/ykk', 'Pc', '1', 3),
(4, '1-4', 'Coil zip no 5 close end da slider', 'Black/ykk', 'Pc', '1', 4),
(5, '1-5', 'Coil zip no 5 open end da slider', 'Black/ykk', 'Pc', '1', 5),
(6, '1-6', 'Coil zip no 5 close end double slider', 'Black/ykk', 'Pc', '1', 6),
(7, '1-7', 'Coil zip no 5 open end da slider', 'Gray/ykk', 'Pc', '1', 7),
(8, '1-8', 'Coil zip no 5 close end auto lock reversable rubber slider', 'Black/ykk', 'Pc ', '1', 8),
(9, '1-9', 'Coil zip no 5 close end autolock double slider', 'Black/ykk', 'Pc ', '1', 9),
(10, '1-10', 'Coil zip no 5 close end auto lock rubber slider ', 'Black/ykk', 'Pc ', '1', 10),
(11, '1-11', 'Coil zip no 5 two tone close da slider', 'Black/ykk', 'Pc', '1', 11),
(12, '1-12', 'Coil zip no 8 open end da slider', 'Black/ykk', 'Pc', '1', 12),
(13, '1-13', 'Coil zip no 8 close end thumb slider', 'Black/ykk', 'Pc', '1', 13),
(14, '1-14', 'Plastic zip no 8 open end butterfly da slider', 'Black/ykk', 'Pc', '1', 14),
(15, '1-15', 'Plastic zip no 8 open end (killi wali side)', 'Black/ykk', 'Pc', '1', 15),
(16, '1-16', 'Plastic zip no 8 open end da slider', 'Black/ykk', 'Pc ', '1', 16),
(17, '1-17', 'Plastic zip no 8 open end butterfly da slider (complete)', 'Black/ykk', 'Pc', '1', 17),
(18, '1-18', 'Plastic zip no 8 open end da double thumb slider (complete)', 'Black/ykk', 'Pc', '1', 18),
(19, '2-1', 'Lycra', '', 'Yard', '2', 1),
(20, '2-2', 'Towel lycra', '', 'Yard', '2', 2),
(21, '2-3', 'Pipe elastic', '', 'Kg', '2', 3),
(22, '2-4', 'Cordura pu coated', 'All color', 'Yard', '2', 4),
(23, '2-5', 'Foam 1 sutar', 'Gray', 'Sheet', '2', 5),
(24, '2-6', 'Foam 3 sutar', 'Gray', 'Sheet', '2', 6),
(25, '2-7', 'Jambo foam', '', 'Foot', '2', 7),
(26, '2-8', 'Foam 1 inch', '', 'Sheet', '2', 8),
(27, '2-9', 'Neopreen', '', 'Sheet', '2', 9),
(28, '2-10', 'Ribstop', '', 'Yard', '2', 10),
(29, '2-11', 'Tarinda', '', 'Kg', '2', 11),
(30, '2-12', 'Hitena', '', 'Yard', '2', 12),
(31, '2-13', 'Cotton fabric', '', 'Yard', '2', 13),
(32, '2-14', 'Taslan', '', 'Yard', '2', 14),
(33, '2-15', 'Quilt', '', 'Yard', '2', 15),
(34, '2-16', 'Rough cordura', '', 'Yard', '2', 16),
(35, '2-17', 'Koreen ', '190-t', 'Meter', '2', 17),
(36, '2-18', 'Soft shell', ' imported', 'Meter', '2', 18),
(37, '2-19', 'Samtex', '', 'Yard', '2', 19),
(38, '2-20', 'Reissa', 'All colour', 'Yard', '2', 20),
(39, '2-21', 'Quilt leaser', 'All colour', 'Yard', '2', 21),
(40, '2-22', 'Cordura ', 'All color', 'Yard', '2', 22),
(41, '2-23', 'Pc foam', '', 'Yard', '2', 23),
(42, '2-24', 'Velcro fabric laminated', '', 'Sheet', '2', 24),
(43, '2-25', 'Tafeeta 210', '', 'Yard', '2', 25),
(44, '2-26', 'Micro fabric', '', 'Yard', '2', 26),
(45, '2-27', 'Stretch cordura', '', 'Yard', '2', 27),
(46, '2-28', 'Regmar grippy', '', 'Yard', '2', 28),
(47, '2-29', 'Rexin', '', 'Meter ', '2', 29),
(49, '2-30', 'Jeans cotton', '', 'Yard', '2', 30),
(57, '4-1', 'Velcro hook', 'Black', 'Meter', '4', 1),
(58, '4-2', 'Velcro loop', 'Black', 'Meter', '4', 2),
(59, '3-1', '5 bharay', 'All colour', 'Kg', '3', 1),
(60, '3-2', '11 bharay', 'All colour', 'Kg', '3', 2),
(61, '3-3', 'Air mesh 3d', 'All colour', 'Yard', '3', 3),
(84, '3-4', 'Body mesh(roma mesh)', '', 'Yard', '3', 4),
(85, '3-5', 'F5 mesh', '', 'Kg', '3', 5),
(86, '1-19', 'Coil zip no 3 close end da slider', 'Red/ykk', 'Pc', '1', 19),
(87, '1-20', 'Coil zip no 5 open end da slider', 'Black/max', 'Pc', '1', 20),
(88, '3-6', 'Football 3d mesh (perforated)', '', 'Yard', '3', 6),
(89, '2-31', 'Playboy lamination rubber', '', 'Sheet', '2', 31);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `material_name`
--
ALTER TABLE `material_name`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mat_id` (`mat_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `material_name`
--
ALTER TABLE `material_name`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
