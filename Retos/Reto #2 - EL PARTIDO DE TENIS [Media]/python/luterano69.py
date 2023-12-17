"""""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 """
class Jugador:  
    marcador    = 0
    ventaja     = False      
    def IncrementarMarcador(self):
       self.marcador+=1 if self.marcador <= 3 else 0

class Partida:
    ganador = 0
    el_juego ={"0":"Love","1":"15","2":"30","3":"40"}
    jugador1 = Jugador()
    jugador2 = Jugador()

    ventaja  = 0
    def ImprimirMarcador(self):
        if self.ganador>0:
            print("El ganador es el P"+str(self.ganador))
        else:
            if self.ventaja==0:
                if self.jugador1.marcador==3 and self.jugador2.marcador==3:
                    print("Deuce")
                else:
                    print(self.el_juego[str(self.jugador1.marcador)], self.el_juego[str(self.jugador2.marcador)] )    
            else:
                print("Ventaja P",self.ventaja)
    def TratarPunto(self,punto_jugador:int):
         
        if self.jugador1.marcador ==3 and self.jugador2.marcador ==3:
            
            #ventaja
            if self.ventaja==0:

                if punto_jugador==1:               
                    self.jugador1.ventaja = True
                    self.jugador2.ventaja = False
                    self.ventaja=1
                else:
                    self.jugador1.ventaja = False
                    self.jugador2.ventaja = True
                    self.ventaja=2
            else:
                if punto_jugador==1:
                    if self.jugador1.ventaja:
                        self.ganador = 1
                    else:
                        self.ventaja =0
                        self.jugador1.ventaja=0
                else:
                    if self.jugador2.ventaja:
                        self.ganador = 2
                    else:
                        self.ventaja =0
                        self.jugador2.ventaja=0
                
        else:
            if punto_jugador ==1:        
                if self.jugador1.marcador  ==3:
                    self.ganador=1
                else:     
                    self.jugador1.marcador+=1
            else:
                if self.jugador2.marcador  ==3:
                    self.ganador=2
                else:
                    self.jugador2.marcador+=1
   
        self.ImprimirMarcador()
################## PARTIDA#####################3
la_partida  = Partida()
secuencia = ("P1","P1","P2","P2","P1","P2","P1","P1")
i=0

while la_partida.ganador == 0:
    #li_punto_jugador= int(input("Punto del juagador P:"))
    ls_jugador = secuencia[i]
    li_punto_jugador = int(ls_jugador[1])

    if li_punto_jugador!=1 and li_punto_jugador!=2:
        print("Introduzca correcto el P1 o P2")
    else:    
        la_partida.TratarPunto(li_punto_jugador)                
    i+=1
