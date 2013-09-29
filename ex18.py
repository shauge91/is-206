# this one is like your scripts with argv
def print_two(*args): # we tell python we want to make a function using def for define. And give it a name (print_two), and tells it we want asterisk args
    arg1, arg2 = args #unpacks the arguments 
    print "arg1: %r, arg2: %r" % (arg1, arg2) #print arguments out
		
# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): #we can skip the whole unpacking args and just use the names we want
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments 
def print_none():
    print "I got nothin'."


print_two ("Zed", "Shaw")
print_two_again ("Zed", "Shaw")
print_one ("First!")
print_none()