weight=float(input('Enter your weight '))
unit=input("Enter 'Lbs' or 'KG' : ")
if unit.upper()=='L':
    conv=weight*0.45
    print(f"You are {conv} kilos.")
else:
    conv=weight/0.45
    print(f"You are {conv} pounds")