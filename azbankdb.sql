-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2021 at 10:10 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `azbankdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `azbank_empusers`
--

CREATE TABLE `azbank_empusers` (
  `id` int(10) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `accountname` varchar(300) DEFAULT NULL,
  `accountno` bigint(20) UNSIGNED DEFAULT NULL,
  `bvn` bigint(20) UNSIGNED DEFAULT NULL,
  `age` int(20) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `marital_status` varchar(100) NOT NULL,
  `next_of_kin` varchar(300) NOT NULL,
  `address` varchar(500) NOT NULL,
  `account_type` varchar(100) NOT NULL,
  `amount` double(65,2) DEFAULT NULL,
  `narration` longtext NOT NULL DEFAULT 'Account Statement'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `azbank_empusers`
--

INSERT INTO `azbank_empusers` (`id`, `customer_id`, `firstname`, `lastname`, `accountname`, `accountno`, `bvn`, `age`, `gender`, `marital_status`, `next_of_kin`, `address`, `account_type`, `amount`, `narration`) VALUES
(6, 412507551, 'anjie', 'layo', 'anjielayo', 2528758045, 23087269845, 20, 'female', 'single', 'kolaolutomilayo', 'lagos', 'savings', 246998.02, 'Account Statement \nairtime amount:30000 on 12/08/2021 01:30:49.\nelectricity bills amount:30000 plan:Electricityon 12/08/2021 02:20:44.\npity you amount:2000 on 12/08/2021 03:39:52.\npity you amount:2000 on 12/08/2021 03:40:06.\ndstv amount:3000 plan:DSTV on 12/08/2021 04:53:02.\ndstv amount:3000 plan:DSTV on 12/08/2021 04:53:40.\ncredit amount:2000 on 12/08/2021 04:54:18.\nairtime amount:3000 on 12/08/2021 04:54:48.\nanjie phone DR amount:500.59 on 14/08/2021 00:54:28.\nanjie phone DR amount:500.59 on 14/08/2021 00:57:01.\nanjie phone DR amount:500.59 on 14/08/2021 00:57:57.\nanjie phone DR amount:500.59 on 14/08/2021 00:59:19.\nanjie phone DR amount:500.56 on 14/08/2021 01:03:59.\ncredit amount:500.11 on 14/08/2021 06:00:52.\ncreditkc amount:500.11 on 14/08/2021 06:15:53.\ncreditkc amount:500.22 on 14/08/2021 06:16:13.\nurgent 2k for water bills DR amount:2000 on 15/08/2021 08:50:46.\nfor bbn DR amount:2000 on 15/08/2021 08:56:29.\nairtimetoanjieVTU topup to 08033592299 DR amount:340.00 to: Airtel vendor on 15/08/2021 18:01:47.\ntestVTU topup to 08033592299 DR amount:300.82 to: 9mobile vendor on 15/08/2021 18:12:59.\nantestvtu topup to 08033592299 DR amount:500.20 to: Glo vendor on 15/08/2021 18:27:46.\ntestbills DR amount:500.68 on 15/08/2021 18:53:11.\ntestquickbills DR amount:500.99 on 15/08/2021 18:54:01.\ntesttransfer amount:10000 on 15/08/2021 19:38:12.\ntestback DR amount:2000.99 on 15/08/2021 20:08:54.\ntest amount:200.99 on 15/08/2021 20:09:18.\ntest credit amount:200.99 on 15/08/2021 20:09:18.\ntestVTU topup to 08033189985 DR amount:2000.99 to: Airtel vendor on 15/08/2021 20:09:44.\ntest amount:30000 on 16/08/2021 13:25:42.\ntestcash credit amount:49000 on 17/08/2021 06:47:18.\ntestcash amount:49000 on 17/08/2021 06:47:42.\ntestcash amount:49000 on 17/08/2021 06:49:17.'),
(8, 76833199, 'funmise', 'adefila', 'funmiseadefila', 2699138101, 25035316693, 20, 'male', 'single', 'adefila', 'lagos', 'savings', 449345.00, 'Account Statement\nairtime to kc amount:2000 on 12/08/2021 15:21:23.\nfunmisesdebt credit amount:8000 on 14/08/2021 02:22:51.\n credit amount:10000 on 16/08/2021 13:29:23.'),
(9, 577781246, 'kelechi', 'enitan', 'kelechienitan', 4060180900, 59896689515, 20, 'male', 'single', 'enitan', 'lagos', 'savings', 28100.00, 'Account Statement\npity you credit amount:2000 on 12/08/2021 03:39:52.\npity you credit amount:2000 on 12/08/2021 03:40:06.\ncredit credit amount:2000 on 12/08/2021 04:54:18.\ncredit amount:200 on 12/08/2021 04:58:26.\ncredit amount:200 on 12/08/2021 04:58:38.\nairtime to kc credit amount:2000 on 12/08/2021 15:21:23.\ndstv bills amount:2000 plan:DSTV on 12/08/2021 22:02:27.\nwater bills amount:1000 plan:Water on 12/08/2021 22:10:34.\nwater bills amount:1000 plan:Water on 12/08/2021 22:13:47. \nCredit of 10000.78 to 4060180900 on 14/08/2021 01:37:34. \nCredit of 500.59 to 4060180900 on 14/08/2021 01:43:53.\nanjiesphoneDRamount50037toGloon14082021021251\nfunmisesdebt amount:8000 on 14/08/2021 02:22:51.\ncredit credit amount:500.11 on 14/08/2021 06:00:52.\ncreditkc credit amount:500.11 on 14/08/2021 06:15:53.\ncreditkc credit amount:500.22 on 14/08/2021 06:16:13.\nairitmetoanjieVTU topup to 08033592299 DR amount:400 to: Glo vendor on 15/08/2021 09:00:00.\ntesttransfer credit amount:10000 on 15/08/2021 19:38:12.\ntestifhehasacashVTU topup to 08033592299 DR amount:20046.44 to: Airtel vendor on 17/08/2021 06:33:29. \nCredit of 50000 to 4060180900 on 17/08/2021 06:46:28.\ntestcash amount:49000 on 17/08/2021 06:47:18.\ntestcash credit amount:49000 on 17/08/2021 06:47:42.\ntestcashvtu topup to 08033592299 DR amount:50000 to: Airtel vendor on 17/08/2021 06:48:14.\ntestcash credit amount:49000 on 17/08/2021 06:49:17.\n DR amount:5900 on 17/08/2021 06:49:45.\n DR amount:5000 on 17/08/2021 06:50:21.\n DR amount:5000 on 17/08/2021 06:50:36.\nVTU topup to 08033592299 DR amount:5000 to: Airtel vendor on 17/08/2021 06:51:40.'),
(18, 763062461, 'ariel', 'layo', 'ariellayo', 2126605476, 60423820832, 20, 'female', 'single', 'layo', 'lagos', 'savings', 368345.00, 'Account Statement\nairtime amount:30000 on 12/08/2021 01:29:25.\nwaterbills amount:35000 plan:Wateron 12/08/2021 02:18:47.'),
(23, 974716141, 'amaka', 'chizobar', 'amakachizobar', 8033002712, 12105487512, 20, 'female', 'single', 'chizobar', 'lagos', 'savings', 44368300.00, 'Account Statement \nCredit of 60000 to 8033002712 on 11/08/2021 09:10:49. \nCredit of 60000 to 8033002712 on 11/08/2021 09:11:59. \nCredit of 40000 to 8033002712 on 11/08/2021 09:14:57. \nCredit of 20000 to 8033002712 on 11/08/2021 09:17:40. \nCredit of 150000 to 8033002712 on 11/08/2021 09:22:19. \nCredit of 50000 to 8033002712 on 11/08/2021 09:40:39. \nCredit of 2000 to 8033002712 on 11/08/2021 09:45:29. \nCredit of 12000 to 8033002712 on 11/08/2021 09:46:35. \nCredit of 2345 to 8033002712 on 11/08/2021 09:47:38.airtimeairtime\nairtime amount:8000 on11/08/2021 23:31:06.\nairtime amount:2500 on 11/08/2021 23:34:24.\nairtime amount:2500 on 11/08/2021 23:49:14.\nairtime amount:30000 on 12/08/2021 01:23:18.\nairtime amount:30000 on 12/08/2021 01:23:38.'),
(27, 556387593, 'denrele', 'edun', 'denreleedun', 9253910513, 57844202791, 20, 'male', 'single', 'edun', 'lagos', 'current', 433345.00, 'Account Statement'),
(28, 95172720, 'hush', 'puppi', 'hushpuppi', 2595684421, 39705292747, 30, 'male', 'married', 'puppi', 'lagos', 'current', 1000049984.00, 'Account Statement \nCredit of 1000000000 to 2595684421 on 12/08/2021 04:59:32.'),
(29, 428840943, 'james', 'kayode', 'jameskayode', 5617460077, 54585483038, 23, 'male', 'married', 'dennis kayode', 'yaba,lagos', 'savings', 50000.00, 'Account Statement'),
(30, 617264810, 'john', 'kayode', 'johnkayode', 1623595239, 28535515344, 24, 'male', 'married', 'dennis kayode', 'yaba', 'current', 50000.00, 'Account Statement'),
(31, 838504763, 'damola', 'coker', 'damolacoker', 4469114218, 87895101047, 20, 'male', 'single', 'coker', 'surulere', 'current', 50100.00, 'Account Statement\ntest credit amount:30000 on 16/08/2021 13:25:42.\nVTU topup to 08032768948 DR amount:5000 to: MTN vendor on 16/08/2021 13:27:31.\n DR amount:14900 on 16/08/2021 13:28:11.\n amount:10000 on 16/08/2021 13:29:23.'),
(32, 74293929, 'ebube', 'muoglim', 'ebubemuoglim', 9158754127, 30161191100, 21, 'female', 'single', 'muoglim', 'lagos', 'current', 50000.00, 'Account Statement');

-- --------------------------------------------------------

--
-- Table structure for table `azbank_regusers`
--

CREATE TABLE `azbank_regusers` (
  `id` int(10) NOT NULL,
  `userid` varchar(300) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `pin` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `azbank_regusers`
--

INSERT INTO `azbank_regusers` (`id`, `userid`, `password`, `pin`) VALUES
(2, '2528758045', 'h@123AA', '1234'),
(3, '2699138101', 'h@123A', '1234'),
(4, '4060180900', 'h@123A', '1234'),
(5, '4469114218', 'Abc1234$', '0070'),
(6, '9158754127', 'h@123A', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `azbank_staff`
--

CREATE TABLE `azbank_staff` (
  `id` int(10) NOT NULL,
  `staff_id` varchar(50) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `azbank_staff`
--

INSERT INTO `azbank_staff` (`id`, `staff_id`, `name`, `password`) VALUES
(1, '1702862', 'Anjolaoluwa', 'admin'),
(2, '1802863', 'Tobiloba', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `bill_vendors`
--

CREATE TABLE `bill_vendors` (
  `id` int(10) NOT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `accountno` bigint(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill_vendors`
--

INSERT INTO `bill_vendors` (`id`, `vendor`, `accountno`) VALUES
(1, 'DSTV', 1370463142),
(2, 'Water', 752197033),
(3, 'Electricity', 2994824703),
(4, 'AXA Mansard Insurance', 4620443220),
(5, 'Smile Internet Service', 5344058261);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `azbank_empusers`
--
ALTER TABLE `azbank_empusers`
  ADD PRIMARY KEY (`id`,`customer_id`);

--
-- Indexes for table `azbank_regusers`
--
ALTER TABLE `azbank_regusers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `azbank_staff`
--
ALTER TABLE `azbank_staff`
  ADD PRIMARY KEY (`id`,`staff_id`);

--
-- Indexes for table `bill_vendors`
--
ALTER TABLE `bill_vendors`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `azbank_empusers`
--
ALTER TABLE `azbank_empusers`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `azbank_regusers`
--
ALTER TABLE `azbank_regusers`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `azbank_staff`
--
ALTER TABLE `azbank_staff`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bill_vendors`
--
ALTER TABLE `bill_vendors`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
