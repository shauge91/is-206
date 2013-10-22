
numbers = []

def loop(end, first): 
	i = 0 
	while i < end:
		print "At the top i is %d" % i 
		numbers.append(i)
	
		i = i + first
		print "Numbers now: ", numbers 
		print "At the bottom i is %d" % i 

number = raw_input("End number >")
number = int(number)
second = raw_input("Increase by >")
second = int(second)	
	
loop(number, second)	

print "The numbers: "

for num in numbers:
	print num 