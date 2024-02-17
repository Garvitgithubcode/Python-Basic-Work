
def getdate():
    import datetime
    return datetime.datetime.now()

def take(g):
    if g==1:
        d=int(input("enter 1 for excersise 2 for food: " ))
        if (d == 1):
            value=input("type here: " )
            with open("harry-ex.txt","a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully written")

        elif (d == 2):
            value = input("type here: ")
            with open("harry-food.txt", "a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")

    elif g==2:
        d=int(input("enter 1 for excersise 2 for food: " ))
        if (d == 1):
            value=input("type here: " )
            with open("kamal-ex.txt","a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")

        elif (d == 2):
            value = input("type here: ")
            with open("kamal-food.txt", "a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")

    elif g==3:
        d=int(input("enter 1 for excersise 2 for food: " ))
        if (d == 1):
            value=input("type here: " )
            with open("rohan-ex.txt","a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")

        elif (d == 2):
            value = input("type here: ")
            with open("rohan-food.txt", "a") as lg:
                lg.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")

    else:
        print("please enter valid name; 1(harry),2(kamal),3(rohan)")


def retrieve(g):
    if g==1:
        d=int(input("press 1 for exersise 2 for food"))
        if (d==1):
            with open("harry-ex.txt") as lg:
                for i in lg:
                    print(i,end="")

        elif (d==2):
            with open("harry-food.txt") as lg:
                for i in lg:
                    print(i,end="")

    elif g == 2:
        d = int(input("press 1 for exersise 2 for food"))
        if (d == 1):
            with open("kamal-ex.txt") as lg:
                for i in lg:
                    print(i, end="")

        elif (d==2):
            with open("kamal-food.txt") as lg:
                for i in lg:
                    print(i,end="")

    elif g == 3:
        d = int(input("press 1 for exersise 2 for food"))
        if (d == 1):
            with open("rohan-ex.txt") as lg:
                for i in lg:
                    print(i, end="")

        elif (d == 2):
            with open("rohan-food.txt") as lg:
                for i in lg:
                    print(i, end="")

    else:
        print("please enter valid name (harry,kamal,rohan)")

print("health management system")
a=int(input("press 1 for log and 2 for retreve: " ))
if a==1:
    b=int(input("press 1 for harry 2 for kamal 3 for rohan"))
    take(b)

else:
    b = int(input("press 1 for harry 2 for kamal 3 for rohan"))
    retrieve(b)






