# -*-coding: utf-8-*-
import Fixture


class MainFixture:
    def __init__(self, name):
        print("start fixture")
        fixture = Fixture.Fixture("fixture")
        fixture.deleteRecords()
        #fixture.addRecords()
        #fixture.testAddWithLink()

mainClass = MainFixture("main")