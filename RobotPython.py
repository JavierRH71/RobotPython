#!/usr/local/bin/python
# -*- coding: latin-1 -*-
'''
Created on 07/05/2017

@author: Javier Haramina

@Version: 1.0

'''

import turtle
import random 
from time import sleep

__Version = '1.0'
def Version():
    return __Version

class Ciudad:
    def __init__(self, Calles = 10, Avenidas = 10, LongCuadra = 30, PlantarFlores = True, CantidadFlores = 0, FlorSimple=False):
        self.Calles = Calles
        self.Avenidas = Avenidas
        self.LargoCuadra = LongCuadra
        self.Robot = turtle.Turtle()
        self.origen = {"x": -1 * ((self.Avenidas * self.LargoCuadra)//2), "y":((self.Calles * self.LargoCuadra)//2)}
        self.TamanioFlor = int(LongCuadra * 1 / 2)
        self.FlorSimple = FlorSimple
        self.FloresPosibles = ['','red','yellow','blue','green', 'pink']
        self.FloresPlantadas=[]
        #cargo la matriz con esquinas vacias
        #self.FloresPlantadas = [z  for z in [[''] * self.Calles] * self.Avenidas]
        
        for i in range(self.Calles):
            self.FloresPlantadas.append([''] * self.Avenidas)
        
        self.Robot.speed('fastest')
        self.Robot.hideturtle()
        self.DibujarCiudad()
        
        if PlantarFlores:
            self.PlantarFlores(CantidadFlores, '', PlantarFlores)

    def DibujarFlor(self, ColorFlor):
        
        x, y = self.Robot.position()
        if self.FlorSimple:
            self.Robot.dot(self.TamanioFlor,ColorFlor)
        else:
            dd = [(x - (self.TamanioFlor / 4.7), y + (self.TamanioFlor / 4.7)),
                  (x + (self.TamanioFlor / 4.7), y + (self.TamanioFlor / 4.7)),
                  (x + (self.TamanioFlor / 4.7), y - (self.TamanioFlor / 4.7)),
                  (x - (self.TamanioFlor / 4.7), y - (self.TamanioFlor / 4.7))]
            for dx, dy in dd:
                self.Robot.goto(dx,dy)
                self.Robot.dot(self.TamanioFlor / 2.5, ColorFlor)
            self.Robot.goto(x,y)
            self.Robot.dot(self.TamanioFlor / 2.5,'orange')
        
                    
    def DibujarCiudad(self):
        self.Robot.reset()
        self.Robot.speed('fastest')
        self.Robot.hideturtle()

        self.Robot.pen(False)
        self.Robot.penup()
        self.Robot.clear()
        self.Robot.goto(self.origen["x"],self.origen["y"])
        for calle in range (0,self.Calles ):
            self.Robot.goto(self.origen["x"], self.origen["y"] + calle * (-self.LargoCuadra ))
            self.Robot.pendown()
            self.Robot.forward(self.LargoCuadra  * (self.Avenidas -1))
            self.Robot.penup()
        
        self.Robot.goto(self.origen["x"],self.origen["y"])
        self.Robot.right(90)
        for avenida in range (0,self.Avenidas ):
            self.Robot.goto(self.origen["x"] + avenida * self.LargoCuadra ,self.origen["y"])
            self.Robot.pendown()
            self.Robot.forward(self.LargoCuadra * (self.Calles -1) )
            self.Robot.penup()
            
               
    def PlantarFlores(self, CantidadDeFlores=0, Color = '', MostrarFloresPlantadas = False, Zona=[[-1,-1],[-1,-1]] ):
        if Color in self.FloresPosibles :
            
            # limpio la ciudad
            #self.FloresPlantadas = [z  for z in [[''] * self.Calles] * self.Avenidas]
            self.FloresPlantadas=[]
            for i in range(self.Calles):
                self.FloresPlantadas.append([''] * self.Avenidas)
                
            if Zona[0][0] >=1:
                if not( Zona[0][0] in range(1,self.Calles + 1) ):
                    Zona[0][0] = 1
                if not( Zona[0][1] in range(1,self.Avenidas + 1) ):
                    Zona[0][1] = 1
                if not( Zona[1][0] in range(1,self.Calles + 1) ):
                    Zona[1][0] = self.Calles
                if not( Zona[1][1] in range(1,self.Avenidas + 1) ):
                    Zona[1][1] = self.Avenidas
                if Zona[0][0] > Zona[1][0] :
                    tmp=Zona[0][0]
                    Zona[0][0] = Zona[1][0]
                    Zona[1][0] = tmp
                if Zona[0][1] > Zona[1][1] :
                    tmp=Zona[0][1]
                    Zona[0][1] = Zona[1][1]
                    Zona[1][1] = tmp
                esquinas=[]
                for c in range(Zona[0][0]-1,Zona[1][0]):
                    for a in range(Zona[0][1]-1,Zona[1][1]):
                        esquinas.append(c * self.Avenidas + a)  
                if CantidadDeFlores <= 0 or (CantidadDeFlores > (Zona[1][0] - Zona[0][0] + 1) * (Zona[1][1] - Zona[0][1] + 1) ):
                    CantidadDeFlores = random.choice(range(1,(Zona[1][0] - Zona[0][0] + 1) * (Zona[1][1] - Zona[0][1] + 1 ) + 1)) 
            else:              
                esquinas=range(self.Calles * self.Avenidas)
                CantidadDeFlores = random.choice(range(1,(self.Calles * self.Avenidas) + 1)) if (CantidadDeFlores <= 0) or (CantidadDeFlores > self.Calles * self.Avenidas) else CantidadDeFlores
              
            EsquinasParaPlantar = random.sample(esquinas,CantidadDeFlores)
             
            for esquina in EsquinasParaPlantar:
                calle =  esquina // self.Avenidas
                avenida = (esquina % self.Avenidas) 
                 
                if len(Color) > 0:
                    self.FloresPlantadas[calle][avenida] = Color
                else:
                    self.FloresPlantadas[calle][avenida] = random.choice(self.FloresPosibles[1:])
  
                if MostrarFloresPlantadas :
                    self.Robot.goto(self.origen["x"] + ((avenida) * self.LargoCuadra),
                                    self.origen["y"] + ((calle) * -self.LargoCuadra))
                    self.DibujarFlor(ColorFlor = self.FloresPlantadas[calle][avenida])
  
                    
class RoboTito(turtle.Turtle):
    def __init__(self,Ciudad = None,Velocidad = 'normal', MostrarTraza= False):
        turtle.Turtle.__init__(self)
        self.City = Ciudad
        self.EsquinaActual = {"calle": 1,"avenida": 1}
        self.Direcciones = ["DERECHA","ARRIBA", "IZQUIERDA", "ABAJO"]
        self.DireccionActual = self.Direcciones[0] 
        self.MostrarTraza = MostrarTraza
        self.penup()
        self.pencolor('blue')
        self.speed(Velocidad)
        #
        
    def DibujarFlor(self, ColorFlor=''):
        if len(ColorFlor) > 0 and (ColorFlor in self.City.FloresPosibles):
            self.penup()
            x, y = self.position()
            
            if self.City.FlorSimple:
                self.dot(self.City.TamanioFlor,ColorFlor)
            else:
                dd = [(x - (self.City.TamanioFlor / 4.7), y + (self.City.TamanioFlor / 4.7)),
                      (x + (self.City.TamanioFlor / 4.7), y + (self.City.TamanioFlor / 4.7)),
                      (x + (self.City.TamanioFlor / 4.7), y - (self.City.TamanioFlor / 4.7)),
                      (x - (self.City.TamanioFlor / 4.7), y - (self.City.TamanioFlor / 4.7))]
                for dx, dy in dd:
                    self.goto(dx,dy)
                    self.dot(self.City.TamanioFlor / 2.5, ColorFlor)
                self.goto(x,y)
                self.dot(self.City.TamanioFlor / 2.5,'orange')
            
            if self.MostrarTraza: self.pendown()    
        
    def Encender(self):
        self.Posicionar(1,1)
   
    def Apagar(self):
        sleep(4)
        exit()
    
    def AvanzarX(self, Cuadras=1):
        if Cuadras > 0:
            for c in range(1,Cuadras + 1):
                self.Avanzar()
        
    def Avanzar(self):
        self.forward(self.City.LargoCuadra)
        if self.DireccionActual == "DERECHA":
            self.EsquinaActual["avenida"] += 1
        if self.DireccionActual == "ARRIBA":
            self.EsquinaActual["calle"] -= 1
        if self.DireccionActual == "IZQUIERDA":
            self.EsquinaActual["avenida"] -= 1
        if self.DireccionActual == "ABAJO":
            self.EsquinaActual["calle"] +=1
        
        if (self.EsquinaActual["calle"] not in range(1,self.City.Calles +1)) or (self.EsquinaActual["avenida"] not in range(1,self.City.Avenidas +1)):
            self.write('Ahhhhhhh Me cai e la ciudad')
            print "Te caiste de la Ciudad, no funciono el programa "
            self.Apagar()
            
    def GirarDerecha(self,angulo = 90):
        if angulo % 90 == 0:
            self.DireccionActual = self.Direcciones[int((self.heading() - angulo) / 90 % 4) ]
            self.right(angulo)

    def GirarIzquierda(self, angulo = 90):
        if angulo % 90 == 0:        
            self.DireccionActual = self.Direcciones[int((self.heading() + angulo) / 90 % 4) ]
            self.left(angulo)

    def Girar(self, angulo = 90):
        if angulo % 90 == 0:
            self.DireccionActual = self.Direcciones[int((self.heading() - angulo) / 90 % 4) ]
            self.right(angulo)
   
    def HayFlor(self):
        retval = False
        if len(self.City.FloresPlantadas[self.EsquinaActual["calle"] -1 ][self.EsquinaActual["avenida"] -1]) > 0:
            retval = True
        return retval
    
    def JuntarFlor(self):
        if self.HayFlor():
            self.dot(self.City.TamanioFlor,'white')
            self.City.FloresPlantadas[self.EsquinaActual["calle"] -1][self.EsquinaActual["avenida"] -1] = ''
    
    def PonerFlor(self, ColorFlor =''):
        if len(ColorFlor) > 0 and (ColorFlor in self.City.FloresPosibles):
            self.DibujarFlor(ColorFlor)
            self.City.FloresPlantadas[self.EsquinaActual["calle"] -1][self.EsquinaActual["avenida"] -1] = ColorFlor
           
            
    def ColorFlor(self):
        color = ''
        color = self.City.FloresPlantadas[self.EsquinaActual["calle"] -1 ][self.EsquinaActual["avenida"] -1]
        return color 
    
    def Posicionar(self,Calle, Avenida):
        if not self.MostrarTraza:
            self.penup()
        self.goto(self.City.origen["x"] + ((Avenida - 1) * self.City.LargoCuadra),
                  self.City.origen["y"] + ((Calle - 1) * -self.City.LargoCuadra))
        if self.MostrarTraza: 
            self.pendown()
        self.EsquinaActual["calle"] = Calle
        self.EsquinaActual["avenida"] = Avenida
    
    def Informar(self, *Msg):
        CurrX, CurrY = self.position()
        self.penup()
        x, y = (self.City.origen["x"] + self.City.Avenidas * self.City.LargoCuadra,
                self.City.origen["y"] + self.City.Calles * -self.City.LargoCuadra)
        
        for m in Msg:
            self.goto (x, y)
            self.write(m)
            y -= 10
            
        self.goto (CurrX,CurrY)
        if self.MostrarTraza: 
            self.pendown()
        print Msg

      
