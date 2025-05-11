import board
import digitalio
import storage

# Подключаем пин (например, GP0 или D3 и т.д.)
button = digitalio.DigitalInOut(board.GP4)  # замените на нужный пин
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # подтяжка вверх: кнопка замыкает на GND

# Если кнопка НЕ нажата — отключаем USB-диск
if button.value:
    storage.disable_usb_drive()
button.deinit()