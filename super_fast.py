# **********************
# ANIMALES SUPER RÁPIDOS
# **********************

def run(speed_km_h: float) -> float:
    # Cálculo de la velocidad en cm/s a partir de km/h
    speed_cm_s = (speed_km_h * 100000) / 3600
    return speed_cm_s

if __name__ == '__main__':
    speed_km_h = 1.08
    speed_cm_s = run(speed_km_h)
    print(f"La velocidad de {speed_km_h} km/h es {speed_cm_s:.2f} cm/s")
