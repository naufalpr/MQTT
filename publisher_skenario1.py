import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

# Inisialisasi MQTT Client versi 2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Pub_Skenario1_Final")
client.connect("localhost", 1883, 60)

print("Memulai Pengiriman Data Skenario 1 ...")

try:
    while True:
        waktu = datetime.now().strftime("%H:%M:%S")
        
        # Generate nilai acak intensitas cahaya (Lux)
        cahaya_lux = random.randint(150, 800)
        pesan_dikirim = f"{cahaya_lux} Lux"
        
        # Publish ke broker
        client.publish("smartroom/ruang1/cahaya", pesan_dikirim)
        
        # Menampilkan log pengiriman secara detail di terminal publisher
        print(f"[{waktu}] Terkirim -> [smartroom/ruang1/cahaya] : {pesan_dikirim}")
        
        # Jeda pengiriman data setiap 3 detik
        time.sleep(3)

except KeyboardInterrupt:
    print("\nPengiriman data dihentikan oleh pengguna.")
    client.disconnect()