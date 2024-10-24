"""
DECIMALES Y REDONDEOS
"""

from decimal import *

num1 = Decimal("10.365")
num2 = Decimal("5.245")

print("Sumar decimales: ", num1 + num2)
print("Restar decimales: ", num1 - num2)
print("Dividir decimales: ", num1 / num2)

division = num1 / num2
# Redondear a 2 decimales
redondeo_2 = division.quantize(Decimal("0.00"))
print("Redondeo a 2 decimales", redondeo_2)

# Redondear hacia arriba
redondeo_alza = division.quantize(Decimal("1.00"), rounding=ROUND_CEILING)
print("Redondeo arriba", redondeo_alza)

# Redondear hacia abajo
redondeo_baja = division.quantize(Decimal("1.00"), rounding=ROUND_FLOOR)
print("Redondeo abajo", redondeo_baja)

# Redondear al mas cercano
redondeo_cercano = division.quantize(Decimal("1.00"), rounding=ROUND_HALF_EVEN)
print("Redondeo cercano: ", redondeo_cercano)