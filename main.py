import random


namn = input("Vad heter du?")
print(f"Hej{namn} och välkommen till spelet")

tal = random.randint(1,10)
gissning = input("gissa ett tal mellan 1 och 10")

if gissning == tal :
    print("Yay")
else :
    print("nay")
