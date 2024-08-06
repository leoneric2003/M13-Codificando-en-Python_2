# ***
# XOR
# ***

def run(v1: bool, v2: bool) -> bool:
    # Cálculo de la operación XOR
    xor = v1 != v2  # Otra forma de calcular XOR en Python
    return xor

if __name__ == '__main__':
    test_cases = [(False, False), (False, True), (True, False), (True, True)]
    for v1, v2 in test_cases:
        result = run(v1, v2)
        print(f"El resultado de XOR({v1}, {v2}) es {result}")

