import funciones
print ("BIENVENIDO AL AHORCADO SUPREMO!!!!")
jugar="si"
while jugar=="si":
	e=0
	l1=[]
	pa=[]
	p=funciones.palabras(l1)
	for letra in p:
		pa.append("_")

	while "_" in pa and e < 7:
		oculto= " ".join(pa)
		print (oculto)

		res = input("ingrese una letra: ")
		encontrado=False
		for i in range(0, len(p)):

			if p[i] == res:
				pa[i]=res
		if res not in pa:
			e=e+1
			k= funciones.mu(e)
			print (k)
		if "_" not in pa:
			print("gano!!!!!!")
	if e ==7:
		print("perdio")
	print( "la palabra era: " +p) 
	jugar=input("desea jugar otra vez: ")
print ("gracias por jugar")
	
