# -*-coding: utf-8-*-
import Check

class ChecksColl:
    checks = None

    def __init__(self, checks):
        self.checks = checks


    def formatJson(self):
        jsonChecks = {}
        i=0
        for check in self.checks:
            jsonChecks[i] = {'studentId': check.id, 'copMacAddress':check.cop.mac_address, 'date':check.date}
            i = i+1

        return jsonChecks