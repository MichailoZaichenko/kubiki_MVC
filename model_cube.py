from random import randint

def start(end=6):
    return randint(1, end)

def ochki(ochki, cube):
    if cube == 6:
        ochki +=3
        return ochki
    else:
        ochki -=1
        return ochki

def check(ochki):
    if ochki <= 0:
        return "Очки закончились", False
    elif ochki > 0:
        return f"У вас есть: {ochki} очков", True
    
