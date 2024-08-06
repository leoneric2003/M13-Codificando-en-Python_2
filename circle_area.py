# ******************
# ÁREA DE UN CÍRCULO
# ******************

import math

def run(radius: float) -> float:
    # Cálculo del área del círculo
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    radius = 4
    area = run(radius)
    print(f'El área de un círculo con radio {radius} es {area:.2f}')
