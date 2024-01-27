import pickle

from Student_data import Student
with open("student.pickle","rb") as f:
    obj = pickle.load(f)

for item in obj:
    print(item.display(),end=" ")
    print("")