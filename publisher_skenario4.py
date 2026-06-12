import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Pub_Skenario4")
client.connect("localhost", 1883)

print("Memulai Skenario 4...")
status_options = ["ON", "OFF", "STANDBY"]

try:
    while True:
        waktu = datetime.now().strftime("%H:%M:%S")
        
        # Simpan nilai random ke variabel agar bisa di-print
        ac_r1 = random.choice(status_options)
        ac_r2 = random.choice(status_options)
        ac_r3 = random.choice(status_options)
        
        client.publish("smartroom/ruang1/ac_status", ac_r1)
        client.publish("smartroom/ruang2/ac_status", ac_r2)
        client.publish("smartroom/ruang3/ac_status", ac_r3)
        
        # Menampilkan detail di terminal publisher
        print(f"[{waktu}] Terkirim [smartroom/ruang1/ac_status] : {ac_r1}")
        print(f"[{waktu}] Terkirim [smartroom/ruang2/ac_status] : {ac_r2}")
        print(f"[{waktu}] Terkirim [smartroom/ruang3/ac_status] : {ac_r3}")
        print("-" * 60)
        
        time.sleep(4)
except KeyboardInterrupt:
    client.disconnect()