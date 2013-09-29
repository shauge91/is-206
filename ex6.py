# Assigning variable x a value (string + other value)
x = "There are %d types of people." % 10
#assigning variable a string value
binary = "binary"
#assigning variable a string value
do_not = "don't"
#assigning variable a string value and other values 
y = "Those who know %s and those who %s." % (binary, do_not)

#print variable x
print x
#print variable y
print y

#print a string and variable x 
print "I said: %r." %x
#print a string and variable y
print "I also said: '%s'." % y

#set boolean hilarious value false
hilarious = False
#assign variable a string value
joke_evaluation = "Isn't that joke so funny?! %r"

#print variable joke_evaluation and hilarious 
print joke_evaluation % hilarious 

#assign variable a string value 
w = "This is the left side of..."
#assign variable a string value 
e = "a string with a right side."

# print variable w and e which makes a longer string 
print w + e 