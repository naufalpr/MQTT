import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg, reason_code=None, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] Data Masuk -> [{msg.topic}]: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sub_Skenario3")
client.on_message = on_message
client.connect("localhost", 1883)

client.subscribe("smartroom/ruang1/suhu")
client.subscribe("smartroom/ruang1/cahaya")
client.subscribe("smartroom/ruang2/suhu")

print("Menunggu pesan Skenario 3 (Multi-topik)...")
client.loop_forever()