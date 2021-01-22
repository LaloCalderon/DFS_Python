# DFS Depth First Search

#De una red (archivo NetworkXX.txt) y una determinada raiz (nodo tal)
#Con criterios para saber que nodo visita son:

'''
	* opc 1 menor ID 
	* opc 2 mayor ID  
	* opc 3 nodo mas cercano
	* opc 4 nodo mas lejano

'''

#Determinar:

	# 1) La cantidad de hojas que se genera en el arbol 
	# 2) Nodo con mas hijos (en caso de empate elegir el del identificador mayor/menor depende del ejercicio)
	# 3) cuantos nodos tienen mas de un hijo

#algoritmo funcion DFS https://www.youtube.com/watch?v=3VA5brfM68Y&t=596s

import math
import operator
import sys


def Read(archive):
	master = {}
	file = open(archive, "r")
	for line in file:
		line = line.rstrip('\n')
		line = line.split(':')
		#print(line)
		node = line[0]
		#print(node)
		coor = line[1].replace("(","")
		coor = coor.replace(")","")
		#print(coor)
		master[node] = coor
	file.close()
	return(master)

def Neighbours(datos):
	key = datos.keys() #1,2,3,4....
	cdatos = datos
	nuevos = {}
	nuevosdist = {}
	
	for i in key:
		vecinos = []
		vecinosdist = {}
		coor = cdatos[i]  
		coor = coor.split(",")
		x1 = coor[0]
		y1 = coor[1]
		for j in key:
			if (j != i):
				ncoor = cdatos[j]
				ncoor = ncoor.split(",")
				x2 = ncoor[0]
				y2 = ncoor[1]
				dist = math.sqrt((float(x1)-float(x2))**2+(float(y1)-float(y2))**2)
				#print("distancia entre "+i+" y "+j+" es "+str(dist))
				if (dist < 100.0):
					vecinos.append(int(j))
					vecinosdist[j] = dist
		
		vecinos.sort()
		vecinosdist = sorted(vecinosdist.items(),key=operator.itemgetter(1))
		listaorden = []
		for x in vecinosdist:
			listaorden.append(int(x[0]))

		nuevos[int(i)] = vecinos
		nuevosdist[int(i)] = listaorden			

	return (nuevos,nuevosdist)			

def DFS(grafo,root,final,visitados):

	if root not in visitados:
		visitados.append(root) 
		for x in grafo[root]:
			if x not in visitados:
				final[root].append(x)
			DFS(grafo,x,final,visitados)
	
	return final

def Resultados(grafofinal):
	
	conthojas = 0
	contnodosmashijos = 0
	hijos = {}
	mashijos = []

	for i in grafofinal:
		vecinos = grafofinal[i]
		hijos[i] = len(vecinos) #El nodo i tiene len(vecinos) numero de hijos
		if (len(vecinos) == 0):
			conthojas = conthojas + 1
		else:
			if len(vecinos) > 1:
				contnodosmashijos = contnodosmashijos + 1
	maxnumhijos = max(hijos.values())

	for x in hijos: 
		if maxnumhijos == hijos[x]:
			mashijos.append(int(x))

	print("Maximo numero de hijos: "+str(maxnumhijos))
	print("Hojas en el arbol: "+str(conthojas))
	print("Nodo con mas hijos con mayor id: " + str(max(mashijos)))
	print("Nodo con mas hijos con menor id: "+ str(min(mashijos)))
	print("Numero de nodos con mas de un hijo: "+ str(contnodosmashijos))

							



#----------------------MAIN---------------------
	''' base_ord es diccionario {'llave': contenido} {'nodo': lista de sus vecinos } 
													   nodo 1,2,3 y lista de vecinos ordenada de menor a mayor
		basedist es dicci {'llave : contenido} { 'nodo': lista de vecinos}
													nodo 1,2,3 y lista de vecinos ordenados de menor a mayor 
													respecto a la distancia del nodo x
		'''

if __name__ == "__main__":

	sys.setrecursionlimit(2000)
	
	data = Read('Network18.txt') #diccionario (llave es el nodo y el contenido sus coordenadas)
	(base,basedist) = Neighbours(data) 
	base_ini = sorted(base.items())
	base_ord = {}
	for i in base_ini:
		base_ord[i[0]] = i[1]
	
#-------AHORA-SI-YA-HACE-EL-ALGORITMO-----------------

	final = {}
	visitados = []

#----------------------------------------------------ELEMENTOS-A-MODIFICAR---------------
	node_root = 1382
	opc = 4
#----------------------------------------------------------------------------------------

	if opc is 1:
		print("Criterio MENOR ID")
		print("Node_root: " + str(node_root))
		for h in base_ord.keys():
			final[h] = []
		
		PH = DFS(base_ord,node_root,final,visitados)
		Resultados(PH)
		pass


	elif opc is 2:
		print("Criterio MAYOR ID")
		print("Node_root: " + str(node_root))
		base_dro = {}
		for i in base_ord:
			listades = base_ord[i]	
			base_dro[i] = sorted(base_ord[i], reverse=True)
		
		for h in base_dro.keys():
			final[h] = []
		
		PH = DFS(base_dro,node_root,final,visitados)
		Resultados(PH)
		pass	


	elif opc is 3:
		print("Criterio MENOR DISTANCIA")
		print("Node_root: " + str(node_root))
		for h in basedist.keys():
			final[h] = []
		
		PH = DFS(basedist,node_root,final,visitados)
		Resultados(PH)
		pass


	elif opc is 4:
		print("Criterio MAYOR DISTANCIA")
		print("Node_root: " + str(node_root))
		basedistinv = {}
		for i in basedist:
			listades = basedist[i]	
			basedistinv[i] = listades[::-1]
		
		for h in basedistinv.keys():
			final[h] = []

		PH = DFS(basedistinv,node_root,final,visitados)
		Resultados(PH)
		pass


	else:
		print("no pues ya no hay otro")






