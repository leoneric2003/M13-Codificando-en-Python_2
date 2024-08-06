# ******************
# DISTANCIA EUCLÍDEA
# ******************

import math

def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # Cálculo de la distancia euclídea
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

if __name__ == '__main__':
    x1, y1, x2, y2 = 3, 5, -7, -4
    distance = run(x1, y1, x2, y2)
    print(f"La distancia euclídea entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es {distance:.2f}")
