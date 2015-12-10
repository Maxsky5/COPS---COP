# -*-coding: utf-8-*-
from entities import entities
import time
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine


# Add some records in all tables
class Fixture:

    def __init__(self, name):
        self.deleteRecords()
        self.addRecords()


    def deleteRecords(self):

        # connexion base
        engine = create_engine('mysql://root:@localhost:3306/dbcops', echo=True)
        Session = sessionmaker(bind=engine.engine)
        session = Session()

        session.query(entities.Lesson_grade).delete()
        session.query(entities.Lesson).delete()
        session.query(entities.Check).delete()
        session.query(entities.Offender).delete()
        session.query(entities.Cop).delete()

        session.query(entities.Classroom).delete()
        session.query(entities.Grade).delete()

        session.commit()

    # Create some recording
    def addRecords(self):

        # connexion db
        engine = create_engine('mysql://root:@localhost:3306/dbcops', echo=True)
        Session = sessionmaker(bind=engine.engine)
        session = Session()

        # checks
        check1 = entities.Check(date=time.strftime("%Y%m%d"))

        # offenders
        thomas = entities.Offender(firstname='thomas', lastname='peyrou', email='thomaspeyrou@gmail.com', date_update=time.strftime("%Y%m%d"), type=2)
        maxime = entities.Offender(firstname='maxime', lastname='ribera', email='', date_update=time.strftime("%Y%m%d"), type=2)
        arthur = entities.Offender(firstname='arthur', lastname='sore', email='', date_update=time.strftime("%Y%m%d"), type=2)
        adam = entities.Offender(firstname='adam', lastname='dief', email='', date_update=time.strftime("%Y%m%d"), type=2)
        gerard = entities.Offender(firstname='gerard', lastname='bboulet', email='jesuce@yopmail.com', date_update=time.strftime("%Y%m%d"), type=2)
        stephan = entities.Offender(firstname='stephan', lastname='amet', email='', date_update=time.strftime("%Y%m%d"), type=1)
        pere_fourasse = entities.Offender(firstname='jeanpaul', lastname='fourasse', email='', date_update=time.strftime("%Y%m%d"), type=1)

        # grades
        ril_grade = entities.Grade(name="ril", date_start='20140901', date_end='20160901', date_update=time.strftime("%Y%m%d"))
        rar_grade = entities.Grade(name="rar", date_start='20140901', date_end='20160901', date_update=time.strftime("%Y%m%d"))

        # Cops
        cop_1 = entities.Cop(name='Cop001', date_update=time.strftime("%Y%m%d"), date_last_sync=time.strftime("%Y%m%d"), mac_address='00:00:00:00:00:00')
        cop_2 = entities.Cop(name='Cop002', date_update=time.strftime("%Y%m%d"), date_last_sync=time.strftime("%Y%m%d"), mac_address='11:11:11:11:11:11')

        # Lessons
        lesson_soulac = entities.Lesson(date=time.strftime("%Y%m%d"), is_morning=0, date_update=time.strftime("%Y%m%d"))
        lesson_brive = entities.Lesson(date=time.strftime("%Y%m%d"), is_morning=1, date_update=time.strftime("%Y%m%d"))

        # Classrooms & Add lesson
        soulac_classroom = entities.Classroom(name='soulac', nb_place=20, lesson=lesson_soulac)
        brive_classroom = entities.Classroom(name='brive', nb_place=20, lesson=lesson_brive)

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
        lesson_ril = entities.Lesson_grade(lesson=lesson_soulac, grade=ril_grade)
        lesson_rar = entities.Lesson_grade(lesson=lesson_brive, grade=rar_grade)

        session.add_all([lesson_ril])
        session.add_all([lesson_rar])
        session.commit()

        return "Record added !"