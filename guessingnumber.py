import random

guess=random.randint(1,100)
while True:
    try:
        n=int(input('Guess the Number(1-100):'))

        if(guess>n):
            print('too low')
        elif(guess<n):
            print('too high')
        else:
            print('Well done')
            break
            
    except ValueError:
        print('Please enter a valid number')
    
    
