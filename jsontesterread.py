translated = ''
plaintext = input("what would you like to encode?")
plaintext = str.lower(plaintext)
f = open("jsontester.txt", "w")
f.write(plaintext)
f.close
f = open("jsontester.txt", "r")
data = ""
lines = f.readlines()
for line in lines:
    data = data + line.strip();
    print(data)
f.close()

print(str(data))

plaintext = str.lower(plaintext)
keyword =input("what would you like the keyword to be?")
keyword = str(keyword)
keyword = str.lower(keyword)
keyword = (keyword*10)
translated = ''
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
plaintext2 = getTranslatedMessage(plaintext,keyword)
print(plaintext2)

keyword2 =input("what would you like the keyword to be?")
keyword2 = str(keyword)
keyword2 = str.lower(keyword)
keyword2 = (keyword*10)
def getTranslatedMessage2(plaintext2,keyword2):
        translated = ''
        length = len(plaintext)
        key2 = []
        for symbol in keyword2:
            if symbol.isalpha():
                num3 = ord(symbol)
                num3 = num3 -96
                key2.append(num3)
        for i in range(len(plaintext2)):
            if plaintext2[i].isalpha():
                num =ord(plaintext2[i])
                num += key2[i]
                translated += chr(num)
        return translated
print(getTranslatedMessage2(plaintext2,keyword2))
            







