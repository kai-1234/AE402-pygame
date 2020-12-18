import random
class movingSpeed:
    def __init__(self,distance,time):
        self.distance = distance
        self.time = time
    def speed(self):
        print(self.distance/self.time)
car = movingSpeed(random.randrange(100,1000),random.randrange(50,500))
print(car.speed())