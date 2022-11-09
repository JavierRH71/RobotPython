from RobotPython import *
Bariloche = Ciudad(Calles=5,Avenidas=5,LongCuadra=60,PlantarFlores=False)
robot = RoboTito(Ciudad=Bariloche, Velocidad='fastest',MostrarTraza = False)
Bariloche.PlantarFlores(CantidadDeFlores=0, Color='', MostrarFloresPlantadas=True,Zona=[[1,1],[5,2]])

robot.Encender()
opc=9
while opc <> 0:
	print "1-Avanzar"
	print "2-Girar izquierda"
	print "3-Girar Derecha"
	print "4-PonerFlor"
	print "5-JuntarFlor"
	print "0- Salir"
	
	opc=int(raw_input("ingrese opcion : "))
	if opc == 1 :
		robot.Avanzar()
	elif opc == 2:
		robot.Girar(270)
	elif opc== 3:
		robot.Girar(90)
	elif opc == 4:
		color = raw_input("de que color? ")
		robot.PonerFlor(color)
	elif opc == 5:
		robot.JuntarFlor()
robot.Apagar()