import multiprocessing as mp

NUMCPU = int(mp.cpu_count())

def collatz(N):
	c = N
	while not c == 1:
		#If c is a number 2**i, i a natural number > 1
		#the sequence converges
		if log(c,2).is_integer():
			break
		if c % 2 == 0:
			c = c / 2
		else:
			c = 3*c + 1
	return True

def main(my_n, total_num):
	z = my_n
	while True:
		for n in xrange(10L**z,10**(z + 1)):
			if collatz(n):
				print n,"OK"
			else:
				print n,"NOK"
				break
		z += total_num
	return False

Threads = [mp.Process(target=main, args=(x,NUMCPU)) for x in range(NUMCPU)]
for p in Threads:
	p.start()

# Exit the completed processes
for p in Threads:
	p.join()
