# -*-coding: utf-8-*-
import Fixture


class MainFixture:
    def __init__(self, name):
        print("start fixture")
        Fixture.Fixture("fixture")

mainClass = MainFixture("main")