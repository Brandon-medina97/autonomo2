# Importa la librería random y la renombra como 'r'
import random as r
# defino la funcion del juego
def ahorcado():
    #se crea una lista en la variable palabra 
    palabra =["pelota", "casa", "carro"]
    #selecciono una palabra alazar
    eleccion = r.choice(palabra)
    # indico el numero de vidas o intentos 
    vidas = 6
    # Crea una lista de "_" según la longitud de la palabra
    palabra_adivinada =["_"] * len(eleccion)
# Bucle principal: se ejecuta mientras haya vidas y letras por adivinar
    while vidas > 0 and "_" in palabra_adivinada:
        # muestra el progreso actual
        print (" ".join(palabra_adivinada))
        # pide al usuario una letra 
        letra = input("dime una letra: ")
        #verifica que la letra se encuentre en la palabra
        if letra in eleccion:
            # Recorre la palabra con su índice usando enumerate
            for i, let in enumerate(eleccion):
                # si la letra coinciden
                if let == letra:
                    #remplaza "_" por la letra ingresada
                    palabra_adivinada[i] = letra
        #resta una vida si la letra no coincide  
        else:
            vidas -= 1
            #imprime el numero de vidas que le quedan
            print(f"te quedan {vidas} vidas")
    # si ya no quedan "_" ganaste 
    if ("_" not in palabra_adivinada):
        print("felicidades ganaste")
        #si no perdiste
    else:
        print("lo siento perdiste") 
# se llama a la funcion para iniciar el juego 
ahorcado()