#init method

class myClass:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('My name is', self.name)

p = myClass('Bhawna')
p.say_hi()
