import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg, reason_code=None, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] [Wildcard #] Tangkapan: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sub_Skenario5")
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("smartroom/ruang2/#")

print("Menunggu pesan Skenario 5 (Wildcard # khusus Ruang 2)...")
client.loop_forever()