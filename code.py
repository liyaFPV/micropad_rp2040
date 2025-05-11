#подключение библеотек
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio
import neopixel
import time
import json


hot_map0=[]
hot_map_type0=[]
hot_map1=[]
hot_map_type1=[]
hot_map2=[]
hot_map_type2=[]
hot_map3=[]
hot_map_type3=[]
led0=[]
led1=[]
led2=[]
led3=[]
map=0#переменая слоя

# настройка пинов

rgbled = neopixel.NeoPixel(board.GP16, 1)

kay0 = digitalio.DigitalInOut(board.GP4)#подключаем пин в програму
kay0.direction = digitalio.Direction.INPUT#настраеваем как выход
kay0.pull = digitalio.Pull.UP#настраеваем подяжку

kay1 = digitalio.DigitalInOut(board.GP5)
kay1.direction = digitalio.Direction.INPUT
kay1.pull = digitalio.Pull.UP

kay2 = digitalio.DigitalInOut(board.GP6)
kay2.direction = digitalio.Direction.INPUT
kay2.pull = digitalio.Pull.UP

kay3 = digitalio.DigitalInOut(board.GP7)
kay3.direction = digitalio.Direction.INPUT
kay3.pull = digitalio.Pull.UP

kay4 = digitalio.DigitalInOut(board.GP8)
kay4.direction = digitalio.Direction.INPUT
kay4.pull = digitalio.Pull.UP

kay5 = digitalio.DigitalInOut(board.GP9)
kay5.direction = digitalio.Direction.INPUT
kay5.pull = digitalio.Pull.UP

kay6 = digitalio.DigitalInOut(board.GP10)
kay6.direction = digitalio.Direction.INPUT
kay6.pull = digitalio.Pull.UP

kay7 = digitalio.DigitalInOut(board.GP11)
kay7.direction = digitalio.Direction.INPUT
kay7.pull = digitalio.Pull.UP

kay8 = digitalio.DigitalInOut(board.GP12)
kay8.direction = digitalio.Direction.INPUT
kay8.pull = digitalio.Pull.UP

kay9 = digitalio.DigitalInOut(board.GP13)
kay9.direction = digitalio.Direction.INPUT
kay9.pull = digitalio.Pull.UP

kay10 = digitalio.DigitalInOut(board.GP14)
kay10.direction = digitalio.Direction.INPUT
kay10.pull = digitalio.Pull.UP

kay11 = digitalio.DigitalInOut(board.GP15)
kay11.direction = digitalio.Direction.INPUT
kay11.pull = digitalio.Pull.UP

rol0 = digitalio.DigitalInOut(board.GP26)
rol0.direction = digitalio.Direction.INPUT
rol0.pull = digitalio.Pull.UP

rol1 = digitalio.DigitalInOut(board.GP27)
rol1.direction = digitalio.Direction.INPUT
rol1.pull = digitalio.Pull.UP

rol2 = digitalio.DigitalInOut(board.GP28)
rol2.direction = digitalio.Direction.INPUT
rol2.pull = digitalio.Pull.UP

rol3 = digitalio.DigitalInOut(board.GP29)
rol3.direction = digitalio.Direction.INPUT
rol3.pull = digitalio.Pull.UP

kbd = Keyboard(usb_hid.devices)#настройка клавиотуры

def led(rgb):
    rgbled[0] = (rgb[0], rgb[1], rgb[2])


def load_json():#фнкция для загрузки json файла конфигурации
    with open("config.json", "r") as f:#открываем файл из внутренеё памяти
        data = json.load(f)#дастойм всё из него и помешаем в буфер

    hot_map0[:]=data["hot_map0"]#достоём из буфира нужные даные и записоваем их в переменую 
    hot_map_type0[:]=data["hot_map_type0"]
    hot_map1[:]=data["hot_map1"]
    hot_map_type1[:]=data["hot_map_type1"]
    hot_map2[:]=data["hot_map2"]
    hot_map_type2[:]=data["hot_map_type0"]
    hot_map3[:]=data["hot_map3"]
    hot_map_type3[:]=data["hot_map_type3"]
    led0[:]=data["led0"]
    led1[:]=data["led1"]
    led2[:]=data["led2"]
    led3[:]=data["led3"]
    

def hid(hotkay, type):
    global map
    if type == "keyboard":
        keys = [getattr(Keycode, k.strip().split(".")[1]) for k in hotkay.split(",")]
        kbd.send(*keys)
    elif type == "mapp":
        map = (map + 1) % 4
    elif type == "mapm":
        map = (map - 1) % 4

load_json()
led(led0)
while True:
    kay_map=[kay0.value,kay1.value,kay2.value,kay3.value,kay4.value,kay5.value,kay6.value,kay7.value,kay8.value,kay9.value,kay10.value,kay11.value,rol0.value,rol1.value,rol2.value,rol3.value]
    for i in range(len(kay_map)):
        if kay_map[i]==0:
            if map==0:hid(hot_map0[i],hot_map_type0[i]);led(led0)
            if map==1:hid(hot_map1[i],hot_map_type1[i]);led(led1)
            if map==2:hid(hot_map2[i],hot_map_type2[i]);led(led2)
            if map==3:hid(hot_map3[i],hot_map_type3[i]);led(led3)
            time.sleep(0.2)