import MotionDetection
from task.Synchronization import Synchronization
class MainWrapper:
    def __init__(self, name):
        print("Synchronizing with server..")
        sync = Synchronization()
        print("Synchronized OK")
        print("Starting COP")
        self.mainLoop()


    def mainLoop(self):
        print("Initializing MotionDetection.")
        md = MotionDetection.MotionDetection("md")


print("Starting Main Class")
mainClass = MainWrapper("main")
