# -*-coding: utf-8-*-
import ConfigParser
import subprocess

import requests

from entitiesRepository.CheckRepository import CheckRepository
from dao.ConnectDb import ConnectDb
from utils.ObjectFormater import ObjectFormater

class Synchronization:
    serverHost = None
    # mac address
    mac = subprocess.check_output("ifconfig wlan0 | grep HWaddr | cut -d ' ' -f 10", shell=True)
    # mac = "6c:19:8f:b8:bd:ff"
    #api call
    apiCall = "/api/synchronize?copMacAddress="

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("/home/pi/COPS-COP/config.ini")
        #config.read("../config.ini")
        Synchronization.serverHost = config.get('api', 'Host')
        data = self.getLastData()
        # mon_fichier = open("../information/synchronize.json", "r")
        # contenu = mon_fichier.read()
        # mon_fichier.close()
        self.addAll(data)

    def sendCheck(self):
        checks = CheckRepository().getAll()
        jsonChecks = ChecksColl(checks).formatJson()
        print jsonChecks

        # mavar1 = put('http://127.0.0.1:5000/checks', data={'data': checks}).json


    def getLastData(self):
        url = "http://"+Synchronization.serverHost+Synchronization.apiCall+Synchronization.mac
        print url.strip()
        data = requests.get(url.strip())
        print data.text
        return data.json()

    def addAll(self, jsonData):
        s = ConnectDb.session()

        print(type(s))

        objectFormater = ObjectFormater("wesh")

        offenders = objectFormater.OffendersToObjects(jsonData['offenders'])
        grades = objectFormater.GradesToObjects(jsonData['grades'])
        cops = objectFormater.CopsToObjects(jsonData['cops'])
        lessons = objectFormater.LessonsToObjects(jsonData['lessons'])
        lessons_grades = objectFormater.LessonsGradesToObjects(jsonData['lessons'])
        classrooms = objectFormater.ClassroomsToObjects(jsonData['classrooms'])

        for grade in grades:
            s.merge(grade)
        s.commit()
        for classroom in classrooms:
            s.merge(classroom)
        s.commit()
        for cop in cops:
            s.merge(cop)
        s.commit()
        for offender in offenders:
            s.merge(offender)
        s.commit()
        for lesson in lessons:
            s.merge(lesson)
        s.commit()
        for lessons_grade in lessons_grades:
            s.merge(lessons_grade)
        s.commit()



main = Synchronization()
