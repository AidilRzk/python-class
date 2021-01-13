# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:40:11 2021

@author: dell
"""

class Name():
    def __init__(self, name, age, colour):
        self.name=name
        self.age=age
        self.colour=colour
        
    def nama(self):
        print("my name is: " + self.name)
        print("my age is: " + self.age)
        print("my fav colour is: " + self.colour)
        
class Person():
    def __init__(self, p, h, g):
        self.personal=p
        self.height=h
        self.gender=g
    
    def boy(self):
        self.gender=True
        
    def girl(self):
        self.gender=False

r1= Name("aidil", "24", "Red")
p1=Person("bad", "183", True)
p1.details= r1
p1.details.nama()
        

'''
r1=Name()
r1.name= input("your name:")
r1.age= "24"
r1.colour= "Red"
r1.nama()

r1= Name("aidil", "24", "Red")
r1.nama()'''