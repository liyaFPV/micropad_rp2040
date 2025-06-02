import board
import digitalio
import json

macros=[]
hotmap0=[]
hotmap0_type=[]

def load():
    global macros, hotmap0, hotmap0_type
    with open("config.json", "r") as file:
        config = json.load(file)
    
    macros = config["macros"]  # это словарь
    hotmap0 = config["hotmap0"]  # это список
    hotmap0_type = config["hotmap0_type"]  # это список






# Подключение пинов
cols = [digitalio.DigitalInOut(board.GP4),
        digitalio.DigitalInOut(board.GP5),
        digitalio.DigitalInOut(board.GP6),
        digitalio.DigitalInOut(board.GP7)]

rows = [digitalio.DigitalInOut(board.GP0),
        digitalio.DigitalInOut(board.GP1),
        digitalio.DigitalInOut(board.GP2),
        digitalio.DigitalInOut(board.GP3)]

# Создаём список клавиш от 0 до 15
keys = [
    ["0", "1", "2", "3"],
    ["4", "5", "6", "7"],
    ["8", "9", "10", "11"],
    ["12", "13", "14", "15"]
]

page = 0
