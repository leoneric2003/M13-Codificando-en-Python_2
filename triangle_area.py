# ********************
# ÁREA DE UN TRIÁNGULO
# ********************

def run(base: float, height: float) -> float:
    # Cálculo del área del triángulo
    area = (base * height) / 2
    return area

if __name__ == '__main__':
    base = 3
    height = 3
    area = run(base, height)
    print(f"El área de un triángulo con base {base} y altura {height} es {area:.2f}")
