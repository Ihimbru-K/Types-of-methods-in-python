# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:11:06 2022

@author: mon pc
"""


#static method
class Student:
 name ='Student'
def __init__(self, a, b):
 self.a = a
 self.b = b
@staticmethod
def info():
    return"This is a student class"
print(Student.info()) 