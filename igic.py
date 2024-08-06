# ***************
# PRECIO SIN IGIC
# ***************

def run(price_with_igic: float, igic: float) -> float:
    # Cálculo del precio sin IGIC
    clean_price = price_with_igic / (1 + igic / 100)
    return clean_price

if __name__ == '__main__':
    price_with_igic = 120
    igic = 7
    clean_price = run(price_with_igic, igic)
    print(f"El precio sin IGIC es {clean_price:.2f}")
