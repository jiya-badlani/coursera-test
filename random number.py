import random

def dice ():
    counter = 0
    l=[]
    while counter<6 :
        randno=random.randint(1,6)
        l.append(randno)
        counter+=1
        if counter>=6 :
            pass
        else:
            return l
n=1
while n==1:
    n = int(input("Enter 1 to roll a dice and get a random number:") )
    print(dice() )
