# Smart Room Monitoring — MQTT dengan Python & Mosquitto

Sistem simulasi pemantauan ruangan cerdas menggunakan protokol MQTT,
Python (paho-mqtt), dan Eclipse Mosquitto Broker di Windows.

---

## Prasyarat

Pastikan perangkat memiliki:
- Windows 10 / 11
- Python 3.8 atau lebih baru
- Eclipse Mosquitto Broker
- Library paho-mqtt

---

## Langkah 1 — Install Python

1. Download Python di https://www.python.org/downloads/
2. Saat instalasi, centang **"Add Python to PATH"** sebelum klik Install Now
3. Verifikasi instalasi dengan membuka Command Prompt dan ketik:

   python --version

---

## Langkah 2 — Install Mosquitto Broker

1. Download installer Mosquitto di https://mosquitto.org/download/
2. Pilih versi **Windows (64-bit)** lalu jalankan installer
3. Saat proses instalasi, centang opsi **"Install as a Windows Service"**
4. Setelah selesai, buka **PowerShell sebagai Administrator** dan jalankan:

   net start mosquitto

5. Verifikasi broker berjalan dengan perintah:

   netstat -an | findstr 1883

   Jika muncul baris dengan status **LISTENING** pada port 1883, broker siap digunakan.

---

## Langkah 3 — Install Library paho-mqtt

Buka Command Prompt lalu jalankan:

   pip install paho-mqtt

---

## Langkah 4 — Struktur Folder

Pastikan semua file program berada dalam satu folder, contohnya:

   C:\smartroom-fix\
   ├── publisher_skenario1.py
   ├── subscriber_skenario1.py
   ├── publisher_skenario2.py
   ├── subscriber_skenario2.py
   ├── publisher_skenario3.py
   ├── subscriber_skenario3.py
   ├── publisher_skenario4.py
   ├── subscriber_skenario4.py
   ├── publisher_skenario5.py
   └── subscriber_skenario5.py

---

## Langkah 5 — Menjalankan Setiap Skenario

> **Penting:** Setiap skenario membutuhkan DUA jendela PowerShell/Command Prompt
> yang berjalan secara bersamaan. Selalu jalankan Subscriber terlebih dahulu,
> baru kemudian Publisher.

Buka folder program terlebih dahulu di setiap terminal:

   cd C:\smartroom-fix

---

### Skenario 1 — Komunikasi Dasar Publisher–Subscriber

**Terminal 1 (Subscriber):**

   python subscriber_skenario1.py

**Terminal 2 (Publisher):**

   python publisher_skenario1.py

---

### Skenario 2 — Pengiriman Data dengan QoS Berbeda (QoS 0, 1, 2)

**Terminal 1 (Subscriber):**

   python subscriber_skenario2.py

**Terminal 2 (Publisher):**

   python publisher_skenario2.py

---

### Skenario 3 — Penggunaan Beberapa Topik

**Terminal 1 (Subscriber):**

   python subscriber_skenario3.py

**Terminal 2 (Publisher):**

   python publisher_skenario3.py

---

### Skenario 4 — Penggunaan Wildcard +

**Terminal 1 (Subscriber):**

   python subscriber_skenario4.py

**Terminal 2 (Publisher):**

   python publisher_skenario4.py

---

### Skenario 5 — Penggunaan Wildcard #

**Terminal 1 (Subscriber):**

   python subscriber_skenario5.py

**Terminal 2 (Publisher):**

   python publisher_skenario5.py

---

## Menghentikan Program

Tekan **Ctrl + C** pada terminal Publisher untuk menghentikan pengiriman data,
kemudian tekan **Ctrl + C** pada terminal Subscriber untuk keluar.

---

## Menghentikan dan Memulai Ulang Mosquitto

Buka PowerShell sebagai Administrator:

   # Menghentikan broker
   net stop mosquitto

   # Memulai ulang broker
   net start mosquitto

---

## Troubleshooting

| Masalah | Penyebab | Solusi |
|---|---|---|
| `Connection refused` | Mosquitto belum berjalan | Jalankan `net start mosquitto` di PowerShell Admin |
| `ModuleNotFoundError: paho` | Library belum terinstall | Jalankan `pip install paho-mqtt` |
| Subscriber tidak menerima pesan | Publisher dijalankan lebih dulu | Restart subscriber, jalankan sebelum publisher |
| Port 1883 tidak ditemukan | Mosquitto tidak aktif | Cek Services Windows, cari Mosquitto, klik Start |
| `python` tidak dikenali | Python belum ada di PATH | Reinstall Python, centang "Add Python to PATH" |
| Pesan terduplikat (QoS 1) | Perilaku normal QoS 1 | Bukan error, QoS 1 memang at-least-once |
