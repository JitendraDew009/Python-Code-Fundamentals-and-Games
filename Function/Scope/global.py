chai_type = "Plain" #global scope

def front_destk():
    
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()

front_destk()

print("Final global chai is ", chai_type)
# with global = Final global chai is  Irani  ## because you are making global chai_type in kitchen()
# without global = Final global chai is  Plain ## default global chai_type = plain
# you cannot use nonlocal chai_type here becaue it works only if there is varable present just above the function.
# It designed in such a way it should be looking just kitchen() outer function.
