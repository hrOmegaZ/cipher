def Convert(string):
    list_1 = []
    list_1[:0] = string
    return list_1

message = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = Convert(alphabet)
name = input('name: ')
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
    key = 0
    while key < 10 and key > 0:
        key = input('Key: ')

elif cipher == 'decrypt':
    m_int = True
    while m_int == True:
        message = input('Message: ')
        try:
            m = int(message)
            m_int = True
            break
        except:
            print('Input numbers')
            m_int = False
    message = Convert(message)
    key = 0
    while key < 10 and key > 0:
        key = input('Key:')

else:
    print('Inputted value is invalid... \nTry again...')