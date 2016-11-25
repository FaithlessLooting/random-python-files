#linear search
#matthew dove

#creates a list of names
namelist = ["Alan", "Bill", "Chris", "Dave"]
#saves a variable with the string you are going to search for
searchtarget = (input("who are you looking for: "))
#sets i equal to 0
i = 0
#while i is less than the length of the list and the word in
#the list we are looking at is not the same as the string we
#are searching for
while i< len(namelist) and namelist[i] != searchtarget:
#add one to i    
    i = i+1
#if i is less than the length of the list when the above loop
#has finished running    
if i <len(namelist):
# output the name is in the position and the position of the string    
    print("the name is in position", i)
#otherwise the loop stopped because i got longer than the length of
#of the list, therefore the string we are looking for must not be
#in the list    
else:
    print ("the name is not on the list")

