
import streamlit as st
import requests

ESP_IP = "http://192.168.4.1"  # Ganti dengan IP ESP-mu

st.set_page_config(page_title="Team 39 STI Pekanbaru", layout="centered")
st.title("🌐 Team 39 STI Pekanbaru")
st.subheader("📡 Sensor Ultrasonic & ⚙️ Kontrol Servo")

def get_distance():
    try:
        response = requests.get(f"{ESP_IP}/distance", timeout=2)
        return response.json().get("distance")
    except:
        return None

def set_servo(angle):
    try:
        response = requests.get(f"{ESP_IP}/servo?angle={angle}", timeout=2)
        return response.text
    except:
        return "❌ Gagal mengirim perintah ke ESP"

# Sensor Data
distance = get_distance()
if distance is not None:
    st.metric("Jarak Ultrasonic", f"{distance} cm")
else:
    st.error("❌ Tidak bisa membaca sensor")

# Servo Control
st.subheader("🕹️ Atur Sudut Servo")
angle = st.slider("Sudut Servo", 0, 180, 90)
if st.button("Kirim ke Servo"):
    result = set_servo(angle)
    st.success(f"Respons dari ESP: {result}")
