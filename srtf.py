import sys

def disp(x, s):
	sys.stdout.write("\033[;1m")  #BOLD headings
	print s
	sys.stdout.write("\033[0;0m") #RESET to normal(default)
	for i in range(count):
		print 'P' + str(i+1) + '\t' + str(x[i])

def fileRead(arriv, burst, count):
	file = open("srtf.txt", "r")
	
	count = int(file.readline())
	
	for i in range(count):
		arriv.insert(i, int(file.readline()))
	
	for i in range(count):	
		burst.insert(i, int(file.readline()))
	
	return count	

def minIndex(l):

	m = count - 1
	while True:
		if (l < arriv[m]):
			m -= 1
		else:
			break
	return m	

def minValue(cop, n):
	new = []
	for i in range(n+1):
		new.insert(i, cop[i])
	return min(new)
		
def cal():
	n = 0
	last = 0
	copy = []
	for i in range(count):
		copy.insert(i, burst[i])
		
	line = arriv[0]	
	
	while True:
		print line
		
		n = minIndex(line)
		n = minValue(copy, n)

		index = copy.index(n)
		#print copy[index]
		copy[index] -= 1
		print copy
		
		line += 1
		
		if copy[index] == 0:
			last += 1
			copy[index] = 999999;
		print copy	
		if last == count: 
			break	

def waiting(sum):
	sum = 0
	for i in range(count):
		wait.insert(i, (turn[i] - burst[i]))
		sum += wait[i]
	disp(wait, '\nWaiting Time')
	return sum

def turnaround(sum):
	sum = 0
	for i in range(count):
		turn.insert(i, (end[i] - arriv[i]))
		sum += turn[i]
	disp(turn, '\nTurnaround Time')
	return sum
	
sum = 0
line = 0
count = 0
end = []
wait = []
turn = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

cal()

