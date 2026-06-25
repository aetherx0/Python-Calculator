# CALCULATOR
A=input("enter an operator (+, -, *, /): ")
B=float(input("choose your first number "))
C=float(input("choose your second number "))

if A== "+":
    RESULT=(B+C)
    print (f" here is your result:{RESULT}")
elif A== "-":
    RESULT=B-C
    print (f" here is your result:{RESULT}")
elif A== "*":
    RESULT=(B*C)
    print (f" here is your result:{RESULT}")
elif A== "/":
    RESULT=(B/C)
    print (f" here is your result:{RESULT}")

