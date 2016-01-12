-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cops
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cops
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cops` DEFAULT CHARACTER SET utf8mb4 ;
USE `cops` ;

-- -----------------------------------------------------
-- Table `cops`.`classrooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`classrooms` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `nb_place` INT(11) NOT NULL DEFAULT '0',
  `date_update` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cops`.`cops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`cops` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET 'utf8mb4' NOT NULL,
  `classroom_id` INT(11) NULL DEFAULT NULL,
  `date_update` DATETIME NOT NULL,
  `date_last_sync` DATETIME NOT NULL,
  `mac_address` VARCHAR(45) CHARACTER SET 'utf8mb4' NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cop_classroom_id_idx` (`classroom_id` ASC),
  CONSTRAINT `fk_cop_classroom_id`
    FOREIGN KEY (`classroom_id`)
    REFERENCES `cops`.`classrooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `cops`.`grades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`grades` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `date_start` DATETIME NOT NULL,
  `date_end` DATETIME NOT NULL,
  `date_update` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cops`.`offenders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`offenders` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `grade_id` INT(11) NULL DEFAULT NULL,
  `date_update` DATETIME NOT NULL,
  `type` ENUM('TEACHER', 'STUDENT') NOT NULL DEFAULT 'STUDENT',
  PRIMARY KEY (`id`),
  INDEX `fk_offender_grade_id_idx` (`grade_id` ASC),
  CONSTRAINT `fk_offender_grade_id`
    FOREIGN KEY (`grade_id`)
    REFERENCES `cops`.`grades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `cops`.`checks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`checks` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `offender_id` INT(11) NOT NULL,
  `cop_id` INT(11) NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_check_student_id_idx` (`offender_id` ASC),
  INDEX `fk_check_cop_id_idx` (`cop_id` ASC),
  CONSTRAINT `fk_check_cop_id`
    FOREIGN KEY (`cop_id`)
    REFERENCES `cops`.`cops` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_check_student_id`
    FOREIGN KEY (`offender_id`)
    REFERENCES `cops`.`offenders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cops`.`lessons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`lessons` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` INT(11) NULL DEFAULT NULL,
  `classroom_id` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `is_morning` TINYINT(1) NOT NULL,
  `date_update` DATETIME NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_lesson_day` (`date` ASC, `is_morning` ASC),
  INDEX `fk_lesson_classrom_id_idx` (`classroom_id` ASC),
  INDEX `fk_lesson_teacher_id_idx` (`teacher_id` ASC),
  CONSTRAINT `fk_lesson_classrom_id`
    FOREIGN KEY (`classroom_id`)
    REFERENCES `cops`.`classrooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_lesson_teacher_id`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `cops`.`offenders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cops`.`lessons_grades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cops`.`lessons_grades` (
  `lesson_id` INT(11) NOT NULL,
  `grade_id` INT(11) NOT NULL,
  PRIMARY KEY (`lesson_id`, `grade_id`),
  INDEX `fk_lessons_idx` (`lesson_id` ASC),
  INDEX `fk_grades_idx` (`grade_id` ASC),
  CONSTRAINT `fk_grades_idx`
    FOREIGN KEY (`grade_id`)
    REFERENCES `cops`.`grades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_lessons_idx`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `cops`.`lessons` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
