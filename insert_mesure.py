from sqlalchemy import text
from db import get_engine

def insert_mesure(id_machine, temp, vib, press, courant,
                  anom_temp, anom_vib, anom_press, anom_courant):

    engine = get_engine()

    with engine.connect() as connection:
        connection.execute(
            text("""
                INSERT INTO mesures (
                    timestamp, id_machine, temperature, vibration, pression, courant,
                    anom_temp, anom_vib, anom_press, anom_courant
                ) VALUES (
                    NOW(), :id_machine, :temp, :vib, :press, :courant,
                    :anom_temp, :anom_vib, :anom_press, :anom_courant
                )
            """),
            {
                "id_machine": id_machine,
                "temp": temp,
                "vib": vib,
                "press": press,
                "courant": courant,
                "anom_temp": anom_temp,
                "anom_vib": anom_vib,
                "anom_press": anom_press,
                "anom_courant": anom_courant
            }
        )