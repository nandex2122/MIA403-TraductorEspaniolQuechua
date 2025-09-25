import subprocess
import time
import webbrowser
import requests

# Paso 1: Ejecutar la aplicación Flask
flask_process = subprocess.Popen(["python", "app.py"])

# Esperar a que Flask arranque
time.sleep(3)

# Paso 2: Ejecutar ngrok
ngrok_process = subprocess.Popen(["ngrok", "http", "5000"])

# Esperar a que ngrok genere la URL
time.sleep(5)

# Paso 3: Obtener la URL pública de ngrok
try:
    response = requests.get("http://localhost:4040/api/tunnels")
    tunnels = response.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"?? Tu aplicación Flask está disponible en: {public_url}")
    webbrowser.open(public_url)
except Exception as e:
    print("No se pudo obtener la URL pública de ngrok:", e)