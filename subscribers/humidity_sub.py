import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Received:", msg.topic, msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883)

client.subscribe("lab/humidity")
client.on_message = on_message

print("Listening for humidity messages...")
client.loop_forever()
