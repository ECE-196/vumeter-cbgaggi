import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

analog_vals = [6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    leds_initialize = 0

    for i, analog_vals in enumerate(analog_vals):
        if volume >= analog_vals:  # Check if volume exceeds the threshold
            leds_initialize = i + 1

    # Turn on/off LEDs
    for i, led in enumerate(leds):
        led.value = i < leds_initialize

    sleep(0.1)
    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
