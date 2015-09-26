#coding=utf-8
import multiprocessing as mp
import random as rd

# Define um output queue
output = mp.Queue()

#numero de nucleos de processamento/numero de vezes que o processo será dividido
num = 4
#numero de pontos
npoints = 10**7
#contador
count = 0

def e_value(output):
	global count, num,npoints
	#'divisão internacional do trabalho' para cada WORKER(SLAVE) ou processo
	part = npoints / num
	#raio do circulo inscrito no quadrado
	raio = 0.5
	#ponto do centro
	O = x0,y0 = 0.5,0.5
	for c in range(part):
		#ponto p dentro do quadrado x pertence à [0,1], y pertence à [0,1]
		P = x,y = rd.random(),rd.random()
		#formula da Distância entre dois pontos O(x0,y0) e P(x,y)
		d = ((x-x0)**2+(y-y0)**2)**0.5
		#Se o ponto cair no circulo
		if d < raio:
			#contabilize!
			count += 1
	#enviar count para o MASTER ou para o QUEUE
	output.put(count)
# Setup a list of processes that we want to run
processos = [mp.Process(target=e_value, args=(output,)) for x in range(num)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]
#juntar os resultados dos processos
c = 0.0
for n in results:
	c += n
#calculo de PI via monte carlo (estatística)
PI = 4.0*c/npoints
print(PI)
