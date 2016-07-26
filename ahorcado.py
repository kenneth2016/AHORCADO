import funciones
print ("BIENVENIDO AL AHORCADO SUPREMO!!!!")
errores=0
l1=[]
p=funciones.palabras(l1)
print(p)
print("_ "*len(p))
pa= list(p)
res = input("ingrese una letra: ")

if res in pa:
	print("si")
else:	
	print("_ _ _ _ _")
	print("|")
	print("|")
	print("|")
	print("|")
	print("|")




