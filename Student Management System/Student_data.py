from base_code import Student
import pickle

S1 = Student("Kamal", 15, "Male")
S2 = Student("Lokesh", 16, "Male")
S3 = Student("Tarun", 14, "Male")
S4 = Student("Komal", 15, "Female")
S5 = Student("Payal", 16, "Female")
S6 = Student("Harshita", 16, "Female")
S7 = Student("Abhishek", 15, "Male")
S8 = Student("Sheetal", 14, "Female")
S9 = Student("Saloni", 16, "Female")
S10 = Student("Akash", 15, "Male")
S11 = Student("Akash", 15, "Male")

with open("student.pickle","wb") as f:
    pickle.dump((S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11),f)
