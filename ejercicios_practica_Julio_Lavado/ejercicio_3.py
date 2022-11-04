# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados elif

# Objetico
# Verificar la calificación de un estudiante según su
# puntaje en un examen
puntaje_1 = input("Ingrese la nota = ")

# Alumno:
# Deberá crear una serie de considiconales
# con if y elif de forma tal de cargar en
# la variable nota la nota del alumno según
# las siguientes condiciones:
if puntaje_1.isdigit():
    puntaje = int(puntaje_1)

    if puntaje >= 90:
        nota = "A"
        print(f'{nota}')

    elif puntaje >= 80:
        nota = "B"
        print(f'{nota}')

    elif puntaje >= 70:
        nota = "C"
        print(f'{nota}')

    elif puntaje >= 60:
        nota = "D"
        print(f'{nota}')

    elif puntaje < 60:
        nota = "F"
        print(f'{nota}')
else:
    print("Ingrese un Número")


# Si el puntaje es mayor igual a 90 --> nota = "A"
# Si el puntaje es mayor igual a 80 --> nota = "B"
# Si el puntaje es mayor igual a 70 --> nota = "C"
# Si el puntaje es mayor igual a 60 --> nota = "D"
# Si el puntaje es menor a  60      --> nota = "F"

# Recuerde utilizar un solo bloque condicional
# armado de if y múltiples elif
# Puede consultar el ejemplo de clase 2 como referencia

# Imprimir en pantalla la variable nota
