#checking
print 'Standard Hello World'

x = 7
y = 7
spam = 'eggs'
print x

print spam * y

print y + x

print y % x

print str(y) + str(x)

 
print 'What is your name? '

x = raw_input()

print 'Hello, ' + x + ' How many time do you want to times your name by?'
foo = raw_input()

try: 
	foo = int(foo)
	print x * foo
except ValueError:
	print 'I cant times a name by an int!!'
 

		
	 	




