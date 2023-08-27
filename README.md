# Health Management System
# 3 clients - Harry, Rohan and karan
print("Health Management System")

client=input("Enter your name:\n")
if client=="harry":
    print("*Food\n*Exercise:" )
    health=input()
    if health == 'food':
        print("Morning : Light breakfast;\nEvening : Heavy food;\nNight : Take ome fruits")
    elif health == 'exercise':
        print("Monday : Back day;\nTuesday : Chest day;\nWednesday : Leg day;\nThursday : Abs;\nFriday : Deadlift;\nSat & Sun : Rest")

if client=="rohan":
    print("*Food\n*Exercise")
    health=input()
    if health == 'food':
        print("Morning : Light breakfast;\nEvening : Heavy food;\nNight : Take ome fruits")
    elif health == 'exercise':
        print("Monday : Back day;\nTuesday : Chest day;\nWednesday : Leg day;\nThursday : Abs;\nFriday : Deadlift;\nSat & Sun : Rest")

if client=="kamal":
    print("*Food\n*Exercise:" )
    health=input()
    if health == 'food':
        print("Morning : Light breakfast;\nEvening : Heavy food;\nNight : Take ome fruits")
    elif health == 'exercise':
        print("Monday : Back day;\nTuesday : Chest day;\nWednesday : Leg day;\nThursday : Abs;\nFriday : Deadlift;\nSat & Sun : Rest")
else:
    print("client not found")

