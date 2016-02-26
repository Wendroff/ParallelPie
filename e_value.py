#coding=utf-8
#retorna valor do numero de Euler usando McLaurin Series
# P(x) = f(0) + f'(0)*x f''(0)*x^2/2!+...
# P(x) = f(0) = f'(0) = f''(0) = e^0 = 1
from math import factorial as fac
import decimal
decimal.getcontext().prec = 1072 #precisão 1072
print decimal.getcontext()
#iterador
c = 0
#valor de x na função
x = 1
#variavel para retornar o valor de e
e_value = 0
try:
	#do forever
	while True:
		e_value += decimal.Decimal(x**float(c)/fac(c))
		c += 1
#se a memória estourar
except OverflowError:
	print e_value, 'encontrado em c',c
