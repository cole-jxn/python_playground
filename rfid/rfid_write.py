import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    id = input('New data:')
    print("Now place your tag to write")
    reader.write(id)
    print("Written")
finally:
    GPIO.cleanup()
