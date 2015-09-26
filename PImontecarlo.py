#coding=utf-8
import random as rd
#numero de pontos
npoints = 10**7
#contador
count = 0
def e_value():
	global count, num,npoints
	#raio do circulo inscrito no quadrado
	raio = 0.5
	#ponto do centro
	O = x0,y0 = 0.5,0.5
	for c in range(npoints):
		#ponto p dentro do quadrado x pertence à [0,1], y pertence à [0,1]
		P = x,y = rd.random(),rd.random()
		#formula da Distância entre dois pontos O(x0,y0) e P(x,y)
		d = ((x-x0)**2+(y-y0)**2)**0.5
		#Se o ponto cair no circulo
		if d < raio:
			#contabilize!
			count += 1
e_value()
#calculo de PI via monte carlo (estatística)
PI = 4.0*count/npoints
print(PI)
