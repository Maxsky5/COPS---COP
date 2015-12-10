# -*-coding: utf-8-*-
import OffenderRepository
import LessonRepository
import CopRepository
import CheckRepository
from entities import entities
import time


class MainRepository:
    def __init__(self):
        print("Starting Repository")
        offender = self.checkOffender(43)
        if offender:
            print "Bienvenu !"
        else:
            print "T'as rien a foutre ici conard !"


    def checkOffender(self, id):
        offenderRepo = OffenderRepository.OffenderRepository()
        lessonRepo = LessonRepository.LessonRepository()
        copRepo = CopRepository.CopRepository()
        checkRepo = CheckRepository.CheckRepository()

        # adresse mac en dur ( en attente de vrais enregistrements dans la base)
        mac = '00:00:00:00:00:00'

        # on va chercher l'offender dans la base
        offender = offenderRepo.getById(id)
        if len(offender) == 0:
            return False
        offender = offender[0]
        if offender.is_teacher():
            lesson = [offender.lesson]
        else:
            lesson = lessonRepo.getLessonByStudy(id)

        if len(lesson) == 0:
            return False
        lesson = lesson[0]
        cop = copRepo.getByMacAndByLesson(mac, lesson.id)

        if len(cop) > 0:
            cop = cop[0]
            check = entities.Check(date=time.strftime("%Y%m%d%H%M%S"), cop_id=cop.id, offender_id=offender.id)
            checkRepo.add(check)
            return True



print("Starting Main Class")
MainRepository()
