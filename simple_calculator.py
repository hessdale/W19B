


def add(num1,num2):
    sum = num1+num2
    print(sum)
    return(sum)
    
def minus(num1,num2):
    sum = num1-num2
    print(sum)
    return(sum)

def multiply(num1,num2):
    sum = num1 * num2
    print(sum)
    return(sum)

def divide(num1,num2):
    sum = num1 / num2
    print(sum)
    return(sum)


def get_operation():
    while(True):
        try:
            choose_operation = input('1=add 2=minus 3=multiply 4=divide  ')
            if(choose_operation == '1'):
                num1=int(input('enter first number to add'))
                num2=int(input('enter second number to add'))
                add(num1,num2)
            elif(choose_operation == '2'):
                num1=int(input('enter first number to subtract'))
                num2=int(input('enter second number to subtract'))
                minus(num1,num2)
            elif(choose_operation == '3'):
                num1=int(input('enter first number to multiply'))
                num2=int(input('enter second number to multiply'))
                multiply(num1,num2)
            elif(choose_operation == '4'):
                num1=int(input('enter first number'))
                num2=int(input('enter second number'))
                divide(num1,num2)
        except ValueError:
            print('enter number 1-4')
        except:
            print('something went wrong')

get_operation()

