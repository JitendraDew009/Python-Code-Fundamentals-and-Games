friend = ["jitu", 'Jitesh', "Dalu"]
            #0      1        2
print(friend)
print(friend[1])
print(friend[-1])
print(friend[1:]) # kaha se pakadna hain
friend[1]= "jeetu"
print(friend)
lucky_number=[4,5,6,7,8,9]
friend.extend(lucky_number) # addition or extend karta hain
friend.append("Zoya") # end me jaa ke add ho jaega 
friend.insert(1, "juju") # index 1 me insert kar dega
print(friend)
friend.remove("juju")
print(friend)
friend.pop() #end ka ek element remove kar dega
print(friend)
print(friend.count("jitu")) # count karta hai kon sa element print hota hain.
lucky_number.sort()
print(lucky_number) #ascending order pe rearrange
lucky_number.reverse()
print(lucky_number) #descending order pe rearrange
friend2 = friend.copy()
print(friend2)

