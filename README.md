# autonomo2
# 🎮 Juego del Ahorcado en Python

Este es un proyecto simple del clásico juego del **Ahorcado**, desarrollado en Python. El programa selecciona una palabra al azar y el jugador debe adivinarla letra por letra antes de quedarse sin vidas.



## Características

* Selección aleatoria de palabras
* Sistema de vidas (6 intentos)
* Visualización del progreso con guiones (`_`)
* Actualización dinámica de letras correctas
* Mensajes de victoria o derrota



## ¿Cómo funciona?

1. El programa elige una palabra al azar de una lista.
2. Se muestran guiones representando cada letra.
3. El usuario ingresa una letra.
4. Si la letra está en la palabra:

   * Se revela en la posición correcta.
5. Si no está:

   * Se pierde una vida.
6. El juego termina cuando:

   * Se adivina la palabra ✅
   * Se acaban las vidas ❌



## Código

```python
import random as r

def ahorcado():
    palabra = ["pelota", "casa", "carro"]
    eleccion = r.choice(palabra)
    vidas = 6
    palabra_adivinada = ["_"] * len(eleccion)

    while vidas > 0 and "_" in palabra_adivinada:
        print(" ".join(palabra_adivinada))
        letra = input("dime una letra: ")

        if letra in eleccion:
            for i, let in enumerate(eleccion):
                if let == letra:
                    palabra_adivinada[i] = letra
        else:
            vidas -= 1
            print(f"te quedan {vidas} vidas")

    if "_" not in palabra_adivinada:
        print("felicidades ganaste")
    else:
        print("lo siento perdiste")

ahorcado()


## Posibles mejoras

* Agregar más palabras
* Evitar letras repetidas
* Mostrar letras ya usadas
* Añadir dificultad (fácil, medio, difícil)


##  Autor

Desarrollado por **Brando Medina** como práctica de programación en Python.


##  Tecnologías usadas

* Python 3
* Módulo `random`

