#!/usr/local/bin/python
# -*- coding: latin-1 -*-

'''
Created on 14/05/2017

@author: Javier Haramina

Este programa junta solo Flores Rojas

'''


from  RobotPython import Ciudad, RoboTito, Version

print "Modulo RobotPython Version: ",  Version()
#creamos la Ciudad de bariloche
Bariloche = Ciudad(Calles=5, Avenidas=5, FlorSimple= True, LongCuadra= 60 )

#Creamos el Robot en la ciudad de BAriloche
robot = RoboTito(Ciudad=Bariloche, Velocidad='slowest')

robot.Encender()
# inicializamos las variables
FlorRoja = 0
#comienza la repeticion para las calles
for calle in range (1,Bariloche.Calles + 1):
    #comienza la repeticion para las avenidas
    for avenida in range(1,Bariloche.Avenidas + 1):
        #Posicionamos al robot en la esquina formada por calle, avenida
        robot.Posicionar(calle, avenida)
        if not robot.HayFlor():
            robot.PonerFlor('green')       
        
                

robot.Apagar()
