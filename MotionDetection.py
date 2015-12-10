import StringIO
import subprocess
import os
import time
import ScanQr
from datetime import datetime
from PIL import Image
from entitiesRepository import OffenderRepository, LessonRepository, CopRepository, CheckRepository
import entities.Check


class MotionDetection:

    # Motion detection settings:
    # Threshold (how much a pixel has to change by to be marked as "changed")
    # Sensitivity (how many changed pixels before capturing an image)
    # ForceCapture (whether to force an image to be captured every forceCaptureTime seconds)
    threshold = 10
    sensitivity = 20
    forceCapture = False
    forceCaptureTime = 1
    scanner = ()

    def __init__(self, name):
        print("MotionDection initialized")
        self.loopDetect()
        

    # Capture a small test image (for motion detection)
    def captureTestImage(self):
        command = "raspistill -n -w %s -h %s -t 5 -e bmp -o -" % (100, 75)
        imageData = StringIO.StringIO()
        imageData.write(subprocess.check_output(command, shell=True))
        imageData.seek(0)
        im = Image.open(imageData)
        buffer = im.load()
        imageData.close()
        return im, buffer


    def bufferImage(self):
        imageData = StringIO.StringIO()
        imageData.write(subprocess.check_output("raspistill --colfx 128:128 -w 800 -h 600 -t 1000 -e bmp -o -", shell=True))
        imageData.seek(0)
        im = Image.open(imageData)
        return im


    def loopDetect(self):
        qrReader = ScanQr.ScanQr("scanner")
        print("Getting first Image")
        # Get first image
        image1, buffer1 = self.captureTestImage()
        # Reset last capture time
        lastCapture = time.time()
        while True:
            # Get comparison image
            image2, buffer2 = self.captureTestImage()

            # Count changed pixels
            changedPixels = 0
            for x in xrange(0, 100):
                for y in xrange(0, 75):
                    # Just check green channel as it's the highest quality channel
                    pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                    if pixdiff > self.threshold:
                        changedPixels += 1

            # Check force capture
            if self.forceCapture:
                if time.time() - lastCapture > forceCaptureTime:
                    changedPixels = sensitivity + 1

            # Save an image if pixels changed
            if changedPixels > self.sensitivity:
                print ("Cop has detected Motion.")
                lastCapture = time.time()
                image = self.bufferImage()
                data = qrReader.detectQR(image)
                if data == 0:
                    print("Qr was not detected.")
                else:
                    print("QR Detected! Value is:")
                    print(data)
                    # Recuperation de l'id de l'éleve avec le Qrcode
                    data = 13
                    if self.checkOffender(data) :
                        print "Bienvenu !"
                    else:
                        print "T'as rien a foutre ici conard !"
            else:
                print("Not changed")

            # Swap comparison buffers
            image1 = image2
            buffer1 = buffer2

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
