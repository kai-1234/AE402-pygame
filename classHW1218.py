
class Pet:
    def __init__(self,legs,lenth):
        self.legs = legs
        self.lenth = lenth
    def size(self):
        return self.lenth**2*2
cat = Pet(4,25)
print(cat.size())
class Cat(Pet):
    def __init__(self,legs,lenth,color):
        super().__init__(legs, lenth)
        self.color = color
    def homeColor(self):
        return self.color
cat = Cat(4,25,'red')
print(cat.homeColor())