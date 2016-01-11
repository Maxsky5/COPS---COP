# -*-coding: utf-8-*-
from entitiesRepository.OffenderRepository import OffenderRepository
from entitiesRepository.LessonRepository import LessonRepository
from entitiesRepository.CopRepository import CopRepository
from entitiesRepository.CheckRepository import CheckRepository
from entities.Check import Check
import time
import subprocess



class CheckOffender:
    def check(self, id):
        offenderRepo = OffenderRepository()
        lessonRepo = LessonRepository()
        copRepo = CopRepository()
        checkRepo = CheckRepository()

        # mac address
        mac = subprocess.check_output("ifconfig wlan0 | grep HWaddr | cut -d ' ' -f 10", shell=True)

        # looking for the offender in db
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
            check = Check(date=time.strftime("%Y%m%d%H%M%S"), cop_id=cop.id, offender_id=offender.id)
            checkRepo.add(check)
            return True