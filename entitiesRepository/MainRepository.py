# -*-coding: utf-8-*-
from task.CheckOffender import CheckOffender


class MainRepository:
    def __init__(self):
        print("Starting Repository")
        check = CheckOffender()
        offender = check.check(1)
        if offender:
            print "Bienvenu !"
        else:
            print "T'as rien a foutre ici conard !"



print("Starting Main Class")
MainRepository()
