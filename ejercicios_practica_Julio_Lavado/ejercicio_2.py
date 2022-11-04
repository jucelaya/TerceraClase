# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Objetivo:
# Ingrese dos palabras cualesquiera
# y realice las sigueintes comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable o la cree con ese valor

# Compare las dos palabras y entre sí 
# utilizando if y else.
# - Si texto_1 es mayor (alfabéticamente) a texto_2, 
#   almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
if texto_1 > texto_2:
    res_1 = 1
    print(f'el primer texto es mayor (alfabeticamente) al segundo texto; Codigo = {res_1}')
else:
    res_1 = 2
    print(f'El segundo texto es mayor (alfabeticamente) al primer texto; Codigo = {res_1}')


# Imprimir en pantalla la variable res_1

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Utilice if, elif y else
# - Si texto_1 tiene más letras, almacenar 1 en res_2
# - Si texto_2 tiene más letras, almacenar 2 en res_2
# - Si tienen la misma cantidad de letras, almacenar 3 en res_2

if len(texto_1) > len(texto_2):
    res_2 = 1
    print(f'El primer texto es de mayor longitudinalmente que el segundo texto; Codigo = {res_2}')
    
else:
    if len(texto_2) > len(texto_1):
        res_2 = 2
        print(f'El segundo texto es de mayor longitudinalmente que el primer texto; Codigo = {res_2}')
    else:
        res_2 = 3
        print(f'Tienen igual longitud; Codigo = {res_2}')

# Imprimir en pantalla la variable res_2



# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# - Si la primera letra de texto_1 es mayor,
#   almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3

primera_letra_texto1 = texto_1[0]
primera_letra_texto2 = texto_2[0]

if primera_letra_texto1 > primera_letra_texto2:
    res_3 = 1
    print(f'La primera letra del primer texto es mayor alfaticamente a ala primera letra del segundo texto; Codigo = {res_3}')
else:
    res_3 = 2
    print(f'La primera letra del segundo texto es mayor alfaticamente a la primera letra del primer texto; Codigo = {res_3}')


# Imprimir en pantalla la variable res_3

