import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    temp = random.randint(20, 35)
    message = f"Temperature: {temp}°C | Student ID: 12114470"
    client.publish("lab/temperature", message)
    print("Published:", message)
    time.sleep(2)
