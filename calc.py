#function to add 2 numbers
def add(num1,num2):
    return num1+num2
#function to subtract 2 numbers
def sub(num1,num2):
    return num1-num2
#function to multiply 2 numbers
def multi(num1,num2):
    return num1*num2
#function to divide 2 numbers
def div(num1,num2):
    return num1/num2
print("Please select operation \n"\
"1.add\n"\
"2.sub\n"\
"3.multi\n"\
"4.div\n")
operation=int(input("Select operations from 1,2,3 and 4:"))
number1=int(input("Enter first number"))
number2=int(input("Enter second number"))
if operation==1:
    print(number1,"+", number2,"=",add(number1,number2))
elif operation==2:
    print(number1,"-", number2, "=", sub(number1,number2))
elif operation==3:
    print(number1,"*", number2, "=", multi(number1,number2))
elif operation==4:
    print(number1,"/", number2, "=", div(number1,number2))
else :
    print("Error")
