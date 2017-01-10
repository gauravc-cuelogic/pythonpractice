x = "There are %d types of people"  % 10 #directly printing value
binary = "binary" # decalaring string value
do_not = "don't"  # decalaring string value
y = "those who know %s and those who %s" % (binary, do_not) #writing two values in a variable

print x 
print y

print "I said : %s again %r" % (x, x) #concenating string and then printing (why we used %r here instread of %s)
print "I also said: %s" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny? ! %r" # %r prints raw data hence it is useful for debugging

print joke_evaluation % hilarious

a = "this is left side of .."
b = "this is right side of string"

print a + b
