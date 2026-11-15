chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        #nonlocal chai_type # u cant access chai type through nonlocal bcuz thats outside function.
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final global chai: ", chai_type)