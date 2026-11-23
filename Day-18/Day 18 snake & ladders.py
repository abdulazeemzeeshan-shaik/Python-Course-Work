#snake & ladders
import random
count=0
rolls=0
while True:
    input("clicke enter to throw a dice")
    dice = random.randint(1,6)
    if  count + dice <= 100:
        count+=dice
        print(f" your dice value is{dice}")
        print(f" you are at {count} position")
        if count ==23:
            count = 7
        elif count ==37:
            count = 27
        elif count== 56:
            count = 45
        elif count == 92:
            count  = 65
    
        
        elif count == 25:
            count  =47
        elif count == 35:
            count = 58
        elif count== 60:
            count = 80
        elif count==72:
            count=91

            print(f"snake bite{count}")

    rolls+=1
    if count==100:

        print(f"you win at {rolls} rolls")
        break