import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Pub_Skenario5")
client.connect("localhost", 1883)

print("Memulai Skenario 5...")
try:
    while True:
        waktu = datetime.now().strftime("%H:%M:%S")
        
        # Generate data dan simpan ke variabel
        suhu_r2 = f"{round(random.uniform(20, 25), 1)} C"
        kel_r2 = f"{random.randint(45, 60)} %"
        pintu_r2 = random.choice(["Terkunci", "Terbuka"])
        suhu_r1 = f"{round(random.uniform(26, 30), 1)} C" # Data pengecoh
        
        # Kirim data ke broker
        client.publish("smartroom/ruang2/suhu", suhu_r2)
        client.publish("smartroom/ruang2/kelembapan", kel_r2)
        client.publish("smartroom/ruang2/keamanan/pintu/utama", pintu_r2) 
        client.publish("smartroom/ruang1/suhu", suhu_r1) 
        
        # Menampilkan detail di terminal publisher
        print(f"[{waktu}] Terkirim [smartroom/ruang2/suhu]                  : {suhu_r2}")
        print(f"[{waktu}] Terkirim [smartroom/ruang2/kelembapan]            : {kel_r2}")
        print(f"[{waktu}] Terkirim [smartroom/ruang2/keamanan/pintu/utama]  : {pintu_r2}")
        print(f"[{waktu}] Terkirim [smartroom/ruang1/suhu] (Data Pengecoh)  : {suhu_r1}")
        print("-" * 70)
        
        time.sleep(3)
except KeyboardInterrupt:
    client.disconnect()