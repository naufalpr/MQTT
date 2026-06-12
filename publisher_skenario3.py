import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Pub_Skenario3")
client.connect("localhost", 1883)

print("Memulai Skenario 3...")
try:
    while True:
        waktu = datetime.now().strftime("%H:%M:%S")
        suhu_r1 = round(random.uniform(22.0, 26.0), 1)
        cahaya_r1 = random.choice(["Terang", "Normal", "Redup", "Gelap"])
        suhu_r2 = round(random.uniform(18.0, 24.0), 1)
        
        client.publish("smartroom/ruang1/suhu", f"{suhu_r1} C")
        client.publish("smartroom/ruang1/cahaya", cahaya_r1)
        client.publish("smartroom/ruang2/suhu", f"{suhu_r2} C")
        
        # Menampilkan detail di terminal publisher
        print(f"[{waktu}] Terkirim [smartroom/ruang1/suhu]   : {suhu_r1} C")
        print(f"[{waktu}] Terkirim [smartroom/ruang1/cahaya] : {cahaya_r1}")
        print(f"[{waktu}] Terkirim [smartroom/ruang2/suhu]   : {suhu_r2} C")
        print("-" * 60)
        
        time.sleep(3)
except KeyboardInterrupt:
    client.disconnect()