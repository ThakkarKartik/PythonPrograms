# Simple with Default Parameters
def welcome():
        print("Hello")
        print("Welcome to my Program")



def myfun(name,msg="Default Msg"):
    print(name)
    print(msg)
    return name

print("Welcome to UDF Program")
myfun("Robert")
myfun("Ivan","User Msg")

welcome()

# Variable amount of Parameteres
def myfun2(*varlist):
    for var in varlist:
        print(var)

myfun2(1,"2",3,"4",5,"6")
L1 = [1,2,3,4]
T1 = (1,2,3,4)
S1 = {1,2,3,4}
myfun2(L1,T1,S1)

n = myfun("Champa","Chiman")
print(n)