# -*- coding: utf-8 -*-

class Person(object):
    __name__ = 'Person Class'
    #__name = ''
    _date = '20221115'
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def __set_age(self, age):
        self.__age = age
        
jack = Person('Jack', 20)
print(jack.get_name())
print(jack.__name__)
#print(jack.__name)
print(jack._Person__name) #not recommended strongly
print(jack._date)
jack.height = 150
print(jack.height)
#jack.__set_age(30)
jack._Person__set_age(30)
print(jack.get_age())