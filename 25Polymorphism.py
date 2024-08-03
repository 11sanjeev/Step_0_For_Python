class Bird():
    def walk(self):
        print('hopping around')

class Mammal():
    def walk(self):
        print('jogging around....')

class Movements:
    @classmethod
    def move(self,thing):
        thing.walk()

bird = Bird()
dog = Mammal()
Movements.move(bird)
Movements.move(dog)
