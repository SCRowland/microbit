from microbit import *
import neopixel
import time


LIGHT_RED = (16, 0, 0)
LIGHT_GREEN = (0, 16, 0)
OFF = (0, 0, 0)

PIXEL_COUNT = 24
ONE_MINUTE_IN_MILLISECONDS = 1000 * 60

NP = neopixel.NeoPixel(pin0, PIXEL_COUNT)


def check_for_reset(np):
    if button_a.was_pressed() or button_b.was_pressed():
        np.clear()
        sleep(100) # otherwise LED 0 randomly lights.
        reset()
        # unreachable
        return True
    
    return False


def wait(np, milliseconds):
    start = time.ticks_ms()
    
    while not check_for_reset(np):
        if time.ticks_diff(time.ticks_ms(), start) > milliseconds:
            return

    return


def set_all(np, colour):
    for pixel in range(len(np)):
        np[pixel] = colour
    np.show()


def twenty_five_minutes(np):
    wait(np, ONE_MINUTE_IN_MILLISECONDS)

    for pixel_id in range(len(np)):
        np[pixel_id] = LIGHT_RED
        np.show()
        wait(np, ONE_MINUTE_IN_MILLISECONDS)
    
    while True:
        np.clear()
        wait(np, 500)

        set_all(np, LIGHT_GREEN)
        wait(np, 500)


twenty_five_minutes(NP)