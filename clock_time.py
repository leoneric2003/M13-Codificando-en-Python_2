## *********************
# CONTANDO MILISEGUNDOS
# *********************

def run(hours: int, minutes: int, seconds: int) -> float:
    # Cálculo del tiempo transcurrido desde la medianoche en milisegundos
    time_since_midnight = (hours * 3600 + minutes * 60 + seconds) * 1000
    return time_since_midnight

if __name__ == '__main__':
    hours = 0
    minutes = 1
    seconds = 1
    time_in_milliseconds = run(hours, minutes, seconds)
    print(f"El tiempo transcurrido desde la medianoche es {time_in_milliseconds:.0f} milisegundos")
