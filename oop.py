class oop:
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def getProp1(self):
        return self.prop1
    def setProp1(self, newVal):
        self.prop1 = newVal

p1 = oop(4, 5)
print(p1.getProp1())
p1.setProp1(2)
print(p1.getProp1())