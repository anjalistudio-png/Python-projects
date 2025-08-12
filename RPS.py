
import random



while True:
    emojis={'r':'🗿','p':'📄','s':'✂️'}
    choices=('r','p','s')
    userChoice=input('Enter your choice(r/p/s):')
    if userChoice not in choices:
        print("Enter valid Choice")
    compChoice=random.choice(choices)
    print(f'You chose {emojis[userChoice]}')
    print(f'Computer chose {emojis[compChoice]}')
    if(userChoice==compChoice):
        print('Its a tie')
    elif(
    (userChoice=='s' and compChoice=='p')or
    (userChoice=='r' and compChoice=='s')or
    (userChoice=='p' and compChoice=='r')):
        print('YOU WINNNNNNNN!!!')
    else:
        print('You Lost,Try Again Next Time')
    should_continue=input('Do you wanna continue this game?(y/n):')
    if(should_continue=='n'):
        break
    else:
        continue







