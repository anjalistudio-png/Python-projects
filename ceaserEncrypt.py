



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']




def encryption(plain_text, shift_key):
    cipher_text=''
    for char in plain_text:
        if char in alphabet:
            postion= alphabet.index(char)
            new_position=(postion+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text +=char
    print(f'Here is the after encryption: {cipher_text}')


def decryption(cipher_text, shift_key):
    plain_text=''
    for char in cipher_text:
        if char in alphabet:
            postion= alphabet.index(char)
            new_position=(postion-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
            cipher_text +=char
    print(f'Here is the after decryption: {plain_text}')

    
    




while True:
    to_do=input('Type e for encryption and d for decryption:\n')
    text=input('Type your message:\n')
    shift=int(input('Enter shift key:\n'))
    if(to_do=='e'):
        encryption(plain_text=text,shift_key=shift)
    elif(to_do=='d'):
        decryption(text,shift)
    playagain=input('Want to continue?(y/n):')
    if playagain=='n':
        print('Byee,Have a nice day!')
        break
    else:
        continue
        


       
