#import #argv from sys 
from sys import argv

script, filename = argv

#open file by given filename 
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read() #function on text, read command with no parameters

print "Type the filename again:"
file_again = raw_input("> ")

#open file by given filename
txt_again = open(file_again)
#print file 
print txt_again.read()