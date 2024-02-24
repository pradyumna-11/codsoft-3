first_num = float(input("Enter first number : "))
op = input("Select an operator (+,-,*,/) : ")
second_num = float(input("Enter second number : "))
if(op=='+'):
    result = first_num+second_num
    print(first_num,op,second_num,"=",result)
elif(op=='-'):
    result = first_num-second_num
    print(first_num,op,second_num,"=",result)
elif(op=='*'):
    result = first_num*second_num
    print(first_num,op,second_num,"=",result)
elif(op=='/'):
    try:
        result = first_num/second_num
        print(first_num,op,second_num,"=",result)
    except ZeroDivisionError:
        print("Division by zero is not possible please try with another number")
else:
    print("Enter a valid operator")
        

    