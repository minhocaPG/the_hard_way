def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide (a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
def cube (a):
	print "CUBE %d * %d * %d" % (a, a, a)
	return a * a * a
	
print "Let's do some math with just functions!"

age = add (24, 34)
height = subtract(100, 1023)
weight = multiply(500, 2)
iq = divide (100, 1)
sleep = cube (2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Sleep: %d" % (age, height, weight, iq, sleep)

# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = divide(age, subtract(iq, add(weight,23 )))


print "That becomes: ", what, "Can you do it by hand?"
