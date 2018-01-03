import sys

def disp(x, s):
	sys.stdout.write("\033[;1m")  #BOLD headings
	print s
	sys.stdout.write("\033[0;0m") #RESET to normal(default)
	for i in range(count):
		print 'P' + str(i+1) + '\t' + str(x[i])

def fileRead(arriv, burst, count):
	file = open("rr.txt", "r")
	
	count = int(file.readline())
	
	for i in range(count):
		arriv.insert(i, int(file.readline()))
	
	for i in range(count):	
		burst.insert(i, int(file.readline()))
	
	return count

def cal(line):
	i = 0
	n = 0 
	copy = []
	line = arriv[0]
	for i in range(count):
		copy.insert(i, burst[i])

	while n != count:
		i = 0
		
		for i in range(count):
		
			if copy[i] != 999999:
				if copy[i] <= QT:
					line += copy[i]
					copy[i] = 999999;
					end.insert(i, line)
			
				elif copy[i] > QT:
					line += QT
					copy[i] -= QT
					#end.insert(i, line)			 			
			
				if copy[i] == 999999:
					n += 1
					#break
			#print i, copy	

def waiting(sum):
	sum = 0
	for i in range(count):
#		wait.insert(i, (turn[i] - burst[i]))
		wait.insert(i, (start[i] - arriv[i]))
		sum += wait[i]
	disp(wait, '\nWaiting Time')
	return sum

def waiting(sum):
	sum = 0
	for i in range(count):
		wait.insert(i, (turn[i] - burst[i]))
#		wait.insert(i, (start[i] - arriv[i]))
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
QT = int(input('Enter Quantum Time : '))
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

cal(line)

disp(end, '\nCompletion Time')

sum = turnaround(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Turnaround Time : ' + str(avg)

sum = waiting(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Waiting Time : ' + str(avg)
