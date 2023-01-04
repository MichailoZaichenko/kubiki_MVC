import model_cube
import tkinker_view_cube as v

ochki = 100
number = 0
def controllerLoop():
    global ochki
    global number
    user_vib = (v.getchois()).lower()
    num = model_cube.start()
    v.viewMassage(f"Число на кубике: {num}")
    och = model_cube.ochki(ochki, num)
    ochki = och
    v.viewMassage(f"Ваши очки: {och}")
    message, result = model_cube.check(och)
    v.viewMassage(message)
    number = num
    return user_vib


        

def main():
    v.viewMassage("Хотите сиграть?")  
    result = False
    v.getLoop()()

if __name__ == '__main__':
    main()
    