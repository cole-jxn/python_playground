import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rc522 = SimpleMFRC522()

try:
	id, data = rc522.read()
	print(id)
	print(data)
finally:
	GPIO.cleanup()
