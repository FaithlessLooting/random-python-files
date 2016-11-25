#ceaser cipher
#25/09/2015
#matthew dove

en_or_de = input("welcome to ceaser shift would you like to encode(1) or decode(2)?")
if en_or_de == "1":
    plaintext = input("what would you like to encode?")
    number = input("how many places would you like to move this?")
    int(number)
    def caesar(plaintext, number):
        cipherText = ""
        for ch in plaintext:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + number
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                    finalLetter = chr(stayInAlphabet)
                    cipherText = ""
                    cipherText += finalLetter
                    print ("Your ciphertext is:", cipherText)
                    return cipherText
