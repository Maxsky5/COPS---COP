-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dbcops
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dbcops` ;

-- -----------------------------------------------------
-- Schema dbcops
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbcops` DEFAULT CHARACTER SET utf8mb4 ;
USE `dbcops` ;

-- -----------------------------------------------------
-- Table `dbcops`.`classrooms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`classrooms` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`classrooms` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `nb_place` INT(11) NOT NULL DEFAULT '0',
  `date_update` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dbcops`.`cops`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`cops` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`cops` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `classroom_id` INT(11) NOT NULL,
  `date_update` DATETIME NOT NULL,
  `date_last_sync` DATETIME NOT NULL,
  `mac_address` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cop_classroom_id_idx` (`classroom_id` ASC),
  CONSTRAINT `fk_cop_classroom_id`
    FOREIGN KEY (`classroom_id`)
    REFERENCES `dbcops`.`classrooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dbcops`.`grades`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`grades` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`grades` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `date_start` DATETIME NOT NULL,
  `date_end` DATETIME NOT NULL,
  `date_update` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dbcops`.`offenders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`offenders` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`offenders` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `grade_id` INT(11) NULL,
  `date_update` DATETIME NOT NULL,
  `type` ENUM('teacher', 'student') NOT NULL DEFAULT 'student',
  PRIMARY KEY (`id`),
  INDEX `fk_offender_grade_id_idx` (`grade_id` ASC),
  CONSTRAINT `fk_offender_grade_id`
    FOREIGN KEY (`grade_id`)
    REFERENCES `dbcops`.`grades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dbcops`.`checks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`checks` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`checks` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `offender_id` INT(11) NOT NULL,
  `cop_id` INT(11) NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_check_student_id_idx` (`offender_id` ASC),
  INDEX `fk_check_cop_id_idx` (`cop_id` ASC),
  CONSTRAINT `fk_check_cop_id`
    FOREIGN KEY (`cop_id`)
    REFERENCES `dbcops`.`cops` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_check_student_id`
    FOREIGN KEY (`offender_id`)
    REFERENCES `dbcops`.`offenders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dbcops`.`lessons`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`lessons` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`lessons` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` INT(11) NULL DEFAULT NULL,
  `classroom_id` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `is_morning` TINYINT(1) NOT NULL,
  `date_update` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_lesson_day` (`date` ASC, `is_morning` ASC),
  INDEX `fk_lesson_classrom_id_idx` (`classroom_id` ASC),
  INDEX `fk_lesson_teacher_id_idx` (`teacher_id` ASC),
  CONSTRAINT `fk_lesson_teacher_id`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `dbcops`.`offenders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_lesson_classrom_id`
    FOREIGN KEY (`classroom_id`)
    REFERENCES `dbcops`.`classrooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dbcops`.`lessons_grades`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`lessons_grades` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`lessons_grades` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lesson_id` INT NOT NULL,
  `grade_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_lessons_idx` (`lesson_id` ASC),
  INDEX `fk_grades_idx` (`grade_id` ASC),
  CONSTRAINT `fk_grades_idx`
    FOREIGN KEY (`grade_id`)
    REFERENCES `dbcops`.`grades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_lessons_idx`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `dbcops`.`lessons` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbcops`.`lessons_grades`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbcops`.`lessons_grades` ;

CREATE TABLE IF NOT EXISTS `dbcops`.`lessons_grades` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lesson_id` INT NOT NULL,
  `grade_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_lessons_idx` (`lesson_id` ASC),
  INDEX `fk_grades_idx` (`grade_id` ASC),
  CONSTRAINT `fk_grades_idx`
    FOREIGN KEY (`grade_id`)
    REFERENCES `dbcops`.`grades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_lessons_idx`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `dbcops`.`lessons` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
