# *****************
# INTERÉS COMPUESTO
# *****************

def run(amount: float, rate: float, years: int) -> float:
    # Cálculo del monto futuro con interés compuesto
    future_amount = amount * (1 + rate / 100) ** years
    return future_amount

if __name__ == '__main__':
    amount = 10000
    rate = 3.5
    years = 7
    future_amount = run(amount, rate, years)
    print(f"El monto futuro de una inversión de {amount} con una tasa de interés de {rate}% durante {years} años es {future_amount:.2f}")
