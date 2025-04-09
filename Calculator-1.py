print("+++++++Welcome to tip calculator+++++++++++")

#print("What was the total bill ?")

Total_Bill = int(input("Enter the total bill -:"))
                

#print("How much tip would you like to give ?")

Tip = int(input("Enter the tip value -: "))
#Tip_per_person = Tip /100
#print(Tip_per_person)

#print("Each person should pay ?")

person_number = int(input("Enter the people count -: "))

Each_person_should_pay = (Total_Bill+Tip)/person_number

print(f"Total_Bill -:{Total_Bill}\nTip-:{Tip}\nEach_person_should_pay-:{Each_person_should_pay}")

