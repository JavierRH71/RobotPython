#!/usr/local/bin/python
# -*- coding: latin-1 -*-
'''
Created on 21/06/2011

@author: Haramina Javier
'''

import pygame
from time import sleep 

from RobotPython import *
#Defino las Constantes correspondientes al Joystick
EJE_H_PAL_IZQ = 0
EJE_V_PAL_IZQ = 1
EJE_H_PAL_DER = 2
EJE_V_PAL_DER = 3
BOTON_EQUIS = 0
BOTON_CIRCULO = 1
BOTON_CUADRADO = 2
BOTON_TRIANGULO = 3
BOTON_INDICE_IZQ = 4
BOTON_INDICE_DER =  5
BOTON_ANULAR_IZQ = 6
BOTON_ANULAR_DER = 7
BOTON_SELECT = 8
BOTON_START = 9
ESTADO_ON = 1

blnPresioneBotonX = False

Val_Eje_H_Pal_Izq = 0.0
Val_Eje_V_Pal_Izq = 0.0


Bariloche = Ciudad(Calles=10,Avenidas=10,LongCuadra=50,PlantarFlores=False)
robot = RoboTito(Ciudad=Bariloche, Velocidad='normal',MostrarTraza = False)
Bariloche.PlantarFlores(CantidadDeFlores=0, Color='', MostrarFloresPlantadas=True,Zona=[[1,1],[5,2]])

robot.Encender()
#inicio la libreria Pygame
pygame.init()
#Creo objeto Joystick
MyJoystick = pygame.joystick.Joystick(0)
#inicio el Joystick
MyJoystick.init()

while not blnPresioneBotonX :
    
    # Para leer los eventos del joystick
    for event in pygame.event.get():
        pass

    # Leo los valores actuales de la posicion del eje 0 (horizontal palanca izq)
    # Leo los valores actuales de la posicion del eje 1 (vert palanca izq)
    Val_Eje_H_Pal_Izq = MyJoystick.get_axis(EJE_H_PAL_IZQ)
    Val_Eje_V_Pal_Izq = MyJoystick.get_axis(EJE_V_PAL_IZQ)
    
    Val_Eje_H_Pal_Izq = int(float(u"%6.3f" % Val_Eje_H_Pal_Izq))
    Val_Eje_V_Pal_Izq = int(float(u"%6.3f" % Val_Eje_V_Pal_Izq))

    # salgo del loop finalizo el conrol del joystik si presiono boton x
    if  MyJoystick.get_button(BOTON_EQUIS) == ESTADO_ON :
        blnPresioneBotonX = True
    if  MyJoystick.get_button(BOTON_CUADRADO) == ESTADO_ON :
        robot.JuntarFlor()
    if  MyJoystick.get_button(BOTON_CIRCULO) == ESTADO_ON :
        robot.PonerFlor(ColorFlor='red')
    if  MyJoystick.get_button(BOTON_TRIANGULO) == ESTADO_ON :
        robot.PonerFlor(ColorFlor='green')
    if  MyJoystick.get_button(BOTON_INDICE_DER) == ESTADO_ON :
        robot.PonerFlor(ColorFlor='blue')
    if  MyJoystick.get_button(BOTON_INDICE_IZQ) == ESTADO_ON :
        robot.PonerFlor(ColorFlor='yellow')
    if  MyJoystick.get_button(BOTON_ANULAR_DER) == ESTADO_ON :
        robot.PonerFlor(ColorFlor='pink')        
    
    #Proceso los eventos del Joystick
    if Val_Eje_H_Pal_Izq < 0:
        robot.GirarIzquierda()
    if Val_Eje_H_Pal_Izq > 0:
        robot.GirarDerecha()
    if Val_Eje_V_Pal_Izq < 0:
        robot.Avanzar() 
    if Val_Eje_V_Pal_Izq > 0:
        robot.GirarDerecha(180)
        robot.Avanzar()
        
        
    sleep(0.25)   
    


        
