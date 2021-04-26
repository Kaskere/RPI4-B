import RPi.GPIO as GPIO
import time
import smtplib

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)



def print_gpio_input(ch, is_cb):
    state_change = True
    if GPIO.input(ch):
        if not is_cb and state_change:
            print("out of water")
            message = "out of water"

    else:
        if not is_cb and state_change:
            print("in water")
            message = "has water"


def callback(channel):
    print_gpio_input(channel, True)



GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(channel, callback)


while True:
    print_gpio_input(channel, False)
    time.sleep(1.0)
