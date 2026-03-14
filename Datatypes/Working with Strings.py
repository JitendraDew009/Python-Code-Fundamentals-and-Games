print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")
#---------------------------------------
phrase = "London_Academy"
print(phrase + " is cool ") #concatination means ek string aur dusre string ko jodne ki prakriya hain.
print(phrase.upper()) #to do all capital letters.
print(phrase.lower()) #to do all lower letters.
print(phrase.isupper()) #to check uppercase me hai ki nahi.
print(phrase.islower()) #to check lowercase me hai ki nahi.
print(phrase.upper().isupper()) # converts to upper then check is it upper and ans will be true.
print(len(phrase)) # calculate length of string.
print(phrase[0]) #L
print(phrase[1]) #o
print(phrase[2]) #n
print(phrase[3]) #d
print(phrase[4]) #o
print(phrase[5]) #n
print(phrase[6]) #_
print(phrase[7]) #A
print(phrase[8]) #c
print(phrase[9]) #a
print(phrase[10]) #d
print(phrase[11]) #e
print(phrase[12]) #m
print(phrase[13]) #y
print(phrase) #London_Academy
              #0123

print(phrase.index("L")) #0
print(phrase.index("o")) #1
print(phrase.index("n")) #2
print(phrase.index("d"))
print(phrase.index("o"))
print(phrase.index("n"))

print(phrase.replace("London", "India"))

