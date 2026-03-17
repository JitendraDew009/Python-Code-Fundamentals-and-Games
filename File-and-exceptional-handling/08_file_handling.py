# file = open("order.txt","w")
# file.write("Masala chai -2 cups")
# file.write("/n Masala chai -3 cups ")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()
with open("order.txt", "w") as file:
    file.write("ginger tea --4cups")