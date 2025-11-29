import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    humidity = random.randint(30, 90)
    message = f"Humidity: {humidity}% | Student ID: 12114470"
    client.publish("lab/humidity", message)
    print("Published:", message)
    time.sleep(2)
