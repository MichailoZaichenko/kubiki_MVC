import tkinter
import controller_cube
def getchois():
    return txt.get()

def viewMassage(mas):
    lb1.configure(text=mas)
    lb2.configure(text=f"Число на кубике: {controller_cube.number}")

def getLoop():
    return window.mainloop

def mainloop():
    user_vib = "y"
    while user_vib.lower() == "y":
        user_vib = controller_cube.controllerLoop()
    print("The end!")

window = tkinter.Tk()

lb1 = tkinter.Label(window, text='')
lb2 = tkinter.Label(window, text='')
txt = tkinter.Entry(window, width=30)
btn = tkinter.Button(window, text="Отправить", command=controller_cube.controllerLoop)

lb1.grid(column=0, row=0)
lb2.grid(column=0, row=1)
txt.grid(column=0, row=2)
btn.grid(column=1, row=2)