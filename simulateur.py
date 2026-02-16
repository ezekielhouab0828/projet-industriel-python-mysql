import random
import time
from insert_mesure import insert_mesure

def generer_mesure():
    temp = round(random.uniform(20.0, 80.0), 2)
    vib = round(random.uniform(0.01, 0.10), 3)
    press = round(random.uniform(0.8, 1.5), 2)
    courant = round(random.uniform(2.0, 5.0), 2)

    anom_temp = temp > 70
    anom_vib = vib > 0.08
    anom_press = press < 0.9 or press > 1.3
    anom_courant = courant > 4.5

    return {
        "temp": temp,
        "vib": vib,
        "press": press,
        "courant": courant,
        "anom_temp": anom_temp,
        "anom_vib": anom_vib,
        "anom_press": anom_press,
        "anom_courant": anom_courant
    }

def envoyer_mesure(id_machine):
    m = generer_mesure()
    insert_mesure(
        id_machine=id_machine,
        temp=m["temp"],
        vib=m["vib"],
        press=m["press"],
        courant=m["courant"],
        anom_temp=m["anom_temp"],
        anom_vib=m["anom_vib"],
        anom_press=m["anom_press"],
        anom_courant=m["anom_courant"]
    )
    print(f"Mesure insérée : {m}")

# Boucle infinie : une mesure toutes les 5 secondes
while True:
    envoyer_mesure(id_machine=1)
    time.sleep(5)