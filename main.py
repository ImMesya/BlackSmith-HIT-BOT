from PIL import ImageGrab
from time import sleep
from directkeys import KEY_A, KEY_D, PressKey, ReleaseKey

red = [(217, 15, 0), (214, 15, 0)]
black = [None, (33, 43, 57)]

ask = input('1 - single, 2 - multiplayer: ')


def get_main_color(img):
    colors = img.getcolors(240)
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except Exception:
        pass

if __name__ == '__main__':
    while True:
        if ask == '1':
            screen = ImageGrab.grab(bbox=(290, 360, 360, 400))
        elif ask == '2':
            screen = ImageGrab.grab(bbox=(345, 195, 360, 200))
        else:
            break

        color = get_main_color(screen)
        if color in red:
            PressKey(KEY_A)
            sleep(0.25)
            ReleaseKey(KEY_A)
        elif color in black:
            PressKey(KEY_D)
            sleep(0.25)
            ReleaseKey(KEY_D)
        else:
            pass
