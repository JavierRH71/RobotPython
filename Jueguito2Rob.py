from RobotPython import *

import msvcrt
def KeyPress():
    Key = ''
    if msvcrt.kbhit():
        Key = msvcrt.getch()
    return Key

def ShiftingKeys(AKeys=[], To="Right"):
    Keys=AKeys
    if To == "Right":
        tmp = Keys[0]
        for i in range (len(Keys) -1):
            Keys[i] = Keys[i+1]
        Keys[-1] = tmp
    elif To == "Left":
        tmp = Keys[-1]
        for i in range (len(Keys) -1):
            Keys[len(Keys) -1 -i] = Keys[len(Keys) -2-i]
        Keys[0] = tmp
    elif To == "Back":
        for j in range(2):
            tmp = Keys[0]
            for i in range (len(Keys) -1):
                Keys[i] = Keys[i+1]
            Keys[-1] = tmp
    return Keys
    
#creamos la Ciudad de bariloche
Bariloche = Ciudad(Calles=5, Avenidas=5, FlorSimple= True, LongCuadra= 60)
#Creamos el Robot en la ciudad de BAriloche
Rob1 = RoboTito(Ciudad=Bariloche, Velocidad='fastest')
Rob2 = RoboTito(Ciudad=Bariloche, Velocidad='fastest')

Rob1.Encender()
Rob2.Encender()
KEY_ESC = chr(27)
R1_KEY = ["d", "s","a","w"]
R2_KEY = ["l", "k","j","i"]
eleccion = ""
print R1_KEY
while eleccion != KEY_ESC:
    
    eleccion = KeyPress().lower()
    
    if eleccion == R1_KEY[3] :
        Rob1.GirarIzquierda()
        Rob1.Avanzar()
        R1_KEY = ShiftingKeys(AKeys=R1_KEY, To="Left")
    elif eleccion == R1_KEY[0]:
        Rob1.Avanzar()
    elif eleccion == R1_KEY[2]:
        Rob1.Girar(180)
        Rob1.Avanzar()
        R1_KEY = ShiftingKeys(AKeys=R1_KEY, To="Back")
    elif eleccion == R1_KEY[1]:
        Rob1.GirarDerecha()
        Rob1.Avanzar()
        R1_KEY = ShiftingKeys(AKeys=R1_KEY, To="Right")
    elif eleccion == " " :
        Rob1.JuntarFlor()
    elif eleccion == "p": 
        color = raw_input("legir color red, blue, green, yellow, pink")
        Rob1.PonerFlor(color)
    elif eleccion == R2_KEY[3] :
        Rob2.GirarIzquierda()
        Rob2.Avanzar()
        R2_KEY = ShiftingKeys(AKeys=R2_KEY, To="Left")
    elif eleccion == R2_KEY[0] :
        Rob2.Avanzar()
    elif eleccion == R2_KEY[2] :
        Rob2.Girar(180)
        Rob2.Avanzar()
        R2_KEY = ShiftingKeys(AKeys=R2_KEY, To="Back")
    elif eleccion == R2_KEY[1] :
        Rob2.GirarDerecha()
        Rob2.Avanzar()
        R2_KEY = ShiftingKeys(AKeys=R2_KEY, To="Right")    
    elif eleccion == "u" :
        Rob2.JuntarFlor()

Rob1.Apagar()
Rob2.Apagar()
    

