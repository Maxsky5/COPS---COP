from entitiesRepository.CheckRepository import CheckRepository
from entities.Offender import Offender
from entities.Cop import Cop
from entities.Lesson import Lesson
from entities.Classroom import Classroom
from entities.Grade import Grade
from dao.ConnectDb import ConnectDb

class ObjectFormater:
    def __init__(self, name):
        print("ObjectFormater init")

    # Retourne une liste d'objets Offenders ou un objet Offender
    def OffendersToObjects(self, offendersList):
        offenders = []
        if type(offendersList) is dict:
            offendersList = [offendersList]
        for offenderList in offendersList:
            grade=None
            if offenderList['grade'] is not None:
                grade = self.GradesToObjects(offenderList['grade'])
            offenders.append(
                Offender(
                    id=offenderList['id'],
                    firstname=offenderList['firstname'],
                    lastname=offenderList['lastname'],
                    email=offenderList['email'],
                    date_update=offenderList['dateUpdate'],
                    type=offenderList['type'],
                    grade=grade
                )
            )
        if len(offenders) == 1:
            return offenders[0]
        else:
            return offenders

    def GradesToObjects(self, gradesList):
        grades = []
        if type(gradesList) is dict:
            gradesList = [gradesList]
        for gradeList in gradesList:

            grades.append(
                Grade(
                    id=gradeList['id'],
                    name=gradeList['name'],
                    date_start=gradeList['dateStart'],
                    date_end=gradeList['dateEnd'],
                    date_update=gradeList['dateUpdate']
                )
            )
        if len(grades) == 1:
            return grades[0]
        else:
            return grades

    def CopsToObjects(self, copsList):
        cops = []
        for copList in copsList:
            classroom = None
            if copList['classroom'] is not None:
                classroom = self.ClassroomsToObjects(copList['classroom'])
            cops.append(
                Cop(
                    id=copList['id'],
                    name=copList['name'],
                    mac_address=copList['macAddress'],
                    date_update=copList['dateUpdate'],
                    date_last_sync=copList['dateLastSync'],
                    classroom=classroom
                )
            )
        if len(cops) == 1:
            return cops[0]
        else:
            return cops

    def LessonsToObjects(self, lessonsList):
        lessons = []
        for lessonList in lessonsList:
            teacher = None
            classroom = None
            grades = []
            if lessonList['teacher'] is not None:
                teacher = self.OffendersToObjects(lessonList['teacher'])
            if lessonList['classroom'] is not None:
                classroom = self.ClassroomsToObjects(lessonList['classroom'])
            if lessonList['grades'] is not None:
                grades = self.GradesToObjects(lessonList['grades'])
            lessons.append(
                Lesson(
                    id=lessonList['id'],
                    name=lessonList['name'],
                    is_morning=lessonList['isMorning'],
                    date_update=lessonList['dateUpdate'],
                    date=lessonList['dateLesson'],
                    offender=teacher,
                    classroom=classroom
                )
            )
        if len(lessons) == 1:
            return lessons[0]
        else:
            return lessons

    def ClassroomsToObjects(self, classroomsList):
        classrooms = []
        if type(classroomsList) is dict:
            classroomsList = [classroomsList]
        for classroomList in classroomsList:
            classrooms.append(
                Classroom(
                    id=classroomList['id'],
                    name=classroomList['name'],
                    nb_place=classroomList['nbPlace'],
                    date_update=classroomList['dateUpdate']
                )
            )
        if len(classrooms) == 1:
            return classrooms[0]
        else:
            return classrooms