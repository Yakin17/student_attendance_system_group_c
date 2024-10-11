-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 11, 2024 at 12:16 PM
-- Server version: 8.0.31
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_attendance_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add course', 7, 'add_course'),
(26, 'Can change course', 7, 'change_course'),
(27, 'Can delete course', 7, 'delete_course'),
(28, 'Can view course', 7, 'view_course'),
(29, 'Can add subjects', 8, 'add_subjects'),
(30, 'Can change subjects', 8, 'change_subjects'),
(31, 'Can delete subjects', 8, 'delete_subjects'),
(32, 'Can view subjects', 8, 'view_subjects'),
(33, 'Can add student', 9, 'add_student'),
(34, 'Can change student', 9, 'change_student'),
(35, 'Can delete student', 9, 'delete_student'),
(36, 'Can view student', 9, 'view_student'),
(37, 'Can add faculty member', 10, 'add_facultymember'),
(38, 'Can change faculty member', 10, 'change_facultymember'),
(39, 'Can delete faculty member', 10, 'delete_facultymember'),
(40, 'Can view faculty member', 10, 'view_facultymember'),
(41, 'Can add attendance', 11, 'add_attendance'),
(42, 'Can change attendance', 11, 'change_attendance'),
(43, 'Can delete attendance', 11, 'delete_attendance'),
(44, 'Can view attendance', 11, 'view_attendance'),
(45, 'Can add admin', 12, 'add_admin'),
(46, 'Can change admin', 12, 'change_admin'),
(47, 'Can delete admin', 12, 'delete_admin'),
(48, 'Can view admin', 12, 'view_admin');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'stud_att_management_app', 'customuser'),
(7, 'stud_att_management_app', 'course'),
(8, 'stud_att_management_app', 'subjects'),
(9, 'stud_att_management_app', 'student'),
(10, 'stud_att_management_app', 'facultymember'),
(11, 'stud_att_management_app', 'attendance'),
(12, 'stud_att_management_app', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-09 15:33:31.315495'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-10-09 15:33:31.424805'),
(3, 'auth', '0001_initial', '2024-10-09 15:33:31.831023'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-10-09 15:33:31.893540'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-10-09 15:33:31.893540'),
(6, 'auth', '0004_alter_user_username_opts', '2024-10-09 15:33:31.909143'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-10-09 15:33:31.909143'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-10-09 15:33:31.909143'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-10-09 15:33:31.924789'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-10-09 15:33:31.924789'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-10-09 15:33:31.924789'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-10-09 15:33:31.987262'),
(13, 'auth', '0011_update_proxy_permissions', '2024-10-09 15:33:31.987262'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-10-09 15:33:32.002887'),
(15, 'stud_att_management_app', '0001_initial', '2024-10-09 15:33:33.299674'),
(16, 'admin', '0001_initial', '2024-10-09 15:33:33.612153'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-10-09 15:33:33.627776'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-09 15:33:33.627776'),
(19, 'sessions', '0001_initial', '2024-10-09 15:33:33.690271');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('33c5qeufaeil6ru88oobkqs7iz4h2nyt', '.eJxVjMsOwiAQRf-FtSHAwNC6dO83kOExtmogKe3K-O_apAvd3nPOfYlA2zqFrZclzFmchRan3y1SepS6g3ynemsytbouc5S7Ig_a5bXl8rwc7t_BRH361qg0WcLkNKoBE3J2ioyyRM5aA0YzjwCcCwOTh6wBE4zooxssD57E-wPLAjdq:1szDLo:-Ourg315yDSe-3F_SccT4Y0pDy8AnA8zWf7rmvYTzB0', '2024-10-25 10:58:28.475594');

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_admin`
--

DROP TABLE IF EXISTS `stud_att_management_app_admin`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_admin`
--

INSERT INTO `stud_att_management_app_admin` (`id`, `created_at`, `updated_at`, `admin_id`) VALUES
(1, '2024-10-09 15:34:06.843421', '2024-10-09 15:34:06.843421', 1);

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_attendance`
--

DROP TABLE IF EXISTS `stud_att_management_app_attendance`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_attendance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `attendance_date` date NOT NULL,
  `attendance` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` bigint NOT NULL,
  `subject_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stud_att_management_app_attendance_student_id_id_829e9d73` (`student_id_id`),
  KEY `stud_att_management_app_attendance_subject_id_id_1007ac43` (`subject_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_attendance`
--

INSERT INTO `stud_att_management_app_attendance` (`id`, `attendance_date`, `attendance`, `created_at`, `updated_at`, `student_id_id`, `subject_id_id`) VALUES
(1, '2024-10-10', 'A', '2024-10-10 07:51:32.463168', '2024-10-10 07:51:32.463168', 4, 1),
(2, '2024-10-10', 'P', '2024-10-10 07:51:32.473146', '2024-10-10 07:51:32.473146', 5, 1),
(3, '2024-10-10', 'P', '2024-10-10 07:51:32.478146', '2024-10-10 07:51:32.478146', 6, 1),
(4, '2024-10-11', 'A', '2024-10-10 14:31:40.054074', '2024-10-10 14:31:40.054074', 4, 2),
(5, '2024-10-11', 'A', '2024-10-10 14:31:40.059069', '2024-10-10 14:31:40.059069', 5, 2),
(6, '2024-10-11', 'A', '2024-10-10 14:31:40.061481', '2024-10-10 14:31:40.061481', 6, 2),
(7, '2024-10-24', 'A', '2024-10-10 19:06:58.844305', '2024-10-10 19:06:58.844305', 4, 1),
(8, '2024-10-24', 'P', '2024-10-10 19:06:58.848299', '2024-10-10 19:06:58.848299', 5, 1),
(9, '2024-10-24', 'P', '2024-10-10 19:06:58.851319', '2024-10-10 19:06:58.851319', 6, 1),
(10, '2024-10-31', 'A', '2024-10-10 19:19:50.808009', '2024-10-10 19:19:50.808009', 4, 1),
(11, '2024-10-31', 'A', '2024-10-10 19:19:50.812004', '2024-10-10 19:19:50.813003', 5, 1),
(12, '2024-10-31', 'P', '2024-10-10 19:19:50.818001', '2024-10-10 19:19:50.819000', 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_course`
--

DROP TABLE IF EXISTS `stud_att_management_app_course`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_course`
--

INSERT INTO `stud_att_management_app_course` (`id`, `course_name`, `created_at`, `updated_at`) VALUES
(1, 'BAM', '2024-10-09 15:35:20.079443', '2024-10-09 15:35:20.079443'),
(2, 'BST', '2024-10-09 15:35:24.519766', '2024-10-09 15:35:24.519766');

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_customuser`
--

DROP TABLE IF EXISTS `stud_att_management_app_customuser`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_customuser`
--

INSERT INTO `stud_att_management_app_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`) VALUES
(1, 'pbkdf2_sha256$600000$JKBkRugqTSjr7E6ddmwYk9$JCUNAteGztN07nX5gUz27DmjuK9sB/UTU/WtwVrL9DY=', '2024-10-11 10:58:28.475594', 1, 'yakin', '', '', 'ishimweyakin8@gmail.com', 1, 1, '2024-10-09 15:34:06.373337', '1'),
(2, 'pbkdf2_sha256$600000$1WzeKefhWLLbTbIcKuVMg5$7y7nAhewPYkvo8XdZAm2HChr50ejlSTDmPwZ6NnWCvQ=', NULL, 0, 'teacher1', 'teacher1', 'teacher1', 'teacher@gmail.com', 0, 1, '2024-10-09 15:34:50.673517', '2'),
(3, 'pbkdf2_sha256$600000$Es6csISMyccY1494IGd5sX$yarMPgjGZVzJS4oO/3pOlPwH2qa/Q8FXauECs1ZuJj8=', '2024-10-11 10:46:06.053068', 0, 'teacher2', 'teacher2', 'teacher2', 'teacher2@gmail.com', 0, 1, '2024-10-09 15:35:07.755507', '2'),
(4, 'pbkdf2_sha256$600000$3Z8ZdnwbXtXIHd5EzMkcph$P+vrDQMFGLECv6wNTSAIJOB5zFNvbRaj8fT6yGFr6UE=', NULL, 0, 'ange', 'Ange', 'Ciramunda', 'ange@gmail.com', 0, 1, '2024-10-09 15:36:04.209179', '3'),
(5, 'pbkdf2_sha256$600000$CS5SHbgH6PktwrHLsDUzuA$zzdYlwnlIgGQzNRZYj1C+b5tfLX9zugkCNYv3VrOiUs=', NULL, 0, 'sammy', 'Sammy', 'Bucumi', 'sammy@gmail.com', 0, 1, '2024-10-09 15:36:39.276036', '3'),
(6, 'pbkdf2_sha256$600000$AcFdWU9YKUqQblCNjnO218$jggHF73YZPWnvPEqh3+her85luz7jbZI8kovTzrUgss=', '2024-10-11 10:54:51.701928', 0, 'tony', 'tony', 'Bukuru', 'tony@gmail.com', 0, 1, '2024-10-10 07:50:40.713164', '3');

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_customuser_groups`
--

DROP TABLE IF EXISTS `stud_att_management_app_customuser_groups`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stud_att_management_app__customuser_id_group_id_c57d98cc_uniq` (`customuser_id`,`group_id`),
  KEY `stud_att_management_app_customuser_groups_customuser_id_af623620` (`customuser_id`),
  KEY `stud_att_management_app_customuser_groups_group_id_69494dc0` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `stud_att_management_app_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stud_att_management_app__customuser_id_permission_f3c1357d_uniq` (`customuser_id`,`permission_id`),
  KEY `stud_att_management_app_cus_customuser_id_c5ecc094` (`customuser_id`),
  KEY `stud_att_management_app_cus_permission_id_b5eeccfe` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_facultymember`
--

DROP TABLE IF EXISTS `stud_att_management_app_facultymember`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_facultymember` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_facultymember`
--

INSERT INTO `stud_att_management_app_facultymember` (`id`, `address`, `created_at`, `updated_at`, `admin_id`) VALUES
(2, 'Kanyosha', '2024-10-09 15:35:08.356935', '2024-10-09 15:35:08.356935', 3);

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_student`
--

DROP TABLE IF EXISTS `stud_att_management_app_student`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  `course_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  KEY `stud_att_management_app_student_course_id_id_f955cc8e` (`course_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_student`
--

INSERT INTO `stud_att_management_app_student` (`id`, `gender`, `address`, `created_at`, `updated_at`, `admin_id`, `course_id_id`) VALUES
(3, 'Male', 'Gasenyi', '2024-10-10 07:50:41.946231', '2024-10-10 07:50:41.946231', 6, 2),
(2, 'Male', 'Kinanira', '2024-10-09 15:36:39.864860', '2024-10-09 15:36:39.864860', 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `stud_att_management_app_subjects`
--

DROP TABLE IF EXISTS `stud_att_management_app_subjects`;
CREATE TABLE IF NOT EXISTS `stud_att_management_app_subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `course_id_id` int NOT NULL,
  `facultymember_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stud_att_management_app_subjects_course_id_id_92b19f05` (`course_id_id`),
  KEY `stud_att_management_app_subjects_facultymember_id_id_8871540a` (`facultymember_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `stud_att_management_app_subjects`
--

INSERT INTO `stud_att_management_app_subjects` (`id`, `subject_name`, `created_at`, `updated_at`, `course_id_id`, `facultymember_id_id`) VALUES
(1, 'JavaScript', '2024-10-09 15:35:34.586692', '2024-10-09 15:35:34.586692', 2, 2),
(2, 'Entrepreneuriat', '2024-10-09 15:35:42.569652', '2024-10-09 15:35:42.569652', 1, 3),
(3, 'sciences', '2024-10-11 12:04:54.530433', '2024-10-11 12:04:54.530433', 1, 3);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
