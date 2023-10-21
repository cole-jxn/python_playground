import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rc522 = SimpleMFRC522()

try:
    data = input('Input data to write to tag:')
    print("Place tag to write data")
    rc522.write(data)
    print("Data successfully written")
finally:
    GPIO.cleanup()
