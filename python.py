# CALCULATOR
A=input("enter an operator (+, -, *, /): ")
B=float(input("choose your First number "))
C=float(input("choose your Second number "))

if A== "+":
    RESULT=(B+C)
    print (f" here is your result:{RESULT}")
elif A== "-":
    RESULT=(B-C)
    print (f" here is your result:{RESULT}")
elif A== "*":
    RESULT=(B*C)
    print (f" here is your result:{RESULT}")
elif A== "/":
    RESULT=(B/C)
    print (f" here is your result:{RESULT}")

