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
		
def cal(waitSum, turnSum):
	copy = []
	for i in range(count):
		copy.insert(i, burst[i])

	copy.append(99999)
	time = 0
	last = 0
	j = count  	
	while last != count:
		index = j
		i = 0        
		while i < count:
		    	if arriv[i] <= time and copy[i] < copy[index] and copy[i] > 0:
		        	index = i
		    	i += 1       
		copy[index] -= 1
		if copy[index] == 0:
		    	last += 1
		    	endTime = time + 1
			end.insert(index, endTime)

		    	waitSum += endTime - burst[index] - arriv[index]
			wait.insert(index, endTime - burst[index] - arriv[index])

		    	turnSum += endTime - arriv[index]
			turn.insert(index, endTime - arriv[index])
	    	time += 1
	return waitSum, turnSum
	
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
	
count = 0
waitSum = 0
turnSum = 0
end = []
wait = []
turn = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

waitSum, turnSum = cal(waitSum, turnSum)

disp(wait, '\nWaiting Time')

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
avg = float(waitSum)/count
print '\nAverage Waiting Time : ' + str(avg)

disp(turn, '\nTurnaround Time')

sys.stdout.write("\033[1;33m")			#setting text color to YELLOW
avg = float(turnSum)/count
print '\nAverage Turnaround Time : ' + str(avg)
