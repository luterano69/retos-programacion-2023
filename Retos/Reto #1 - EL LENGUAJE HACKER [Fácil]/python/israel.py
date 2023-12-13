
""""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """
texto ="asd"

def f_sustituir(a:str):
    b = ""
    try:
        #a= a.capitalize()
        if not a.isalpha:
            print("la entrada " + str(a) +" no es alfanumérica")
            return "-1"
        #if a<="A" and a>= "Z":
        #    print("la entrada " + str(a) +" no es alfanumérica")
        #    return "-1" 
        if  a== "A":
            b="4" 
        elif a=="B":
            b="13"
        elif a=="C":
            b="["
        elif a=="D":
            b=")" 
        elif a=="E":         
            b="3"
        elif a=="F":
            b="|="
        elif a=="G":
            b="&"
        elif a=="H":
            b="#"
        elif a=="I":
            b="1"
        elif a=="J":
            b=",_|"
        elif a=="K":
            b=">|"
        elif a=="L":
             b="1"
        elif a=="M":
             b="/\\/\\"
        elif a=="N":
             b="^/"        
        elif a=="Ñ":
             b="/\\asd"
        elif a=="O":
             b="0"
        elif a=="P":
             b="|*"
        elif a=="Q":
             b="(_,)"
        elif a=="R":
             b="I2"
        elif a=="S":
             b="5"
        elif a=="T":
             b="7"
        elif a=="U":
             b="(_)"
        elif a=="V":
             b="\/"
        elif a=="W":
             b="\/\/"
        elif a=="X":
             b="><"
        elif a=="Y":
             b="j"
        elif a=="Z":
             b="2"
        else:
            b=" "

    except Exception as error:
        print(error)

    finally:
        return b

texto = input("Introduce el texto: ").upper()
i =0
texto_traducido = ""
for a in texto:
    pass
    texto_traducido= texto_traducido +   f_sustituir(a)
    i+=1
print(texto_traducido)
