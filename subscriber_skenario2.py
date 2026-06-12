import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg, reason_code=None, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] [QoS {msg.qos}] Topik: {msg.topic} | Isi: {msg.payload.decode()}")

def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        client.subscribe("smartroom/ruang1/suhu", qos=0)
        client.subscribe("smartroom/ruang1/kelembapan", qos=1)
        client.subscribe("smartroom/ruang1/tekanan", qos=2)
        print("Berhasil mendaftarkan topik QoS 0, 1, dan 2.")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sub_Skenario2")
client.on_connect = on_connect
client.on_message = on_message

print("Menghubungkan ke broker...")
client.connect("localhost", 1883)
client.loop_forever()
