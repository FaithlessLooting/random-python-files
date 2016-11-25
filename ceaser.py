#ceaser cipher
#25/09/2015
#matthew dove

en_or_de = input("welcome to ceaser shift would you like to encode(1) or decode(2)?")
if en_or_de == "1":
    plaintext = input("what would you like to encode?")
    number = input("how many places would you like to move this?")
    number = int(number)
    def getTranslatedMessage(plaintext,number):
        translated = ''
        for symbol in plaintext:
            if symbol.isalpha():
                num = ord(symbol)
                num += number
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                    translated += chr(num)
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                    translated += chr(num)
                else:
                    translated += symbol
        return translated
    print('Your translated text is:')
    print(getTranslatedMessage(plaintext, number))
    
    print("and the number of letters shifted is", number)

if en_or_de == "2":
    plaintext = input("what would you like to encode?")
    number = input("how many places would you like to move this?")
    number = int(number)
    number = -number
    def getTranslatedMessage(plaintext,number):
        translated = ''
        for symbol in plaintext:
            if symbol.isalpha():
                num = ord(symbol)
                num += number
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                    translated += chr(num)
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                    translated += chr(num)
                else:
                    translated += symbol
        return translated
    print('Your translated text is:')
    print(getTranslatedMessage(plaintext, number))


              
