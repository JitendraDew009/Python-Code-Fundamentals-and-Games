# f = open("D:\All Coding Stuff\Python Code\FreeCodeCamp\Python-Code-Fundamentals-and-Games\File Input\Output\demo2.txt", "w" )
# f.write("This is my fist line in empty file.")
f = open("D:\All Coding Stuff\Python Code\FreeCodeCamp\Python-Code-Fundamentals-and-Games\File Input\Output\demo2.txt", "a" ) # we used a = append instead of w = write
f.write("\nThis is my second line "
        "\n This is my third line")

f.close()