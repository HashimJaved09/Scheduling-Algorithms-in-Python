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
	qt = []
	io = []
	iow = []
	copy = []
	line = arriv[0]
	for i in range(count):
		qt.insert(i, QT)
		io.insert(i, IO)
		iow.insert(i, 0)
		copy.insert(i, burst[i])

	while n != count:
		i = 0

		for i in range(count):
		
			if copy[i] != 999999:
				if copy[i] <= qt[i]:
					if i%2 != RE:      		#I/O wale process
						if copy[i] <= io[i] & iow[i] <= line:
							line += copy[i]
							qt[i] = 999999;
							io[i] = 999999;
							iow[i] = 999999;						
							copy[i] = 999999;	
							end.insert(i, line)

						elif copy[i] > io[i] & iow[i] <= line:
							line += io[i]
							qt[i] -= io[i]
							iow[i] = line + IOW 
							copy[i] -= io[i]
					else:
						line += copy[i]
						qt[i] = 999999;
						#io[i] = 999999;
						copy[i] = 999999;
						end.insert(i, line)							
			
				elif copy[i] > qt[i]:
					if i%2 != RE:      		#I/O wale process
						if copy[i] <= io[i] & iow[i] <= line:
							line += qt[i]
							io[i] -= qt[i]					
							copy[i] -= qt[i]	

						elif copy[i] > io[i] & iow[i] <= line:
							if qt[i] >= io[i]:
								line += io[i]
								qt[i] -= io[i]
								iow[i] = line + IOW
								copy[i] -= io[i]
							elif qt[i] < io[i]:
								line += qt[i]
								io[i] -= qt[i] 
								copy[i] -= qt[i]
					else:
						line += QT
						copy[i] -= QT			 			
				
				if qt[i] == 0:
					qt[i] = QT;
				if io[i] == 0:
					io[i] = IO;	
				if copy[i] == 999999:
					n += 1
		print copy, qt, io
	print iow
			#print i, copy	

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
start = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)

QT = int(input('Enter Quantum Time : '))
IO = int(input('Enter I/O Interrupt Time : '))
RE = int(input('Enter 0 for EVEN Process Interrupts or 1 for ODD : '))
IOW = int(input('Enter I/O Waiting Time : '))

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
