""""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 """
import random
import string

def GenerarClaves(longitud:int,contiene_mayusculas:bool,contiene_numeros:bool,contiene_simbolos:bool):

    caracteres = string.ascii_lowercase
    if contiene_mayusculas:
        caracteres+=string.ascii_uppercase
    if contiene_numeros:
        caracteres+=string.digits
    if contiene_simbolos:
        caracteres+=string.punctuation    
    i = 1
    password = ''
    for i in range(longitud):
       password +=random.choice(caracteres)
       i+=1
    return password

print("GENERAR UNA CLAVE")
longitud = int(input("¿LONGITUD DE LA CLAVE?"))
if longitud<8 or longitud>16:
    print("La longitud de la clave debe estar comprendida entre 8 y 16")
    exit()
quieres_mayusculas = input(f"¿QUIERES QUE CONTENGA MAYÚSCULAS (S/N)?").capitalize()
quieres_numeros = input("¿QUIERES QUE CONTENGA NUMEROS? (S/N) ").capitalize()
quieres_simbolos= input("¿QUIERES QUE CONTENGA SÍMBOLOS? (S/N)").capitalize()

print("Password:\n" +GenerarClaves(12,quieres_mayusculas=="S",quieres_numeros=="S",quieres_simbolos=="S") )
