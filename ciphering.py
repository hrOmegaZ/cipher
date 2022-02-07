# This program asks for your name to personalize
# It asks to encrypt or decrypt a message
# Then you put in a message and the key
# It will after put out the encrypted/decrypted message

def Convert(string):
    list_1 = []
    list_1[:0] = string
    return list_1

playing = True
message = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = Convert(alphabet)
cryption = []
name = input('name: ')
while playing == True:
    cipher = input(f'{name}, would you like to encrypt or decrypt a message? ')
    if cipher == 'encrypt':
        m_int = False
        while m_int == False:
            message = input('Message: ')
            try:
                m = int(message)
                m_int == True
                print('Input letters')
            except:
                m_int == False
                break
        message = Convert(message)
        key = int(999)
        while key > 10 or key < 0:
            key = int(input('Key: '))
        for x in range(len(message)):
            for y in range(len(alphabet)):
                if message[x] == alphabet[y]:
                    cryption.append(alphabet[y+key])
            if message[x] == ' ':
                cryption.append(' ')
            else:
                pass
        print(''.join(cryption))

    elif cipher == 'decrypt':
        m_int = True
        while m_int == True:
            message = input('Message: ')
            try:
                m = int(message)
                m_int = True
                break
            except:
                m_int = False
        message = Convert(message)
        key = int(999)
        while key > 10 or key < 0:
            key = int(input('Key: '))
        for x in range(len(message)):
            for y in range(len(alphabet)):
                if message[x] == alphabet[y]:
                    cryption.append(alphabet[y-key])
            if message[x] == ' ':
                cryption.append(' ')
            else:
                pass
        print(''.join(cryption))

    else:
        print('Inputted value is invalid... \nTry again...')
    
    stay = input('Do you wish to continue? (Y or N) ')
    if stay == 'Y' or stay == 'Yes' or stay == 'yes' or stay == 'y':
        pass
    elif stay == 'N' or stay == 'No' or stay == 'no' or stay == 'n':
        print(f'{name}, thanks for using this program...')
        playing == False
        break