print("Welcome to Pizza Hut-:")

bill = 0

size = input ("Enter the size pizza do you want S,M,L -:")

peppi = input ("Do you want pepperoni Y or N -: ")

cheese = input ("Do you want an extra cheese -:")

if size == 'S' :
    bill  += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else :
    print("You typed the wrong choice")

if peppi == 'Y':
    if size == 'S':
        bill += 2
    else :
        bill += 3

if cheese == 'Y':
    bill +=1 

print(f"Total Bill  -:{bill}")



