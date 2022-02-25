# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:33:31 2022

@author: mon pc
"""


class Student:
    
    def __init__(self, a, b):#a and b are instance variables for the Student class
        self.a = a
        self.b = b
    def Avg(self): #Avg is an instance method for the Student class
        return(self.a + self.b)/2 #"self" is used to show that they are instance variables n methods
s1 = Student(10, 20)
print(s1.Avg())
    