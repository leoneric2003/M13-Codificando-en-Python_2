# ****************
# EL CUADRADO ROJO
# ****************

def run(arc_A: float) -> float:
    # Cálculo del área del cuadrado
    area = arc_A ** 2
    return area

if __name__ == '__main__':
    arc_A = 1
    area = run(arc_A)
    print(f"El área de un cuadrado con lado {arc_A} es {area:.2f}")
