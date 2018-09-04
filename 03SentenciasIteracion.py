#SENTENCIAS DE ITERACION

#WHILE-------------------------
# i=1

# while i<10:
# 	print(i)
# 	i+=1


#FOR--------------------------

# j=1
# for j in range(10):
# 	print(j)

# for j,k in enumerate(range(10)):
# 	print(j)
# 	print("k",k)


# for item in "[1,2,3,4,5,6,7]":
# 	print(item*2)



# ###for---------------------------------------------------------------------
# for l, line in enumerate(open("/home/diana/Escritorio/Practicas/hol.txt")):
# 	for p in line.split():
# 		for f in p:
# 			if f == "r":
# 				pass
# 			else: 
# 				print(f)

# for i in rang(10):
# 	print(i)


##IMPRIMI EL VALOR DE UNA LISTA ----------------------------------------
# lista = []
# for i in range(10):
# 	lista.append(i)
# print(lista)

#print([i for i in range(10) if i %2==0])



##WHILE----------------------------------------------------------------
import random  --se  necesita esta libreria para manejar numeros random.

# while True:
# 	print(random.randint(1,100))

r=1
c=0

while r != 99 or c<5:
	r = random.randint(1,100)
	c += 1

	print (r)





	