# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************

def run(year: int) -> int:
    # Cálculo del siglo correspondiente al año dado
    if year % 100 == 0:
        century = year // 100
    else:
        century = (year // 100) + 1
    return century

if __name__ == '__main__':
    year = 1705
    century = run(year)
    print(f"El año {year} corresponde al siglo {century}")
