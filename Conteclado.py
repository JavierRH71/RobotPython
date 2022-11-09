def TeclaPulsada():
	'''Lee el buffer de Teclado, y devuelve el codigo de tecla pulsada si
	 se presiono una tecla
	 ojo, esto no funciona en el IDLE porque lee directamente del teclado
	 y no del stdin
	'''
	
	Tecla = ''
	if msvcrt.kbhit():
		Tecla = msvcrt.getch()
	return Tecla