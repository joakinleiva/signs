import math

#VARIABLES UNIVERSALES

METALCON = 600
VEINTEX20 = 600
ANGULO40 = 600
ZINCGALVANIZADO = 600

#Calculo metalcom

def perfiles_zinc_necesarios(ancho, alto):
    # Calcula la suma de todos los lados del letrero rectangular
    suma_lados = (ancho * 2) + (alto * 2)

    # Calcula la cantidad de perfiles de zinc necesarios
    perfiles_necesarios = suma_lados / 600

    # Redondea hacia arriba para asegurarse de tener suficientes perfiles
    perfiles_necesarios = math.ceil(perfiles_necesarios)

    return perfiles_necesarios

#Calculo zinc galvanizado
def laminas_zinc_necesarias(ancho, alto):
    # Calcula cuántas láminas de zinc de 300x100 cm necesitas
    laminas_ancho = ancho // 300
    laminas_alto = alto // 100
    laminas_necesarias = laminas_ancho * laminas_alto

    if ancho % 300 != 0:
        laminas_ancho += 1

    if alto % 100 != 0:
        laminas_alto += 1

    return laminas_ancho * laminas_alto

# Ingreso de medidas
print(" ")
ancho = int(input("Ingresa \033[1;1mancho\033[0m del letrero (CM):  "))
print(" ")
alto = int(input("Ingresa \033[1;1malto\033[0m del letrero (CM): "))
print(" ")

# Calculo diagonal
preDiagonal = (ancho ** 2 + alto ** 2)
diagonal = math.sqrt(preDiagonal)

# Impresion de informacion

print(f"Ancho: {ancho} CM")
print(f"Alto: {alto} CM")
print(f"Longitud de la diagonal: {int(diagonal)} CM")

# Calcula la cantidad de perfiles de zinc necesarios y muestra el resultado
print(" ")
perfiles = perfiles_zinc_necesarios(ancho, alto)

laminas = laminas_zinc_necesarias(ancho, alto)

print("==========================")

print(f"Necesitas {perfiles} perfil(es) de Metalcon de 150x40 de 0.85 de espesor para el letrero.")
print(" ")
print(f"Necesitas {laminas} láminas de zinc de 300x100 cm para cubrir el letrero.")
