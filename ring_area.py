# ***************
# ÁREA DEL ANILLO
# ***************

import math

def run(R: float, r: float) -> float:
    # Cálculo del área del anillo
    if R <= r:
        raise ValueError("El radio externo debe ser mayor que el radio interno.")
    white_area = math.pi * (R**2 - r**2)
    return white_area

if __name__ == '__main__':
    R = 5
    r = 2
    try:
        area = run(R, r)
        print(f"El área del anillo con radio externo {R} y radio interno {r} es {area:.2f}")
    except ValueError as e:
        print(e)
