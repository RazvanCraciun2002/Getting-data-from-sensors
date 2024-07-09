import json
import random
import paho.mqtt.client as mqtt
import time

# MQTT client setup
mqtt_broker = "mqtt.beia-telemetrie.ro"  # Replace with your MQTT broker address
mqtt_port = 1883
mqtt_topic = "training/device/Craciun-Razvan"

# Function to generate random temperature and humidity data
def generate_data():
    temperature = random.uniform(5.0, 40.0)
    humidity = random.uniform(30.0, 60.0)
    return {"temperature": temperature, "humidity": humidity}

# Callback function that runs when the MQTT client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Successfully connected to MQTT Broker with result code {str(rc)}")
    else:
        print(f"Connection failed with return code {rc}")

client = mqtt.Client()

# Assign the on_connect callback function to the client
client.on_connect = on_connect

# Establish connection to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Loop to continuously generate and publish data
try:
    while True:
        data = generate_data()
        payload = json.dumps(data)
        client.publish(mqtt_topic, payload)
        print(f"Published data: {payload} to topic {mqtt_topic}")
        time.sleep(5)  # Wait for 5 seconds before publishing next set of data
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.disconnect()
