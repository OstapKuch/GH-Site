USE [master]
GO

/****** Object:  Database [Project Renting car]    Script Date: 05.08.2017 20:27:51 ******/
CREATE DATABASE [Project Renting car]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Project Renting car', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Project Renting car.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Project Renting car_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Project Renting car_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO

ALTER DATABASE [Project Renting car] SET COMPATIBILITY_LEVEL = 130
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Project Renting car].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Project Renting car] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Project Renting car] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Project Renting car] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Project Renting car] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Project Renting car] SET ARITHABORT OFF 
GO

ALTER DATABASE [Project Renting car] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Project Renting car] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Project Renting car] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Project Renting car] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Project Renting car] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Project Renting car] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Project Renting car] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Project Renting car] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Project Renting car] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Project Renting car] SET  DISABLE_BROKER 
GO

ALTER DATABASE [Project Renting car] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Project Renting car] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Project Renting car] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Project Renting car] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Project Renting car] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Project Renting car] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Project Renting car] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Project Renting car] SET RECOVERY FULL 
GO

ALTER DATABASE [Project Renting car] SET  MULTI_USER 
GO

ALTER DATABASE [Project Renting car] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Project Renting car] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Project Renting car] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Project Renting car] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Project Renting car] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Project Renting car] SET QUERY_STORE = OFF
GO

USE [Project Renting car]
GO

ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO

ALTER DATABASE [Project Renting car] SET  READ_WRITE 
GO

