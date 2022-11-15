# -*- coding: utf-8 -*-

class Animal(object):
    _color = 'white'
    
    def run(self):
        print('animal is running')
        
    def eat(self):
        print('animal is eating')
        
    def hunt(self):
        self.run()
        self.eat()
        
    def sleep(self):
        print('sleeping')
        
class Tiger(Animal):
    _weight = 120
    
    def run(self):
        print('tiger is running')
        
    #def run(self, speed):
        #print('tiger is running by %s m/s' % speed)
        
    def eat(self):
        print('tiger is eating')
        
    def hunt(self):
        self.run()
        self.eat()
        
class Vehicle(object):
    def run(self):
        print('vehicle is running')
        
def set_speed(Animal, speed):
    Animal.run()
    print('with %s m/s' % speed)
        
animal = Animal()
animal.hunt()

tiger = Tiger()
tiger.hunt()
print(tiger._weight)
print(tiger._color)
tiger.sleep()
tiger.run()
tiger.run()

set_speed(animal, 10)
set_speed(tiger, 20)
set_speed(Vehicle(), 30)

Vehicle().run()