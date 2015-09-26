#coding: utf-8
a = 1
b = 1000

lista = range(a,b)
#primeiro primo legal
i = 2
while(i <= b/2):
	#para cada elemento da lista de multiplos de um numero 'i'
	for n in range(i,b,i):
		try:
			#tente removê-los da lista se o elemento não é igual ao primeiro numero
			if n != i: lista.remove(n) # n precisa existir e como alguns já foram removidos anteriormente é só ignorar...
		except:
			pass
	#o proximo numero é um primo então... atualize o contador
	i += 1
print lista
