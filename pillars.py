# **********************
# POSTES EN LA CARRETERA
# **********************

def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    if num_pillars <= 1:
        return 0

    # Cálculo de la distancia total entre el primer y el último poste
    inter_distance = (num_pillars - 1) * gap_pillars + (num_pillars - 2) * pillar_width
    return inter_distance


if __name__ == '__main__':
    num_pillars = 10
    gap_pillars = 5
    pillar_width = 30
    total_distance = run(num_pillars, gap_pillars, pillar_width)
    print(f"La distancia total entre postes es {total_distance:.2f}")
