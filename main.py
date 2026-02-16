from insert_mesure import insert_mesure
from read_data import read_machines, read_mesures

print("Machines enregistrées :")
print(read_machines())

insert_mesure(
    id_machine=1,
    temp=22.5,
    vib=0.03,
    press=1.02,
    courant=3.5,
    anom_temp=False,
    anom_vib=False,
    anom_press=False,
    anom_courant=False
)

print("Mesures enregistrées :")
print(read_mesures())