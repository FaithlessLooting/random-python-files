#ceaser cipher
#25/09/2015
#matthew dove

en_or_de = input("welcome to ceaser shift would you like to encode(1) or decode(2)?")
if en_or_de == "1":
    plaintext = input("what would you like to encode?")
    number = input("how many places would you like to move this?")
    number = int(number)
    keyword = input("what is your keyword?")
    def getTranslatedMessage(plaintext,number):
        translated = ''
        for symbol in plaintext:
            if symbol.isalpha():
                num = ord(symbol)
                num += number
                for symbol in keyword:
                    if symbol.isalpha():
                        num2 = ord(symbol)
                        num += num2
                for symbol in plaintext:
                    if symbol.isupper():
                        if num > ord('Z'):
                            num -= 26
                    if num < ord('A'):
                        num += 26
                    translated += chr(num)
                if symbol.islower():
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
            for symbol in keyword:
                    if symbol.isalpha():
                        num2 = ord(symbol)
                        num += num2
                        for symbol in plaintext:
                            if symbol.isupper():
                                if num > ord('Z'):
                                    num -= 26
                    if num < ord('A'):
                        num += 26
                    translated += chr(num)
                    if symbol.islower():
                        if num > ord('z'):
                            num -= 26
                    elif num < ord('a'):
                        num += 26
                        ranslated += chr(num)
                    else:
                        translated += symbol
                    return translated
    print('Your translated text is:')
    print(getTranslatedMessage(plaintext, number))


              


        


              


                    
