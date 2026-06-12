import paho.mqtt.client as mqtt
from datetime import datetime

# Callback v2 dengan 5 argumen wajib
def on_message(client, userdata, msg, reason_code=None, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] Topik: {msg.topic} | Pesan: {msg.payload.decode()}")

def on_connect(client, userdata, flags, reason_code, properties=None):
    waktu = datetime.now().strftime("%H:%M:%S")
    if reason_code == 0:
        print(f"[{waktu}] Berhasil terhubung ke Mosquitto Broker")
        # Melakukan subscribe tepat setelah sukses terkoneksi
        client.subscribe("smartroom/ruang1/cahaya")
        print(f"[{waktu}] Berhasil subscribe ke topik: smartroom/ruang1/cahaya")
    else:
        print(f"[{waktu}] Gagal terkoneksi, kode error: {reason_code}")

# Inisialisasi MQTT Client versi 2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sub_Skenario1_Final")
client.on_connect = on_connect
client.on_message = on_message

print("Menghubungkan ke Mosquitto Broker...")
client.connect("localhost", 1883, 60)

# Loop selamanya untuk mendengarkan kiriman data
client.loop_forever()