from demoa import DemoA
from demob import DemoB

class DemoC(DemoB,DemoA):
    def showC(self):
        print("This is Demo C")

obj = DemoC()
obj.showA()
obj.showB()
obj.showC()