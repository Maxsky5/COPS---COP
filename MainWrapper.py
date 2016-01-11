import MotionDetection
import task.MainSynchronization

class MainWrapper:
    def __init__(self, name):
        print("Synchronizing with server..")
        sync = task.MainSynchronization
        print("Synchronized OK")
        print("Starting COP")
        self.mainLoop()


    def mainLoop(self):
        print("Initializing MotionDetection.")
        md = MotionDetection.MotionDetection("md")


print("Starting Main Class")
mainClass = MainWrapper("main")
