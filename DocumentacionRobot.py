#!/usr/local/bin/python
# -*- coding: latin-1 -*-
'''
Created on 24/05/2017

@author: Javier Haramina
'''

print """
 los simbolos #  o las triples comillas 
 son para poner comentarios en el programa, son como anotaciones 
 que la compu ignora por completo NO SON ORDENES DE PROGRAMA
 
 LA CIUDAD.
 
 Antes de comenzar cualquier programa se debe Crear la ciudad usando la siguiente sintaxis.
 
 @Sintaxis: NombreDeLaCiudad = Ciudad(Calles, Avenidas, LongCuadra, PlantarFlores , CantidadFlores , FlorSimple )
    @parametros:
        Calles : es la cantidad de Calles que le queremos que tenga la ciudad
        Avenidas :  es la cantidad de Avenidas que queremos que tenga la ciudad
        LongCuadra :  es la longituda de la cuadra que queremos que tenga la ciudad
        PlantarFlores : es un parametro del tipo boolean, si es True, planta Flores en la Ciudad al momento de Crearla
                        si es False no lo hace
        CantidadFlores : es la cantidad de Flores que Queremos Que Plante al inicio, si el parametro
                         PlantarFlores es True. Si es 0 pone una cantidad aleatoria de flores 
        FlorSimple : es un parametro del tipo boolean, si es True, la ciudad Mostrará las flores 
                     como un circulo, si es False, mostrará flores con petalos
                     
     @Ejemplo: Bariloche = Ciudad(Calles=10, Avenidas=10, LongCuadra=30, PlantarFlores = True, CantidadFlores = 0, FlorSimple=False)
 
 @Propiedades de la Ciudad que pueden ser utilizadas durante el programa
     Las propiedades de un objeto, pueden ser utilizadas igual que se usan las variables 
     comunes, con la unica diferencia que hay que anteponer el nombre del objeto seguido de 
     un punto y luego el nombre de la propiedad que quiera utilizarse.
     Ejemplo para utlilizar la propiedad Calles de la Ciudad de Bariloche deberemos escribir en 
     el programa lo siguiente:
     
    @Ejemplo Barilohce.Calles 
        con este ejemplo podríamos saber que cantidad de Calles Tiene la Ciudad 
 
    Calles         un valor del tipo entero que indica la cantidad de Calles que tiene la Ciudad
    Avenidas       un valor del tipo entero que indica la Cantidad de Avenidas que tiene la Ciudad
    LargoCuadra    un valor del tipo entero que indica el largo de la cuadra en pixeles
    TamanioFlor    un valor del tipo entero que indica el tamaño de la Flor en Pixeles,
                   su valor es el de la mitad del largo de la cuadra
    FlorSimple     un valor del tipo Boolean (True / False) que indica si las flores se dibujan
                   como un circulo cuando su valor es True o como una Flor si su valor es False
    FloresPosibles un vector con los posibles colores de Flores que se pueden manejar en la ciudad
                   ['','red','yellow','blue','green', 'pink']
 
 @Metodos:  La ciudad puede realizar algunas tareas o metodos que son las siguientes
     
     PlantarFlores(CantidadDeFlores=0, Color = '', MostrarFloresPlantadas = False, Zona=[[-1,-1],[-1,-1]] ):
     @parametros : 
         CantidadDeFlores : es la cantidad de flores a plantar si es 0 pone una cantidad aleatoria de flores
         Color : es el color de las flores a plantar si no se pone o se pone '' elige colores aleatoriamente
         MostrarFloresPlantadas : si se pone False, no muestra las flores, True si las muestra
         Zona :  es una matriz bidimensional de 2 x 2 indicando la zona rectangular donde plantar.
                 El primer par de la matriz indica la esquina sup izq, y el siguiente par, la esquina inf derecha
                 es de la forma[[calle sup ,avenida izq ],[calle inf ,avenida der]]

                 
 Luego, hay que crear al Robot en dicha ciudad y darle un nombre de la siguiente manera:
 
 @Sintaxis: NombreDelRobot = RoboTito(Ciudad, Velocidad, MostrarTraza )
        @parametros : 
            Ciudad debe ser un objeto Ciudad, donde se moverá el robot
            
            Velocidad del Robot es opcional, y se puede no poner.
            Pero se pueden usar las siguientes Velocidades 'slowest', 'slow', 'normal'
            'fast', 'fastest' 
            El parametro MostrarTraza si es True, hace que el robot vaya dejando una traza
            de su recorrido
 
 @Ejemplo1: robot = RoboTito(Ciudad=Bariloche, Velocidad='Normal')
 
 @Ejemplo2: robot = RoboTito(Ciudad=Bariloche)
 
 
 @Metodos
 Metodos u Ordenes a las que responde el Robot:
 cualquiera de estas ordenes se 
 accede por el nombre del robot seguido de un punto seguido del nombre de la orden
 
 @Sintaxis : nombrerobot.orden
 
 @Ejemplo : robot.Avanzar()
 
 
 Encender()  enciende y posiciona al robot en la esquina 1,1 orientado al ESTE 
             listo para empezar
             
 Apagar()    antes de Finalizar el Programa debemos llamar a este método, para que 
             el robot espere 4 segundos y luego se apague, esto es útil para poder ver los
             resultados de nuestro programa
             
 Avanzar()    Avanza a la siguiente Esquina en la misma orientacion que esta

 AvanzarX(Cuadras) Avanza el nro de Cuadrasindicadas, en la misma orientacion que esta 
 
 Girar(angulo en grados multiplos de 90) Gira la orientacion del robot a la derecha, 
             los grados indicados por el angulo
 
 GirarDerecha(angulo en grados multiplos de 90) Gira la orientacion del robot a la derecha, 
             los grados indicados por el angulo
             
 GirarIzquierda(angulo en grados multiplos de 90) Gira la orientacion del robot a la izquierda, 
             los grados indicados por el angulo
             
 HayFlor()  Permite al robot preguntar si hay o no una flor en la esquina donde se encuentra
             devolviendo True si hay una Flor o False si no hay
             
 JuntarFlor() Permite al robot juntar la flor que hay en esa esquina
 
 PonerFlor(ColorFlor) Permite al robot poner una Flor del color indicado por ColorFlor 
                      en la esquina donde se encuentra. 
                      Los colores posibles son:('red', 'blue', 'yellow', 'green', 'pink')
  
 Posicionar(Calle, Avenida) Permite al robot posicionarse en la esquina determinada por 
                             la interseccion entre la Calle y la Avenida indicadas
                             
 
 ColorFlor()    Permite al robot preguntar de que color es la Flor que hay en la esquina.
                 El Robot responderá con alguno de los colores Posibles 
                 Los colores posibles son:('red', 'blue', 'yellow', 'green', 'pink')
 
 Informar(Mensaje, mensaje, mensaje ,.....) Permite al robot informar el o los mensaje
                de texto por pantalla. Los Mensajes Deben ir separados por comas
 
"""
