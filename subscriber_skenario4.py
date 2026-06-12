import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg, reason_code=None, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] [Wildcard +] Topik: {msg.topic} | Status: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sub_Skenario4")
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("smartroom/+/ac_status")

print("Menunggu pesan Skenario 4 (Wildcard +)...")
client.loop_forever()