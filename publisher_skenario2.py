import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)

client.loop_start() 

print("Memulai Pengiriman Data Skenario 2...")
print("=" * 65)

try:
    while True:
        waktu = datetime.now().strftime("%H:%M:%S")
        
        suhu = round(random.uniform(20.0, 30.0), 1)
        kelembapan = random.randint(40, 75)
        tekanan = random.randint(1000, 1025)
        
        # Mengirim data dengan level QoS berbeda
        client.publish("smartroom/ruang1/suhu", f"{suhu} C", qos=0)
        client.publish("smartroom/ruang1/kelembapan", f"{kelembapan} %", qos=1)
        client.publish("smartroom/ruang1/tekanan", f"{tekanan} hPa", qos=2)
        
        print(f"[{waktu}] Kirim [QoS 0] smartroom/ruang1/suhu       : {suhu} C")
        print(f"[{waktu}] Kirim [QoS 1] smartroom/ruang1/kelembapan : {kelembapan} %")
        print(f"[{waktu}] Kirim [QoS 2] smartroom/ruang1/tekanan    : {tekanan} hPa")
        print("-" * 65)
        
        time.sleep(3)

except KeyboardInterrupt:
    print("\nPengiriman dihentikan.")
    client.loop_stop() # Hentikan loop background saat keluar
    client.disconnect()