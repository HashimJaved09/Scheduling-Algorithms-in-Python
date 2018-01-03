import sys

def disp(x, s):
	sys.stdout.write("\033[;1m")  #BOLD headings
	print s
	sys.stdout.write("\033[0;0m") #RESET to normal(default)
	for i in range(count):
		print 'P' + str(i+1) + '\t' + str(x[i])

def fileRead(arriv, burst, count):
	file = open("fcfs.txt", "r")
	
	count = int(file.readline())
	
	for i in range(count):
		arriv.insert(i, int(file.readline()))
	arriv.sort()
	
	for i in range(count):	
		burst.insert(i, int(file.readline()))
	
	return count	

def cal(sum):
	sum = arriv[0]
	for i in range(count):
		sum = sum + burst[i]
		end.insert(i, sum)
	disp(end, '\nCompletion Time')

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
count = 0
end = []
wait = []
turn = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

cal(sum)

sum = turnaround(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Turnaround Time : ' + str(avg)
sys.stdout.write("\033[0;0m") 			#RESET to normal(default)

sum = waiting(sum)

avg = float(sum)/count

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
print '\nAverage Waiting Time : ' + str(avg)
