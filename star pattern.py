print("draw star pattern ")
num=int(input("enter pattern no." ))
print("enter boolean number 0/1 ")
a=int(input())
if a==0:
    for i in range(0,num+1):
         print("*" ' ' * i )

elif a==1:
    for i in range(num,0,-1):
            print("*" ' '*  i )

else:
    print("invalid!")
    print("please check your input!")



