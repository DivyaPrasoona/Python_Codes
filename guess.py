gnum=23
i=0
j=3
while i<=j:
    guess=int(input('Guess: '))
    i+=1
    k=j-i
    if guess==gnum:
        print('You guessed it right!!!')
    elif i!=0:
        print("uh oh!. That's a wrong guess")
        print(f"You have only {k} guesses left!")
    else:
        print('You have run out of guesses')