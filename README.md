# autonomo2
Juego del el Ahorcado en Python
Descripción
Este proyecto consiste en la implementación básica del juego del ahorcado utilizando el lenguaje de programación Python.
El programa selecciona una palabra aleatoria de una lista y el usuario debe adivinarla ingresando letras.
Tecnologías utilizadas
Lenguaje: Python 3
Librerías:
random (librería estándar de Python)
La librería random pertenece a la biblioteca estándar de Python, por lo que no requiere instalación adicional.
Se utiliza para seleccionar una palabra aleatoria de una lista.

import random as r
Palabra_elegida = r.choice(PALABRAS)

Funcionamiento del programa

El programa sigue estos pasos:

Se define una lista de palabras:
PALABRAS = ["escuela", "aereopuerto", "casa", "pelota", "leon"]
Se selecciona una palabra aleatoria:
Palabra_elegida = r.choice(PALABRAS)
Se genera una representación oculta de la palabra usando guiones bajos:
for letra in Palabra_elegida:
    generador_de_espacio += "_ "
El usuario ingresa una letra:
letra_usuario = input("Ingrese una Letra ")
Se verifica si la letra ingresada está en la palabra:
for validacion in Palabra_elegida:
    if validacion == letra_usuario:
        reemplazar_espacio += letra_usuario

        Lógica del juego
Se recorre la palabra letra por letra usando un ciclo for
Se compara cada letra con la ingresada por el usuario
Si coincide, se reemplaza el guion bajo _ por la letra correcta
El proceso se repite hasta completar la palabra

Estado del proyecto

 En desarrollo

Actualmente el programa:

Selecciona palabras aleatorias
Permite ingresar letras
Realiza validaciones básicas

Futuras mejoras:

Guardar letras correctas
Contador de intentos
Mensaje de victoria/derrota
