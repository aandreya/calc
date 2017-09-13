x = int(raw_input("Enter the 1st number: "))
print "1st chosen number is: " + str(x)
y = int(raw_input("Enter the 2nd number: "))
print "2nd chosen number is: " + str(y)

operation = raw_input("Choose computing operation (+ - * /=): ")

if operation == "+":
    print "Chosen operation is SUM: "
    print x + y
elif operation == "-":
    print "Chosen operation is DEDUCT: "
    print x - y
elif operation == "*":
    print "Chosen operation is MULTIPLY: "
    print x * y
elif operation == "/":
    print "Chosen operation is DIVISION: "
    print float (x) / float (y)
else:
    print "You did not choose valid mathematical operation!"
