import board # type: ignore
import digitalio # type: ignore
import time
import config

from adafruit_matrixkeypad import Matrix_Keypad # type: ignore
import usb_hid # type: ignore
from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore

# Ждём немного, чтобы HID успел подключиться
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)

# Инициализация клавиатуры
keypad = Matrix_Keypad(config.rows, config.cols, config.keys)


config.load()
print(config.macros)
print(config.hotmap0)
print(config.hotmap0_type)


def Keyboards(key_text):
    try:
        key_name = key_text.split('.')[-1]
        keycode = getattr(Keycode, key_name)
        keyboard.send(keycode)
    except AttributeError:
        pass  

def Keyboards_multi(name):
    try:
        macro_keys = config.macros[name]
        
        for key in macro_keys:
            key_name = key.split('.')[-1]
            keycode = getattr(Keycode, key_name)
            keyboard.press(keycode)
            time.sleep(0.05)
        
        keyboard.release_all()
    except AttributeError as e:
        print()
    except KeyError:
        print() 



# Функция получения нажатых клавиш (в виде int)
def get_pressed_keys():
    return [int(k) for k in keypad.pressed_keys]


def hid0(i):
    if i < len(config.hotmap0_type):
        if config.hotmap0_type[i] == "clik":
            Keyboards_multi(config.hotmap0[i])
        elif config.hotmap0_type[i] == "p":
            config.page += 1
            print(config.page)
        elif config.hotmap0_type[i] == "m":
            config.page -= 1
            print(config.page)
        
# Основной цикл
while True:
    pressed = get_pressed_keys()
    if pressed:
        for key in pressed:
            print(config.page)
            print(key)
            hid0(key)
        time.sleep(0.4)