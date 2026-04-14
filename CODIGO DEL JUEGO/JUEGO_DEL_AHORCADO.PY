# se importo la libreria random
import random as r

#SE CREO UNA LISTA DE PALABRAS.
PALABRAS = ["escuela","aereopuerto","casa" ,"pelota" ,"leon"]

#Creamos la variable remplezar_palabra con un espacio para utlizarlo despues
generador_de_espacio = ""
remplazar_espacio = ""
# generar palabra aleatoria
Palabra_elegida = r.choice(PALABRAS)
print (f"la palabra elegida es {Palabra_elegida}")

for letra in Palabra_elegida:
    generador_de_espacio += "_ "
print(generador_de_espacio)


#se pide al usuario una letrA
letra_usuario = input ("Ingrese una Letra ")
#print(letra_usuario)

# verificamos que la letra se encuentre en la palabra
for validacion in Palabra_elegida:
    if validacion == letra_usuario:
        remplazar_espacio+= letra_usuario
    else:
        remplazar_espacio+= "_"
print(remplazar_espacio)