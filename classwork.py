# #Problem 1
userInput=input("Enter a word")
while(userInput!="q"):
    print(userInput)
    userInput=input("Enter a word")


#Problem 3
user=input("Enter a number:")
while(user!="q"):
    if(user=="1"):
         print("1")
    elif(user=="2"):
         print("2")
    if(user=="3"):
         print("3")
    elif(user=='0'):
         print("error")
    user=input("Enter a number:")

#Problem 4
wordInput=input("Enter a word: ")
wordlist=" "
while(wordInput!="q"):
    wordlist=wordInput+","+wordlist
    wordInput=input("Enter a word:")
    if(wordInput=="q"):
         print(wordlist)