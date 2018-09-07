#INTEGER
C=34
B=76
Print(a+b)
Print(a/b)
Print(a//b) si queremos que el número sea siempre entero

#FLOAT
F=23.98
P=45.32
Print(f*p)

#BOOLEAN
T=True
F=False

#LISTAS (ARRAYS)
Lista=[54,12,67,23]
Print(lista)
#para agregar elementos a la lista
Lista.append(65)
#para insertar
Lista.isert(0,7) 
#en el anterior comando el 0 es la posición donde deseas agregar el elemento, el segundo es el elemento
##para imprimir solo un elemento
Print(lista[0])
Print(lista[2])

##para borrar
 del(l[1]) 
#dices la posición

#metodos de ordenamiento
Lista.sort() # ordenara pero alterara los valores de l
print(sorted(lista)) 



#TUPLAS
# t=(1,2,"abc",True,[4,5])
# print("print(t)")
# print(t)
# print("print(t[2])")
# print(t[2])
# print("for")
# for item in t:
# 	print(item)
	#despliega uno por uno de los items en la tupla saltando renglon




#DISCCIONARIOS (DICT)
#compuesto por un valor clave y uno nominal //1 id y //2 variable o valor
#lista y diccionario son mutables
#d={1:2, "abc":34, 2:"item", "d":"ch", "li":[1,2,3], "dic":{11:23}}	
#print("imprimir diccionario")
#print(d)

#print(d["dic"])

#print(d["li"][1])

#para pedir claves
#print(d.keys()) para sacar las claves
#print(d.values())  para sacar los valores
#print(d.items())  para sacar ambos

#borrar 
#del.d["abc"]


#SETS /------------------------ CONJUNTOS---Estos no llevna claves, solo valores

# s={1,2,3,4}

# print(s)
# print(type(s))

# for item in s:
# 	print(item)
