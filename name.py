name=input('Enter your name: ')
if len(name)<3:
    print('Name must be more than 2 characters!')
elif len(name)>20:
    print("Name must be below or equal to 20 characters")
else :
    print('Hey ' + name + '!, Hope you have a great day!.')