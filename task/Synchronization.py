# -*-coding: utf-8-*-
from entitiesRepository.CheckRepository import CheckRepository
from dao.ConnectDb import ConnectDb
from utils.ObjectFormater import ObjectFormater
from entities.Offender import Offender
from entities.Cop import Cop
from entities.Lesson import Lesson
from entities.Classroom import Classroom
from entities.Grade import Grade
import json

class Synchronization:
    serverHost = None
    # mac address
    #mac = subprocess.check_output("ifconfig wlan0 | grep HWaddr | cut -d ' ' -f 10", shell=True)
    #api call
    apiCall = "/api/synchronize?copMacAddress="

    def __init__(self):
        #config = ConfigParser.ConfigParser()
        #config.read("/home/pi/COPS-COP/config.ini")
        #Synchronization.serverHost = config.get('api', 'Host')
        #data = self.getLastData()
        mon_fichier = open("../information/synchronize.json", "r")
        contenu = mon_fichier.read()
        mon_fichier.close()
        self.addAll(json.loads(contenu))

    def sendCheck(self):
        checks = CheckRepository().getAll()
        jsonChecks = ChecksColl(checks).formatJson()
        print jsonChecks

        mavar1 = put('http://127.0.0.1:5000/checks', data={'data': checks}).json


    def getLastData(self):
        url = "http://"+Synchronization.serverHost+Synchronization.apiCall+Synchronization.mac
        print url.strip()
        data = requests.get(url.strip())
        print data.text
        return data.json()

    def addAll(self, jsonData):
        s = ConnectDb.session()

        objectFormater = ObjectFormater("wesh")

        offenders = objectFormater.OffendersToObjects(jsonData['offenders'])
        grades = objectFormater.GradesToObjects(jsonData['grades'])
        cops = objectFormater.CopsToObjects(jsonData['cops'])
        lessons = objectFormater.LessonsToObjects(jsonData['lessons'])
        classrooms = objectFormater.ClassroomsToObjects(jsonData['classrooms'])
        s.add_all(offenders)
        s.add_all(grades)
        s.add_all(cops)
        s.add_all(lessons)
        s.add_all(classrooms)
        """if(type(offenders) is dict):
            offenders = [offenders]

        if(type(cops) is dict):
            cops = [cops]

        if(type(lessons) is dict):
            lessons = [lessons]

        if(type(classrooms) is dict):
            classrooms = [classrooms]

        for offender in offenders:
            if self.entityExist(offender):
                print("update")
                # update
            else :
                s.add(offender)
        for grade in grades:
            if self.entityExist(grade):
                # update
                print("update")
            else :
                s.add(grade)
        for classroom in classrooms:
            if self.entityExist(classroom):
                # update
                print("update")
            else :
                s.add(classroom)
        for cop in cops:
            if self.entityExist(cop):
                # update
                print("update")
            else :
                s.add(cop)
        for lesson in lessons:
            if self.entityExist(lesson):
                # update
                print("update")
            else :
                s.add(lesson)"""

        s.commit()

    def entityExist(self, entity):
        s = ConnectDb.session()
        id = entity.id
        object = s.query().filter_by(id=id).one()
        if not object:
            return True
        return False

main = Synchronization()
