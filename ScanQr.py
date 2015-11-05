#!/usr/bin/env python
# coding: utf-8
#
# pyqrcode sample decoder

import sys, qrtools, time, picam

class ScanQr:
    def __init__(self, name):
        print("Qr Detection initialized.")


    def detectQR(self, image):
        print("Cop Decoding")
        d = qrtools.QR()
        if d.decodeString(image, 800, 600):
            return d.data
        else:
            return 0
        print('fin de decode')
