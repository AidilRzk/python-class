# -*- coding: utf-8 -*-


class Name():
    def __init__(self, name, age, colour):
        self.name=name
        self.age=age
        self.colour=colour
        
    def nama(self):
        print("my name is: " + self.name)
        print("my age is: " + self.age)
        print("my fav colour is: " + self.colour)

'''
r1=Name()
r1.name= input("your name:")
r1.age= "24"
r1.colour= "Red"
r1.nama()'''

r1= Name("aidil", "24", "Red")
r1.nama()