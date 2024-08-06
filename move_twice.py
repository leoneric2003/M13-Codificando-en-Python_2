# *******************
# TIRO PORQUE ME TOCA
# *******************

def run(current_pos: int, dice: int) -> int:
    # Cálculo de la nueva posición en el tablero
    final_pos = current_pos + dice
    return final_pos

if __name__ == '__main__':
    current_pos = 3
    dice = 6
    final_pos = run(current_pos, dice)
    print(f"La nueva posición después de tirar el dado es {final_pos}")
