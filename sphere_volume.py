# *********************
# VOLUMEN DE UNA ESFERA
# *********************

import math

def run(radius: float) -> float:
    # Cálculo del volumen de la esfera
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

if __name__ == '__main__':
    radius = 5
    volume = run(radius)
    print(f"El volumen de una esfera con radio {radius} es {volume:.2f}")
