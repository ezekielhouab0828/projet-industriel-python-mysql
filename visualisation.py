import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from read_data import read_mesures

# Charger les données
df = read_mesures()

# Convertir la colonne timestamp en datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Trier par date
df = df.sort_values("timestamp")

# Afficher les courbes
plt.figure(figsize=(12, 6))

plt.plot(df["timestamp"], df["temperature"], label="Température (°C)")
plt.plot(df["timestamp"], df["vibration"], label="Vibration (mm/s)")
plt.plot(df["timestamp"], df["pression"], label="Pression (bar)")
plt.plot(df["timestamp"], df["courant"], label="Courant (A)")

plt.xlabel("Temps")
plt.ylabel("Valeurs")
plt.title("Évolution des mesures de la machine")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(df.tail())