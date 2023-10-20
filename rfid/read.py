import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

for x in range (10):
	id, text = reader.read()
	print(id)
	print(text)
	time.sleep(2)

GPIO.cleanup()
