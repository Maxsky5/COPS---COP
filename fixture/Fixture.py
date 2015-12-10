# -*-coding: utf-8-*-
from entities.Grade import Grade
from entities.Cop import Cop
from entities.Classroom import Classroom
from entities.Lesson_grade import Lesson_grade
from entities.Check import Check
from entities.Lesson import Lesson
from entities.Offender import Offender
from dao.ConnectDb import ConnectDb
import time


# Add some records in all tables
class Fixture:

    def __init__(self, name):
        self.deleteRecords()
        self.addRecords()

    def deleteRecords(self):

        # connexion base
        session = ConnectDb.session()

        session.query(Lesson_grade).delete()
        session.query(Lesson).delete()
        session.query(Check).delete()
        session.query(Offender).delete()
        session.query(Cop).delete()

        session.query(Classroom).delete()
        session.query(Grade).delete()

        session.commit()

    # Create some recording
    def addRecords(self):

        # connexion db
        session = ConnectDb.session()

        # checks
        check1 = Check(date=time.strftime("%Y%m%d"))

        # offenders
        thomas = Offender(firstname='thomas', lastname='peyrou', email='thomaspeyrou@gmail.com', date_update=time.strftime("%Y%m%d"), type=2)
        maxime = Offender(firstname='maxime', lastname='ribera', email='', date_update=time.strftime("%Y%m%d"), type=2)
        arthur = Offender(firstname='arthur', lastname='sore', email='', date_update=time.strftime("%Y%m%d"), type=2)
        adam = Offender(firstname='adam', lastname='dief', email='', date_update=time.strftime("%Y%m%d"), type=2)
        gerard = Offender(firstname='gerard', lastname='bboulet', email='jesuce@yopmail.com', date_update=time.strftime("%Y%m%d"), type=2)
        stephan = Offender(firstname='stephan', lastname='amet', email='', date_update=time.strftime("%Y%m%d"), type=1)
        pere_fourasse = Offender(firstname='jeanpaul', lastname='fourasse', email='', date_update=time.strftime("%Y%m%d"), type=1)

        # grades
        ril_grade = Grade(name="ril", date_start='20140901', date_end='20160901', date_update=time.strftime("%Y%m%d"))
        rar_grade = Grade(name="rar", date_start='20140901', date_end='20160901', date_update=time.strftime("%Y%m%d"))

        # Cops
        cop_1 = Cop(name='Cop001', date_update=time.strftime("%Y%m%d"), date_last_sync=time.strftime("%Y%m%d"), mac_address='00:00:00:00:00:00')
        cop_2 = Cop(name='Cop002', date_update=time.strftime("%Y%m%d"), date_last_sync=time.strftime("%Y%m%d"), mac_address='11:11:11:11:11:11')

        # Lessons
        lesson_soulac = Lesson(date=time.strftime("%Y%m%d"), is_morning=0, date_update=time.strftime("%Y%m%d"))
        lesson_brive = Lesson(date=time.strftime("%Y%m%d"), is_morning=1, date_update=time.strftime("%Y%m%d"))

        # Classrooms & Add lesson
        soulac_classroom = Classroom(name='soulac', nb_place=20, lesson=lesson_soulac)
        brive_classroom = Classroom(name='brive', nb_place=20, lesson=lesson_brive)

        # add offenders to grade
        ril_grade.offenders = ([thomas, maxime, arthur, adam])
        rar_grade.offenders = ([gerard])



        # add cop to classroom
        soulac_classroom.cops = [cop_1]
        brive_classroom.cops = [cop_2]

        # add lesson to offender (type teacher)
        stephan.lesson = lesson_soulac
        pere_fourasse.lesson = lesson_brive

        # add check to offencer
        thomas.check = [check1]

        # add check to cop
        cop_1.check = [check1]

        # add grade & lesson to Lesson_grade
        lesson_ril = Lesson_grade(lesson=lesson_soulac, grade=ril_grade)
        lesson_rar = Lesson_grade(lesson=lesson_brive, grade=rar_grade)

        session.add_all([lesson_ril])
        session.add_all([lesson_rar])
        session.commit()

        return "Record added !"