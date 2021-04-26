import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


class Sensor:
    channel = None

    def __init__(self, channel):
        self.channel = channel
        GPIO.setup(self.channel, GPIO.IN)
        # This line tells our script to keep an eye on our gpio pin and let us
        # know when the pin goes HIGH or LOW
        GPIO.add_event_detect(self.channel, GPIO.BOTH, bouncetime=300)
        # This line asigns a function to the GPIO pin so that when the
        # above line tells us there is a change on the pin, run this function
        GPIO.add_event_callback(self.channel, self.callback)

    def callback(self, channel):
        sensor_input = GPIO.input(self.channel)
        print ("IN:" + str(sensor_input))
        if sensor_input:
            print("LED off")
        else:
            print("LED on")


sensor = Sensor(17)


# This is an infinte loop to keep our script running
while True:
    # This line simply tells our script to wait 0.1 of a second
    # this is so the script doesnt hog all of the CPU
    time.sleep(0.1)
