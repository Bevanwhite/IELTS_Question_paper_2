-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 11, 2021 at 04:50 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jeffery`
--

-- --------------------------------------------------------

--
-- Table structure for table `confirm_quiz_answer`
--

DROP TABLE IF EXISTS `confirm_quiz_answer`;
CREATE TABLE IF NOT EXISTS `confirm_quiz_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer1` varchar(500) DEFAULT NULL,
  `answer2` varchar(500) DEFAULT NULL,
  `answer3` varchar(500) DEFAULT NULL,
  `answer4` varchar(500) DEFAULT NULL,
  `answer5` varchar(500) DEFAULT NULL,
  `answer6` varchar(500) DEFAULT NULL,
  `answer7` varchar(500) DEFAULT NULL,
  `answer8` varchar(500) DEFAULT NULL,
  `answer9` varchar(500) DEFAULT NULL,
  `answer10` varchar(500) DEFAULT NULL,
  `answer11` varchar(500) DEFAULT NULL,
  `answer12` varchar(500) DEFAULT NULL,
  `answer13` varchar(500) DEFAULT NULL,
  `answer14` varchar(500) DEFAULT NULL,
  `answer15` varchar(500) DEFAULT NULL,
  `answer16` varchar(500) DEFAULT NULL,
  `answer17` varchar(500) DEFAULT NULL,
  `answer18` varchar(500) DEFAULT NULL,
  `answer19` varchar(500) DEFAULT NULL,
  `answer20` varchar(500) DEFAULT NULL,
  `answer21` varchar(500) DEFAULT NULL,
  `answer22` varchar(500) DEFAULT NULL,
  `answer23` varchar(500) DEFAULT NULL,
  `answer24` varchar(500) DEFAULT NULL,
  `answer25` varchar(500) DEFAULT NULL,
  `answer26` varchar(500) DEFAULT NULL,
  `answer27` varchar(500) DEFAULT NULL,
  `answer28` varchar(500) DEFAULT NULL,
  `answer29` varchar(500) DEFAULT NULL,
  `answer30` varchar(500) DEFAULT NULL,
  `answer31` varchar(500) DEFAULT NULL,
  `answer32` varchar(500) DEFAULT NULL,
  `answer33` varchar(500) DEFAULT NULL,
  `answer34` varchar(500) DEFAULT NULL,
  `answer35` varchar(500) DEFAULT NULL,
  `answer36` varchar(500) DEFAULT NULL,
  `answer37` varchar(500) DEFAULT NULL,
  `answer38` varchar(500) DEFAULT NULL,
  `answer39` varchar(500) DEFAULT NULL,
  `answer40` varchar(500) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quiz_id` (`quiz_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `create_quiz`
--

DROP TABLE IF EXISTS `create_quiz`;
CREATE TABLE IF NOT EXISTS `create_quiz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `question` varchar(500) NOT NULL,
  `toq` varchar(50) NOT NULL,
  `answer01` varchar(100) NOT NULL,
  `answer02` varchar(100) NOT NULL,
  `answer03` varchar(100) NOT NULL,
  `answer04` varchar(100) NOT NULL,
  `correct_answer` varchar(100) NOT NULL,
  `index_no` int(11) NOT NULL,
  `date_posted` datetime NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `quiz_id` (`quiz_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `create_quiz`
--

INSERT INTO `create_quiz` (`id`, `title`, `question`, `toq`, `answer01`, `answer02`, `answer03`, `answer04`, `correct_answer`, `index_no`, `date_posted`, `quiz_id`, `user_id`) VALUES
(1, 'Public Speaking', 'In public speaking, sound ethical decisions involve weighing a potential course of action against ', 'radio', ' A set of ethical standards or guidelines', ' The practicality of taking that course of action', ' A set of legal criteria for acceptable speech', ' The speakers goals in a given situation', '1', 1, '2021-01-09 18:37:20', 3, 1),
(2, 'anxiety', '.................... is anxiety over the prospect of giving a speech in front of an audience', 'radio', ' Adrenaline', ' Visualization', ' Stage Fright', 'None', '3', 2, '2021-01-09 18:37:20', 3, 1),
(3, 'Textbook', 'Which of the following does your textbook recommend as a way to help you deal with nervousness in your speeches? ', 'radio', ' Be prepared to fail in your first few speeches', ' Tell the audience how nervous you get when speaking', ' Work especially hard on your speech introduction', ' All answers are correct', '3', 1, '2021-01-09 18:37:20', 4, 1),
(4, 'Speeches', 'What are the three general purposes for giving speeches?', 'radio', 'To persuade, act , & adjust your speaking style', 'To inform, make people laugh, & have fun', 'To inform, persuade, & entertain', 'None of the Above', '4', 2, '2021-01-09 18:37:20', 4, 1),
(5, 'language or ideas', 'If you present another persons language or ideas as your own, you are guilty of ', 'radio', ' Defamation', ' Personification', ' Plagiarism', 'None', '3', 1, '2021-01-09 18:37:20', 5, 1),
(6, 'speechmaking', 'The primary purpose of speechmaking is to ', 'radio', ' Display your knowledge about a topic', ' Gain a desired response from listeners', ' Enhance the audiences self-concept', ' Promote your ethical standards', '2', 1, '2021-01-09 18:37:20', 6, 1),
(7, 'Textbook 1', 'Which of the following does your textbook discuss as major factors in demographic audience analysis? ', 'radio', ' Education, cultural background, and interest in the topic', ' Physical setting, religion, and audience size', ' Gender, age, group membership, and sexual orientation', ' Social status, ethnicity, and attitude toward the topic', '3', 2, '2021-01-09 18:37:20', 6, 1),
(8, 'Responsibilities', 'Because speechmaking is a form of power, it carries with it heavy .................... responsibilities. ', 'radio', 'Ethical', 'Psychological', ' Sociological', 'None', '1', 3, '2021-01-09 18:37:20', 6, 1),
(9, 'Imaging', '.................... is mental imaging in which a speaker vividly pictures himself or herself giving a successful presentation ', 'radio', 'Focusing', 'Visualization', 'Representation', 'Channeling', '2', 1, '2021-01-09 18:37:20', 7, 1),
(10, 'knowledge experience', 'The knowledge, experience, goals, values, and attitudes through which each listener filters a message make up the listeners ', 'radio', ' Frame of Reference', ' Cognitive Screen', ' Psychological Filter', ' Attitudinal Field', '1', 4, '2021-01-09 18:37:20', 6, 1),
(11, 'Plagiarism', 'According to your textbook, stealing ideas or language from two or three sources and passing them off as ones own is called ', 'radio', ' Global plagiarism.', ' Patchwork plagiarism.', ' Admissible plagiarism.', ' Incremental plagiarism.', '2', 5, '2021-01-09 18:37:20', 6, 1),
(12, 'Generating ', '.................... is a method of generating ideas for speech topics by free association of words and ideas ', 'radio', ' Imaging', ' Brainstorming', ' Channeling', ' None of the above', '2', 3, '2021-01-09 18:37:20', 4, 1),
(13, 'Structure ', 'When you want to change or structure the attitudes of your audience, your general purpose is to ', 'radio', ' Inform', ' Persuade', ' Entertain', ' None of the above', '2', 4, '2021-01-09 18:37:20', 4, 1),
(14, 'Structures', 'When you want to change or structure the attitudes of your audience, your general purpose is to ', 'radio', ' Inform', ' Persuade', ' Entertain', ' None of the above', '2', 5, '2021-01-09 18:37:20', 4, 1),
(15, 'see this ', 'what is the ranger name', 'short', 'none', 'none', 'none', 'none', 'Tiger', 1, '2021-01-09 18:37:20', 10, 1),
(16, 'Television 1', 'see this', 'short', 'none', 'none', 'none', 'none', 'ranger', 1, '2021-01-09 18:37:20', 2, 1),
(17, '1. Present Simple - Complete the sentence.', ' Jessica _____four languages.', 'radio', 'speak', 'spoke', 'speaks', 'will speak', '3', 1, '2021-01-10 21:52:25', 11, 1),
(23, '1. Choose the correct linking word:', '_____ the rain, we still went to the park.\r\n', 'radio', 'Despite', 'However', 'Although', 'After', '1', 1, '2021-01-10 21:52:25', 14, 1),
(18, '2. Present Simple - Complete the sentence.', 'In Britain the banks usually _____ at 9.30 in the morning. ', 'radio', 'open', 'opened', 'opens', 'opening', '3', 2, '2021-01-10 21:52:25', 11, 1),
(19, '1. Which is right?', '‘_____ ?’ ‘No, she’s on holiday.’\r\n', 'radio', 'Does Sue work', 'Is working Sue', 'Is Sue working', 'Does Sue work', '3', 1, '2021-01-10 21:52:25', 12, 1),
(20, '2. Which is right?', '‘Where _____?’ ‘In a village near London.’', 'radio', 'lives your uncle', 'does your uncle live', 'your uncle lives', 'does live your uncle', '2', 2, '2021-01-10 21:52:25', 12, 1),
(21, '1. Grammar practise quiz 1', 'The size of the pupil in the eye __________ good indicator of a person\'s interest, emotion, attitude and thought processes.\r\n', 'radio', 'is a', 'the', 'being the', 'as the', '1', 1, '2021-01-10 21:52:25', 13, 1),
(22, '2. Grammar practise quiz 1', 'Ozone ___________ extremely active chemically and succeeds in damaging any vegetation it comes in contact with.', 'radio', 'by being', 'is', 'which is', 'being', '2', 2, '2021-01-10 21:52:25', 13, 1),
(24, '2. Choose the correct linking word:', '_____ it was raining, we still went to the park.\r\n', 'radio', 'Despite', 'However', 'Although', 'After', '3', 2, '2021-01-10 21:52:25', 14, 1),
(25, '1. Use one of the word or phrase:', 'I\'ll call you _____ I get home.', 'radio', 'after', 'as soon as', 'once', 'while', '1', 1, '2021-01-10 21:52:25', 15, 1),
(26, '2. Use one of the word or phrase:', 'We decided to go for a walk _____ we had had lunch.', 'radio', 'after', 'as soon as', 'because', 'by the time', '1', 2, '2021-01-10 21:52:25', 15, 1),
(27, '1. Choose the correct linking word.', 'I am having a great time in England , _____ the bad weather.', 'radio', 'despite', 'because', 'whereas', 'while', '1', 1, '2021-01-10 21:52:25', 16, 1),
(28, '2. Choose the correct linking word.', 'She did well in the test, _____ Tom didn’t.', 'radio', 'in spite of', 'when', 'whereas', 'despite', '3', 2, '2021-01-10 21:52:25', 16, 1);

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `toq` varchar(50) NOT NULL,
  `gandco` varchar(50) NOT NULL,
  `userbased` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date_posted` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`id`, `name`, `toq`, `gandco`, `userbased`, `user_id`, `date_posted`) VALUES
(1, 'test - advanced', 'speaking', 'grammar', 'advanced', 1, '2021-01-09 18:37:20'),
(2, 'test - intermediate', 'speaking', 'grammar', 'intermediate', 1, '2021-01-09 18:37:20'),
(3, 'test - Perliminary', 'speaking', 'grammar', 'preliminary', 1, '2021-01-09 18:37:20'),
(4, 'Normal Paper - 1', 'speaking', 'none', 'preliminary', 1, '2021-01-09 18:37:20'),
(5, 'Normal Paper - 2', 'speaking', 'none', 'intermediate', 1, '2021-01-09 18:37:20'),
(6, 'Normal Paper - 3', 'speaking', 'none', 'advanced', 1, '2021-01-09 18:37:20'),
(7, 'Cohesion paper -1', 'speaking', 'cohesion', 'preliminary', 1, '2021-01-09 18:37:20'),
(8, 'Cohesion paper -2', 'speaking', 'cohesion', 'intermediate', 1, '2021-01-09 18:37:20'),
(9, 'Cohesion paper - 3', 'speaking', 'cohesion', 'advanced', 1, '2021-01-09 18:37:20'),
(10, 'ranger', 'speaking', 'grammar', 'preliminary', 1, '2021-01-09 18:37:20'),
(11, 'Grammar Worksheet 1 - P', 'writing', 'grammar', 'preliminary', 1, '2021-01-10 21:52:25'),
(12, 'Grammar Worksheet 1 - I', 'writing', 'grammar', 'intermediate', 1, '2021-01-10 21:52:25'),
(13, 'Grammar Worksheet 1 - A', 'writing', 'grammar', 'advanced', 1, '2021-01-10 21:52:25'),
(14, 'Cohesion Worksheet 1 - P', 'writing', 'cohesion', 'preliminary', 1, '2021-01-10 21:52:25'),
(15, 'Cohesion Worksheet 1 - I', 'writing', 'cohesion', 'intermediate', 1, '2021-01-10 21:52:25'),
(16, 'Cohesion Worksheet 1 - A', 'writing', 'cohesion', 'advanced', 1, '2021-01-10 21:52:25');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_answer`
--

DROP TABLE IF EXISTS `quiz_answer`;
CREATE TABLE IF NOT EXISTS `quiz_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer1` varchar(500) DEFAULT NULL,
  `answer2` varchar(500) DEFAULT NULL,
  `answer3` varchar(500) DEFAULT NULL,
  `answer4` varchar(500) DEFAULT NULL,
  `answer5` varchar(500) DEFAULT NULL,
  `answer6` varchar(500) DEFAULT NULL,
  `answer7` varchar(500) DEFAULT NULL,
  `answer8` varchar(500) DEFAULT NULL,
  `answer9` varchar(500) DEFAULT NULL,
  `answer10` varchar(500) DEFAULT NULL,
  `answer11` varchar(500) DEFAULT NULL,
  `answer12` varchar(500) DEFAULT NULL,
  `answer13` varchar(500) DEFAULT NULL,
  `answer14` varchar(500) DEFAULT NULL,
  `answer15` varchar(500) DEFAULT NULL,
  `answer16` varchar(500) DEFAULT NULL,
  `answer17` varchar(500) DEFAULT NULL,
  `answer18` varchar(500) DEFAULT NULL,
  `answer19` varchar(500) DEFAULT NULL,
  `answer20` varchar(500) DEFAULT NULL,
  `answer21` varchar(500) DEFAULT NULL,
  `answer22` varchar(500) DEFAULT NULL,
  `answer23` varchar(500) DEFAULT NULL,
  `answer24` varchar(500) DEFAULT NULL,
  `answer25` varchar(500) DEFAULT NULL,
  `answer26` varchar(500) DEFAULT NULL,
  `answer27` varchar(500) DEFAULT NULL,
  `answer28` varchar(500) DEFAULT NULL,
  `answer29` varchar(500) DEFAULT NULL,
  `answer30` varchar(500) DEFAULT NULL,
  `answer31` varchar(500) DEFAULT NULL,
  `answer32` varchar(500) DEFAULT NULL,
  `answer33` varchar(500) DEFAULT NULL,
  `answer34` varchar(500) DEFAULT NULL,
  `answer35` varchar(500) DEFAULT NULL,
  `answer36` varchar(500) DEFAULT NULL,
  `answer37` varchar(500) DEFAULT NULL,
  `answer38` varchar(500) DEFAULT NULL,
  `answer39` varchar(500) DEFAULT NULL,
  `answer40` varchar(500) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quiz_id` (`quiz_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quiz_answer`
--

INSERT INTO `quiz_answer` (`id`, `answer1`, `answer2`, `answer3`, `answer4`, `answer5`, `answer6`, `answer7`, `answer8`, `answer9`, `answer10`, `answer11`, `answer12`, `answer13`, `answer14`, `answer15`, `answer16`, `answer17`, `answer18`, `answer19`, `answer20`, `answer21`, `answer22`, `answer23`, `answer24`, `answer25`, `answer26`, `answer27`, `answer28`, `answer29`, `answer30`, `answer31`, `answer32`, `answer33`, `answer34`, `answer35`, `answer36`, `answer37`, `answer38`, `answer39`, `answer40`, `date_posted`, `quiz_id`, `user_id`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 19:29:19', 3, 1),
(2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 19:55:48', 4, 1),
(3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:08:59', 5, 1),
(4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:39:52', 6, 1),
(5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:52:23', 5, 1),
(6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:52:26', 4, 1),
(7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:55:46', 7, 1),
(8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 20:56:09', 6, 1),
(9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 21:18:21', 7, 1),
(10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 21:18:35', 4, 1),
(11, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 21:18:38', 6, 1),
(12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 21:45:30', 4, 1),
(13, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 21:45:34', 6, 1),
(14, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 22:01:28', 4, 1),
(15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 22:01:31', 6, 1),
(16, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 22:02:32', 10, 1),
(17, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-09 22:03:17', 2, 1),
(18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-10 01:39:42', 2, 1),
(19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 00:09:59', 11, 1),
(20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:54:41', 3, 6),
(21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:54:45', 10, 6),
(22, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:54:48', 7, 6),
(23, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:54:51', 4, 6),
(24, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:55:03', 5, 6),
(25, '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-01-11 17:55:10', 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `quiz_answers_type`
--

DROP TABLE IF EXISTS `quiz_answers_type`;
CREATE TABLE IF NOT EXISTS `quiz_answers_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `texts` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quiz_answers_type`
--

INSERT INTO `quiz_answers_type` (`id`, `texts`) VALUES
(1, 'Answer 01'),
(2, 'Answer 02'),
(3, 'Answer 03'),
(4, 'Answer 04');

-- --------------------------------------------------------

--
-- Table structure for table `speaking`
--

DROP TABLE IF EXISTS `speaking`;
CREATE TABLE IF NOT EXISTS `speaking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) NOT NULL,
  `question_01` varchar(500) NOT NULL,
  `question_02` varchar(500) NOT NULL,
  `question_03` varchar(500) NOT NULL,
  `question_04` varchar(500) NOT NULL,
  `question_05` varchar(500) NOT NULL,
  `date_posted` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `speaking`
--

INSERT INTO `speaking` (`id`, `title`, `question_01`, `question_02`, `question_03`, `question_04`, `question_05`, `date_posted`, `user_id`) VALUES
(1, 'Your friends', '76e8a05e0902f8c8.mp3', 'c7c0edc4698afd72.mp3', '1496da38b785949d.mp3', '1fe5dd9db552d22e.mp3', '51dfc2a57a4166de.mp3', '2021-01-09 17:36:21', 1),
(2, 'Cold weather', '5c06065c8d3b4f8a.mp3', '0ba3bc0ad9c885d8.mp3', 'd7ae1c97abe89c6a.mp3', '196ac6f7f6d49681.mp3', 'f4fcc74af6a8ef92.mp3', '2021-01-09 18:37:20', 1);

-- --------------------------------------------------------

--
-- Table structure for table `speakinganswer`
--

DROP TABLE IF EXISTS `speakinganswer`;
CREATE TABLE IF NOT EXISTS `speakinganswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `answer01` varchar(500) DEFAULT NULL,
  `answer02` varchar(500) DEFAULT NULL,
  `answer03` varchar(500) DEFAULT NULL,
  `answer04` varchar(500) DEFAULT NULL,
  `answer05` varchar(500) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `speakinganswer`
--

INSERT INTO `speakinganswer` (`id`, `pid`, `answer01`, `answer02`, `answer03`, `answer04`, `answer05`, `date_posted`, `user_id`) VALUES
(1, 1, NULL, NULL, NULL, NULL, NULL, '2021-01-09 17:57:09', 1),
(2, 1, 'who is this and I just wanted to make sure that you are ok you are safe in hands and love to see you in a good way and I hope you make a hook', 'so how are you doing tonight and I like to speak up with me and the buffet everything you did today and most likely to you for you to do tomorrow I am just chill in our here and', 'so what are the things that you look in forward India future and what would be the outcome that you have to send for after this and what are the different nations things that you have done in this time of period and what', 'Piya Milan what are you going to do in so-called future and what are you programming like me you like this use and but you know about linked list and queues and', 'Anda Hai recording Banu V just according to see whether it\'s going to work with windows store in the database and database going to give me a good feedback is going to say when we can see the result of the', '2021-01-09 18:55:08', 1),
(3, 1, 'phone to nice want you to know that I have to go through', NULL, NULL, NULL, NULL, '2021-01-09 19:16:05', 1),
(4, 2, 'I have been in very cold weather about few days ago in Dubai but Dubai is also one of the coldest place on earth', 'why do we mostly have moderate the cold weather and the winter season runs from November to March November and December have weather why January February usually', 'so insulin ka the most cold cold place on the Sri Lanka Buddhi Badi area so if you go to that place there will be Hills and mountains as well so that occurs hun', 'I like to live in a hot place rather than cold place but I like a climate Vineet rain so usually because I will it rain like the dust will go off and like it', 'so if I were in the cold weather like let\'s say we were in uranium so if I catch a cold in that place by would rather on the steam on me like I would take a doll', '2021-01-09 21:19:20', 1),
(5, 2, 'once I have travelled to Canada that is in December and it was very cold and it was like I can\'t breathe right now Malik like in Sri Lanka so it was very very cold', 'Mumbai countries not a very cold country so it is more likely hot country and like the lender it start raining and most like the least like it is like a country like rain and', 'bigul sound there is a place that is more likely to be a sort of cold place in the hill country but in other places like where I live would be a very cold place', 'I need to look hot place more than Cold Place because I like I used to the hot weather and the not used to the cold weather like how to steam yourself how to wear dresses and all and like we start sweating and we know we have to clean all but', 'I took this exam to check whether the testing part is accurately correct and do it happen without any spelling errors but it is have some spelling errors apparently so we have to develop in a way that it going', '2021-01-09 22:00:22', 1),
(6, 2, NULL, NULL, NULL, NULL, NULL, '2021-01-11 13:12:39', 1),
(7, 1, NULL, NULL, 'understand that school was done and he was a great friend and today it taught me how to save great when we are in trouble he has a great impact on my life in humans in Australia now we regularly communicate via Sky I specifically like him because he was more alive', NULL, NULL, '2021-01-11 16:36:00', 1),
(8, 1, 'I have more than 10 friends and I am not sure if I should say this is many! However, I had more than 30 friends in my school days. With the passage of the time, the number plummeted. If I count my Facebook friends as real friends, the number would go high!', 'I meet my friends almost twice a week. I love to spend my weekends with them and sometimes I visit different places, watch movies and discuss different topics with them. I do not go out with all of my friends. I mostly hang out with 2-3 close buddies and go out with them almost 3-4 times a month.', 'Tata school bus stand and he was a great friend she was tall and today it taught me how to circuit when we are in trouble he has a great impact on my life than humans in Australia now we regularly communicate vs guy I specifically like him because he was more like a brother', ' I must say I am quite lucky to have good neighbours who are always supportive and well-behaved. I am quite close to them. We have been living in our neighbourhood for more than a decade and our neighbours have become our close relatives. We have a mutual understanding and an invisible bond that ties us together as good neighbours. I respect their opinion, privacy and try to step forward whenever they need me.   ', ' To be honest, family comes first. However, there are some friends who become our family members. The bond between family members is often stronger but this does not mean that we do not have friends who are less important in our life. Being with the family makes us who we really are and friends make our life worth living. ', '2021-01-11 17:45:10', 6);

-- --------------------------------------------------------

--
-- Table structure for table `speakinganswersaved`
--

DROP TABLE IF EXISTS `speakinganswersaved`;
CREATE TABLE IF NOT EXISTS `speakinganswersaved` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `answer01` varchar(500) NOT NULL,
  `cohesion_01` int(11) DEFAULT NULL,
  `grammar_01` int(11) DEFAULT NULL,
  `answer02` varchar(500) NOT NULL,
  `cohesion_02` int(11) DEFAULT NULL,
  `grammar_02` int(11) DEFAULT NULL,
  `answer03` varchar(500) NOT NULL,
  `cohesion_03` int(11) DEFAULT NULL,
  `grammar_03` int(11) DEFAULT NULL,
  `answer04` varchar(500) NOT NULL,
  `cohesion_04` int(11) DEFAULT NULL,
  `grammar_04` int(11) DEFAULT NULL,
  `answer05` varchar(500) NOT NULL,
  `cohesion_05` int(11) DEFAULT NULL,
  `grammar_05` int(11) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `speakinganswersaved`
--

INSERT INTO `speakinganswersaved` (`id`, `pid`, `answer01`, `cohesion_01`, `grammar_01`, `answer02`, `cohesion_02`, `grammar_02`, `answer03`, `cohesion_03`, `grammar_03`, `answer04`, `cohesion_04`, `grammar_04`, `answer05`, `cohesion_05`, `grammar_05`, `date_posted`, `user_id`) VALUES
(1, 1, 'Haridwar ki dress all the pictures in the format and it is my lovely to be with you and all the time you work with me and I am so happy to be with me the person that you are', 6, 23, 'so how are you doing tonight and I like to speak up with me and the buffet everything you did today and most likely to you for you to do tomorrow I am just chill in our here and', 13, -1, 'so what are the things that you look in forward India future and what would be the outcome that you have to send for after this and what are the different nations things that you have done in this time of period and what', 13, -23, 'Piya Milan what are you going to do in so-called future and what are you programming like me you like this use and but you know about linked list and queues and', 6, -21, 'Anda Hai recording Banu V just according to see whether it\'s going to work with windows store in the database and database going to give me a good feedback is going to say when we can see the result of the', 6, -20, '2021-01-09 18:59:29', 1),
(2, 2, 'I have been in very cold weather about few days ago in Dubai but Dubai is also one of the coldest place on earth', 13, 21, 'why do we mostly have moderate the cold weather and the winter season runs from November to March November and December have weather why January February usually', 13, 24, 'so insulin ka the most cold cold place on the Sri Lanka Buddhi Badi area so if you go to that place there will be Hills and mountains as well so that occurs hun', 19, 16, 'I like to live in a hot place rather than cold place but I like a climate Vineet rain so usually because I will it rain like the dust will go off and like it', 19, 5, 'so if I were in the cold weather like let\'s say we were in uranium so if I catch a cold in that place by would rather on the steam on me like I would take a doll', 19, 20, '2021-01-09 21:45:11', 1),
(3, 2, 'once I have travelled to Canada that is in December and it was very cold and it was like I can\'t breathe right now Malik like in Sri Lanka so it was very very cold', 13, 28, 'Mumbai countries not a very cold country so it is more likely hot country and like the lender it start raining and most like the least like it is like a country like rain and', 13, 1, 'bigul sound there is a place that is more likely to be a sort of cold place in the hill country but in other places like where I live would be a very cold place', 13, 23, 'I need to look hot place more than Cold Place because I like I used to the hot weather and the not used to the cold weather like how to steam yourself how to wear dresses and all and like we start sweating and we know we have to clean all but', 13, 12, 'I took this exam to check whether the testing part is accurately correct and do it happen without any spelling errors but it is have some spelling errors apparently so we have to develop in a way that it going', 6, 6, '2021-01-09 22:01:16', 1),
(4, 1, 'I have more than 10 friends and I am not sure if I should say this is many! However, I had more than 30 friends in my school days. With the passage of the time, the number plummeted. If I count my Facebook friends as real friends, the number would go high!', 8, 14, 'I meet my friends almost twice a week. I love to spend my weekends with them and sometimes I visit different places, watch movies and discuss different topics with them. I do not go out with all of my friends. I mostly hang out with 2-3 close buddies and go out with them almost 3-4 times a month.', 3, 11, 'Tata school bus stand and he was a great friend she was tall and today it taught me how to circuit when we are in trouble he has a great impact on my life than humans in Australia now we regularly communicate vs guy I specifically like him because he was more like a brother', 6, -1, ' I must say I am quite lucky to have good neighbours who are always supportive and well-behaved. I am quite close to them. We have been living in our neighbourhood for more than a decade and our neighbours have become our close relatives. We have a mutual understanding and an invisible bond that ties us together as good neighbours. I respect their opinion, privacy and try to step forward whenever they need me.   ', 10, 10, ' To be honest, family comes first. However, there are some friends who become our family members. The bond between family members is often stronger but this does not mean that we do not have friends who are less important in our life. Being with the family makes us who we really are and friends make our life worth living. ', 9, 12, '2021-01-11 17:54:02', 6);

-- --------------------------------------------------------

--
-- Table structure for table `speakingquestion`
--

DROP TABLE IF EXISTS `speakingquestion`;
CREATE TABLE IF NOT EXISTS `speakingquestion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) NOT NULL,
  `question_01` varchar(500) NOT NULL,
  `question_02` varchar(500) NOT NULL,
  `question_03` varchar(500) NOT NULL,
  `question_04` varchar(500) NOT NULL,
  `question_05` varchar(500) NOT NULL,
  `date_posted` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `speakingquestion`
--

INSERT INTO `speakingquestion` (`id`, `title`, `question_01`, `question_02`, `question_03`, `question_04`, `question_05`, `date_posted`, `user_id`) VALUES
(1, 'Your friends', 'Do you prefer to have one particular friend or a group of friends? [Why?]', 'What do you like doing most with your friend/s?', 'Do you think it’s important to keep in contact with friends you knew as a child? [Why/Why not?]', 'What makes a friend into a good friend?', 'What are the qualities you see on friend?', '2021-01-09 17:36:21', 1),
(2, 'Cold weather', 'Have you ever been in very cold weather? [When?]', 'How often is the weather cold where you come from?', 'Are some parts of your country colder than others? [Why?]', 'Would you prefer to live in a hot place or a cold place? [Why?]', 'What you will do if you catch a cold when you in cold weather?', '2021-01-09 18:37:20', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(80) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `image_file` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `firstname`, `lastname`, `username`, `email`, `password`, `is_admin`, `image_file`) VALUES
(1, 'Jeffery', 'White', 'Jeffery White', 'jefferybevan@gmail.com', '$2b$12$zRyk6PPih47icgaZAQbmkep2fJ0VdPHNOrXeFN7SZLGQBEnniuoHq', 1, 'default.jpg'),
(2, 'sth', 'divyanjala', 'stheshan', 'stheshan4@gmail.com', '$2b$12$s1OLGkh.JO9TLc1f.VBPgOl7MC7zLuBygy1rKDBwQGgMrcCExM2.m', 0, 'default.jpg'),
(3, 'sthd', 'asd', 'asdasd', 'st@gmail.com', '$2b$12$M9s84J2.vgO/sUCurWGGXelk3hO5WUP.hWfTbpR6dDXC1rdrbheWq', 0, 'default.jpg'),
(4, 'Sehani', 'Senevirathne', 'IT17127042', 'sapnasehani@gmail.com', '$2b$12$/VaPXZ9Ff5tRLnxdRRv8jOFGrfKPZ43syT3XvuqysZVMD48LE/9OS', 0, 'default.jpg'),
(5, 'Sehani', 'Senevirathne', 'IT17127042_S', 'sapshe@gmail.com', '$2b$12$cJt4dMaKXHZ3DEX3zAbBh.3W1B1G0e9kkVbUvosOVQfh9N.BOTaai', 0, 'default.jpg'),
(6, 'Jeffery', 'White', 'Jeffery IT17158350', 'jeffery1996.jbw@gmail.com', '$2b$12$Rx.igZxa1rOblCYmgc4ZzO2vCaEswJSxouRiCQA3/TjGCvLz32zL6', 0, 'default.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `writingpaper`
--

DROP TABLE IF EXISTS `writingpaper`;
CREATE TABLE IF NOT EXISTS `writingpaper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) NOT NULL,
  `task01` varchar(1000) NOT NULL,
  `task01_img` varchar(20) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `writingpaper`
--

INSERT INTO `writingpaper` (`id`, `title`, `task01`, `task01_img`, `date_posted`, `user_id`) VALUES
(1, 'IELTS Writing Task 1 - Graph Paper', 'You should spend about 20 minutes on this task.\r\nWrite at least 150 words.\r\nThe graph below shows the consumption of 3 spreads from 1981 to 2007. Write a report for a university lecturer describing the information given.\r\n', '01e485d29dc3f584.PNG', '2021-01-10 21:52:25', 1);

-- --------------------------------------------------------

--
-- Table structure for table `writingpaperanswer`
--

DROP TABLE IF EXISTS `writingpaperanswer`;
CREATE TABLE IF NOT EXISTS `writingpaperanswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `task` text NOT NULL,
  `type` varchar(200) NOT NULL,
  `date_posted` datetime NOT NULL,
  `grammar` int(11) NOT NULL,
  `cohesion` int(11) NOT NULL,
  `similarity` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `writingpaperanswer`
--

INSERT INTO `writingpaperanswer` (`id`, `pid`, `task`, `type`, `date_posted`, `grammar`, `cohesion`, `similarity`, `user_id`) VALUES
(1, 1, 'The line graph illustrates the amount of three kinds of spreads (margarine, low fat and reduced spreads and butter) which were consumed over 26 years from 1981 to 2007. Units are measured in grams.\r\nOverall, the consumption of margarine and butter decreased over the period given, while for low fat and reduced spreads, it rose. At the start of the period, butter was the most popular spread, which was replaced by margarine from 1991 to 2001, and following that low fat and reduced spreads became the most widely used spread in the final years.\r\nWith regards to the amount of butter used, it began at around 140 grams and then peaked at 160   grams in 1986 before falling dramatically to about 50 grams in the last year. Likewise, approximately 90 grams of margarine was eaten in the first year after which the figure fluctuated slightly and dropped to a low of 40 grams in 2007.\r\nOn the other hand, the consumption of low fats and reduced spreads only started in 1996 at about 10 grams. This figure, which reached a high of just cover 80grams 5 years later, fell stightly in the final years to approximately 70 grams in 2007.\r\n', 'type1', '2021-01-10 21:52:25', 16, 9, 100, 5),
(2, 1, 'Color Picker\r\nClick on the image to get the html codes..\r\n\r\nUse the online image color picker above to select a color and get the HTML Color Code of this pixel. Also you get the HEX color code value, RGB value and HSV value. You can put a picture url in the textbox below or upload your own image. (for example an screenshot of your desktop). Or use an website url, you will see a thumbnail on the right side.\r\n\r\n\r\nColor Picker\r\nClick on the image to get the html codes..\r\n\r\nUse the online image color picker above to select a color and get the HTML Color Code of this pixel. Also you get the HEX color code value, RGB value and HSV value. You can put a picture url in the textbox below or upload your own image. (for example an screenshot of your desktop). Or use an website url, you will see a thumbnail on the right side.\r\n\r\n\r\n\r\nColor Picker\r\nClick on the image to get the html codes..\r\n\r\nUse the online image color picker above to select a color and get the HTML Color Code of this pixel. Also you get the HEX color code value, RGB value and HSV value. You can put a picture url in the textbox below or upload your own image. (for example an screenshot of your desktop). Or use an website url, you will see a thumbnail on the right side.\r\n\r\n\r\n\r\n\r\nColor Picker\r\nClick on the image to get the html codes..\r\n\r\nUse the online image color picker above to select a color and get the HTML Color Code of this pixel. Also you get the HEX color code value, RGB value and HSV value. You can put a picture url in the textbox below or upload your own image. (for example an screenshot of your desktop). Or use an website url, you will see a thumbnail on the right side.', 'type1', '2021-01-11 09:10:30', 22, 8, 13, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
