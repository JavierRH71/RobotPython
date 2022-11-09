#!/usr/local/bin/python
# -*- coding: latin-1 -*-

'''
Created on 07/05/2017
Last Modified : 08/11/2022
@author: Javier Haramina
'''
# Importamos Todas las librerias necesarias para usar el Robot
from  RobotPython import *

#creamos la Ciudad en una Variable Llamada Bariloche que 
#va atener 5 Calles y 5 avenidas y una longitud de 60 cada cuadra
Bariloche = Ciudad(Calles=5,Avenidas=5,LongCuadra=60)

#Creamos el robot en la ciudad de Bariloche que se movera 
# a una velocidad normal puede ser fast, slow, fastest o slowest 
Wally = RoboTito(Ciudad=Bariloche, Velocidad='slow')

#Definimos Variables s las necesitamos
F = 0

# los def son subprocesos o sub rutinas
# Definimos el subproceso llamado RevisarEsquina
def RevisarEsquina():
    # global se usa para indicar que la variable F esta 
    # definida fuera del subproceso
    global F
    if Wally.HayFlor():
        Wally.JuntarFlor()
        F = F + 1

# Definimos el subproceso llamado RecorreCalle
def RecorreCalle():
    for avenida in range (1,Wally.City.Avenidas):
        print Wally.EsquinaActual,Wally.HayFlor()
        RevisarEsquina()
        Wally.Avanzar()

    RevisarEsquina()    
    
# Definimos el subproceso llamado IdayVuelta        
def IdayVuelta():
    RecorreCalle()
    Wally.Girar(90)
    Wally.Avanzar()
    Wally.Girar(90)
    
    RecorreCalle()
    Wally.Girar(270)
    Wally.Avanzar()
    Wally.Girar(270)


#aqui comienza realmente el programa Principal
Wally.Encender()
IdayVuelta()
IdayVuelta()
RecorreCalle()

#informamos algun mensaje
Wally.Informar( "Junte", F , "Flores")

# apagamos el Robot
Wally.Apagar()
# aqui termina el programa