import sys

def disp(x, s):
	sys.stdout.write("\033[;1m")  #BOLD headings
	print s
	sys.stdout.write("\033[0;0m") #RESET to normal(default)
	for i in range(count):
		print 'P' + str(i+1) + '\t' + str(x[i])

def fileRead(arriv, burst, count):
	file = open("sjf.txt", "r")
	
	count = int(file.readline())
	
	for i in range(count):
		arriv.insert(i, int(file.readline()))
	
	for i in range(count):	
		burst.insert(i, int(file.readline()))
	
	return count	

def minIndex(l):
	if l >= arriv[count-1]: 
		return count-1 
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
	last = 1
	copy = []
	line = arriv[0]
	start.insert(0, arriv[0])

	for i in range(count):
		copy.insert(i, burst[i])
	line += copy[0]
	end.insert(0, line)
	copy[0] = 999999;
	
	while True:
		n = minIndex(line)
		n = minValue(copy, n)
		index = copy.index(n)
		
		start.insert(index, line)
		line += burst[index]
		end.insert(index, line)
		copy[index] = 999999;
		
		last += 1
		if last == count: 
			break	

def waiting(sum):
	sum = 0
	for i in range(count):
#		wait.insert(i, (turn[i] - burst[i]))
		wait.insert(i, (start[i] - arriv[i]))
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
start = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

cal()

disp(end, '\nCompletion Time')

sum = turnaround(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Turnaround Time : ' + str(avg)

sum = waiting(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Waiting Time : ' + str(avg)
