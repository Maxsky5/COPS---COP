# -*-coding: utf-8-*-
from requests import put, post, get
from entitiesRepository.CheckRepository import CheckRepository
from entitiesRepository.CopRepository import CopRepository
from entities.Offender import Offender
from entities.Cop import Cop
from entities.Lesson_grade import Lesson_grade
from entities.Lesson import Lesson
from entities.Classroom import Classroom
from entities.Grade import Grade
from dao.ConnectDb import ConnectDb
import json


class Synchronization:
    def __init__(self):
        data = self.getLastData()
        self.addAll(data)

    def sendDateLastSync(self):
        cop = CopRepository.getByMac('00:00:00:00:00')
        mavar1 = put('http://127.0.0.1:5000/todo1', data={'data': ""}).json

        print mavar1

    def sendCheck(self):
        checks = CheckRepository().getAll()
        jsonChecks = ChecksColl(checks).formatJson()
        print jsonChecks

        mavar1 = put('http://127.0.0.1:5000/checks', data={'data': checks}).json


    def getLastData(self):
        file = open("synchronize.json", "r")
        data = file.read()

        data = json.loads(data)
        return data

    def addAll(self, jsonData):
        s = ConnectDb.session()
        # offender
        for offender in jsonData['offenders']:
            grade=None
            if offender['grade'] is not None:
                grade = Grade(
                    id=offender['grade']['id'],
                    name=offender['grade']['name'],
                    date_start=offender['grade']['dateStart'],
                    date_end=offender['grade']['dateEnd'],
                    date_update=offender['grade']['dateUpdate']
                )
            offender1 = Offender(
                id=offender['id'],
                firstname=offender['firstname'],
                lastname=offender['lastname'],
                email=offender['email'],
                date_update=offender['dateUpdate'],
                type=offender['type']
            )
            s.add(offender1)


        # Cop
        for cop in jsonData['cops']:
            classroom=None
            if cop['classroom'] is not None:
                classroom =  Classroom(
                    id=cop['classroom']['id'],
                    name=cop['classroom']['name'],
                    nb_place=cop['classroom']['nbPlace']
                )
            cop1 = Cop(
                id=cop['id'],
                name=cop['name'],
                mac_address=cop['macAddress'],
                date_update=cop['dateUpdate'],
                date_last_sync=cop['dateLastSync'],
                classroom=classroom
            )

        # lessons
        for lesson in jsonData['lessons']:
            teacher=None
            if lesson['teacher'] is not None:
                teacher = Offender(
                    id=lesson['teacher']['id'],
                    firstname=lesson['teacher']['firstname'],
                    lastname=lesson['teacher']['lastname'],
                    email=lesson['teacher']['email'],
                    date_update=lesson['teacher']['dateUpdate'],
                    type=lesson['teacher']['type']
                )
            lesson1 = Lesson(
                id=lesson['id'],
                date=lesson['dateLesson'],
                is_morning=lesson['isMorning'],
                date_update=lesson['dateUpdate'],
                offender=teacher
            )

        # classroom
        for classroom in jsonData['classrooms']:
            classroom1 = Classroom(
                id=classroom['id'],
                name=classroom['name'],
                nb_place=classroom['nbPlace'],
                date_update=classroom['dateUpdate']
            )
        s.commit()


mainClass = Synchronization()
