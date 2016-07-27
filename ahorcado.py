import funciones
print ("BIENVENIDO AL AHORCADO SUPREMO!!!!")
errores=0
l1=[]
pa=[]
p=funciones.palabras(l1)
print(p)
for letra in p:
	pa.append("_")
while errores <= 7:
	errores=0
	while "_" in pa:
		oculto= " ".join(pa)
		print (oculto)

		res = input("ingrese una letra: ")
		encontrado=False
		for i in range(0, len(p)):

			if p[i] == res:
				pa[i]=res
		if res not in pa:
			errores=errores+1
print(p) 
print ("gracias por jugar")
	
