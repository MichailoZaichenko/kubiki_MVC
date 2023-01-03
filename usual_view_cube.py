import controller_cube
def getchois():
    return input('Хотите подкинуть ещё раз? Y/N')
    
def viewMassage(mas):
    print(mas)

def getLoop():
    return mainloop

def mainloop():
    user_vib = "y"
    while user_vib.lower() == "y":
        user_vib = controller_cube.controllerLoop()
    print("The end!")