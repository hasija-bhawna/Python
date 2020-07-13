class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}!".format(self.name))
        Robot.population += 1

    def die(self):
        print("Robot {} is going to die.".format(self.name))
        Robot.population -= 1

    def count(cnt):
        cnt = Robot.population
        print('Count is:', cnt)
        if cnt == 0:
            print('There are no more Robots')



obj = Robot('JADOO')
obj.count()
obj.die()
obj.count()

obj1 = Robot('maxim')
obj1.count()

obj2 = Robot('citrus')
obj2.count()

obj2.die()
obj1.die()
obj2.count()
