
#!/usr/local/bin/python
# -*- coding: latin-1 -*-
'''
Created on 24/05/2017

@author: Haramina Javier
'''
from  RobotPython import *

Bariloche = Ciudad(Calles=5,Avenidas=5, LongCuadra=60,FlorSimple=False)
robot = RoboTito(Ciudad=Bariloche, Velocidad='slow')
robot.Encender()
Esquinas=[(1,1),(1,2),(1,3),(1,4),(1,5),
          (2,5),(3,5),(4,5),(5,5),(5,4),
          (5,3),(5,2),(5,1),(4,1),(3,1),
          (2,1),(2,2),(2,3),(2,4),(3,4),
          (4,4),(4,3),(4,2),(3,2),(3,3)]
for a, c in Esquinas:
    robot.Posicionar(c, a)
    if robot.HayFlor() and robot.ColorFlor() in ['red', 'blue', 'green']: 
        robot.JuntarFlor()
        robot.PonerFlor(ColorFlor='yellow')
robot.Apagar()