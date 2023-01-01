import model_cube
import usual_view_cube as v

ochki = 100
def controllerLoop():
    user_vib = (v.getchois()).lower()
    if user_vib == "y":
        n = model_cube.start()
        if n == 6:
            v.viewMassage(n)
            model_cube.Win()
            v.viewMassage(ochki)
        elif n != 6:
            v.viewMassage(n)
            model_cube.Lose()
            v.viewMassage(ochki)
    elif user_vib == "n":
        v.viewMassage(model_cube.End_Game())
    elif ochki<=0:
        v.viewMassage(model_cube.End_Game())
    elif user_vib != "n" or "y":
        v.viewMassage("Введите Y или N")
        

def main():
    v.viewMassage("Хотите сиграть?")
    result = False
    f = v.getLoop()
    while not result:
        controllerLoop()

if __name__ == '__main__':
    main()
    