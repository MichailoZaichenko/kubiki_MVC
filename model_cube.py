from random import randint

def start(end=6):
    return randint(1, end)

def Win(ochki):
    ochki+=3, False

def Lose(ochki):
    ochki-=1, False

def End_Game():
    return "Игра завершена!", True