import MotionDetection


class MainWrapper:
    def __init__(self, name):
        print("Starting COP")
        self.mainLoop()


    def mainLoop(self):
        print("Initializing MotionDetection.")
        md = MotionDetection.MotionDetection("md")


print("Starting Main Class")
mainClass = MainWrapper("main")
