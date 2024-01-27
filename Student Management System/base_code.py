
import pickle
class Student:
    def __init__(self,name:str,age:int,gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")