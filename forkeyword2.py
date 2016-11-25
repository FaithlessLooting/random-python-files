plaintext = input("what would you like to encode?")
plaintext = str.lower(plaintext)
keyword =input("what would you like the keyword to be?")
keyword = str(keyword)
keyword = str.lower(keyword)
keyword = (keyword*10)
def getTranslatedMessage(plaintext,keyword):
        translated = ''
        length = len(plaintext)
        key = []
        for symbol in keyword:
            if symbol.isalpha():
                num2 = ord(symbol)
                num2 = num2 -96
                key.append(num2)
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                num =ord(plaintext[i])
                num += key[i]
                translated += chr(num)
        return translated

print(getTranslatedMessage(plaintext,keyword))  
