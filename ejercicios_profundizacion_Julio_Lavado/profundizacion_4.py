# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Objetizo:
Realizar un programa que solicite ingresar
tres valores decimales de temperatura
De las temperaturas ingresadas se determinará:
1 - ¿Cuál es suma de todas las temperaturas ingresadas?
2 - ¿Cuál es el promedio de las temperaturas ingresadas?

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.

Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Utilizando el operador suma o el operador incremento
deberá almacenar la suma de todas las temperaturas
ingresadas en una nueva variable llamada "temperatura_total"

Luego, mediante el uso de la variable "temperatura_total"
y teniendo en cuenta que se ingresaron tres temperaturas.
Deberá calcular el promedio de todas las temperaturas
y almacenar el resultado en una variable llamada
"temperatura_promedio"

- Al final imprimir en pantalla la variable 
  temperatura_promedio
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temperatura_1 = float(input("Ingrese la medicion de temperatura 1 = "))
temperatura_2 = float(input("Ingrese la medicion de temperatura 2 = "))
temperatura_3 = float(input("Ingrese la medicion de temperatura 3 = "))

temperatura_total = temperatura_1 + temperatura_2 + temperatura_3
print(f'La suma de las temperaturas ingresadas es : {temperatura_total};')
print(f'El promedio de las temperaturas ingresadas es: {(temperatura_total)/3};')


if temperatura_1 > temperatura_2:
  if temperatura_1 > temperatura_3:
    temperatura_max = temperatura_1
    print(f'El mayor es el primer valor ingresado, {temperatura_max}')
    if temperatura_2 > temperatura_3:
      temperatura_min = temperatura_3
      print(f'El menor es el tercer valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_2},{temperatura_min}')
    else:
      temperatura_min = temperatura_2
      print(f'El menor es el segundo valor ingresado, {temperaturamin}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_3},{temperatura_min}')
  else:
    temperatura_max = temperatura_3
    print(f'El mayor es el tercer valor ingresado, {temperatura_max}')
    if temperatura_1 > temperatura_2:
      temperatura_min = temperatura_2
      print(f'El menor es el segundo valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_1},{temperatura_min}')
    else:
      temperatura_min = temperatura_1
      print(f'El menor es el primer valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_2},{temperatura_min}')
else:
  if temperatura_2 > temperatura_3:
    temperatura_max = temperatura_2
    print(f'El mayor es el segundo valor ingresado, {temperatura_max}')
    if temperatura_3 > temperatura_1:
      temperatura_min = temperatura_1
      print(f'El menor es el primer valor ingresado, {temperatura_1}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_3},{temperatura_min}')
    else:
      temperatura_min = temperatura_3
      print(f'El menor es el tercer valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_1},{temperatura_min}')
  
  else:
    temperatura_max = temperatura_3
    print(f'El mayor es el tercer valor ingresado, {temperatura_max}')
    if temperatura_2 > temperatura_1:
      temperatura_min = temperatura_1
      print(f'El menor es el primer valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_2},{temperatura_min}')
    else:
      temperatura_min = temperatura_2
      print(f'El menor es el segundo valor ingresado, {temperatura_min}')
      print(f'El Orden de mayor a menor es {temperatura_max},{temperatura_1},{temperatura_min}')



print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
