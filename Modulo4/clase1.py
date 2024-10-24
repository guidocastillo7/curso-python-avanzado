"""
OPERACIONES ARITMETICAS AVANZADAS
Documentacion: https://docs.python.org/es/3.10/library/math.html
"""
import math

# Constantes matematicas
print("Valor de pi: ", math.pi)
print("Valor de numero Euler: ", math.e)


# Funciones trigonometricas
angulo = math.radians(45)
print(angulo)
print("Seno: ", math.sin(angulo))
print("Coseno: ", math.cos(angulo))
print("Tangente: ", math.tan(angulo))


# Funciones exponenciales
print("Exponencial: ", math.exp(2))


# Funciones logaritmicas
print("Logaritmo de 10: ", math.log(10))


# Potencias
print("Potencia 2 elevado a 3: ", math.pow(2, 3))


# Raiz cuadrada
print("Raiz cuadrada de 25: ", math.sqrt(25))


# FRACCIONES
from fractions import Fraction
tres_cuartos = Fraction(3, 4)
un_octavo = Fraction(1, 8)
print("Fracciones: ", tres_cuartos, un_octavo)

# Podemos sumar, restar, multiplicar y dividir las fracciones
print("Sumar fracciones: ", tres_cuartos + un_octavo)
print("Restar fracciones: ", tres_cuartos - un_octavo)
print("Multiplicar fracciones: ", tres_cuartos * un_octavo)
print("Dividir fracciones: ", tres_cuartos / un_octavo)


# DECIMALES 
from decimal import Decimal, getcontext

getcontext().prec = 10
num1 = Decimal("0.000256")
num2 = Decimal("0.000625")
print("Suma de decimales: ", num1 + num2)