 
import math

# Paso 1: Solicitar al usuario que ingrese el radio del circulo que quiere calcular



radio= float(input('Porfavor, ingresa el radio del circulo: '))


# Paso 2: calcular el area del circulo utilizando la formula are = pi * radio al cuadrado

area= math.pi * (radio **2)


# Paso 3: Mostrar al usuario el area calculada

print('El area del circulo con radio ',radio, 'es:', area)