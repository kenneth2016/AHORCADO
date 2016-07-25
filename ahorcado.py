import funciones
print ("BIENVENIDO AL AHORCADO SUPREMO!!!!")
errores=0
l1=[]
p=funciones.palabras(l1)
while errores<=7:
	print("_ "*len(p))
	input("ingrese una letra: ")

print (list(p))