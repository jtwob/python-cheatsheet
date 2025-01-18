class oop(object):
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def getProp1(self):
        return self.prop1
    def setProp1(self, newVal):
        self.prop1 = newVal
    def getProp2(self):
        return self.prop2
    def setProp2(self, newVal):
        self.prop2 = newVal

class oop2(oop):
    def __init__(self, prop1, prop2, prop3):
        super().__init__(prop1, prop2)
        self.prop3 = prop3
    def getProp3(self):
        return self.prop3


def main(): 
    p1 = oop2(1, 2, 3)
    print(p1.getProp1())
    p1.setProp1(0)
    print(p1.getProp1())
    print(p1.getProp3())
      
main() 

