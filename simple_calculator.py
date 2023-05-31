# defining functions for the maths taking the numbers as arguements
def add(num1,num2):
    sum = num1+num2
    print('equals')
    print(sum)   
def minus(num1,num2):
    sum = num1-num2
    print('equals')
    print(sum)   
def multiply(num1,num2):
    sum = num1 * num2
    print('equals')
    print(sum)
def divide(num1,num2):
    sum = num1 / num2
    print('equals')
    print(sum)

# defining the function that takes the users input to choose what math function to do
def user_input():
    try:
        # taking the users input choice and converting it to an integer and prints error message on ValueError
        print('1=add 2=minus 3=multiply 4=divide')
        chosen_operation = input('selection: ')
        math(int(chosen_operation))
    except ValueError:
        print('enter number 1-4')
    except:
        print('something went wrong')

# function that takes the users choice in an arguement
def math(choice):
    try:
        # depending on the users choice it sends numbers as arguements with the function
        if(choice == 1):
            num1=int(input('enter first number to add: '))
            num2=int(input('enter second number to add: '))
            add(num1,num2)
        elif(choice == 2):
            num1=int(input('enter first number to subtract: '))
            num2=int(input('enter second number to subtract: '))
            minus(num1,num2)
        elif(choice == 3):
            num1=int(input('enter first number to multiply: '))
            num2=int(input('enter second number to multiply: '))
            multiply(num1,num2)
        elif(choice == 4):
            num1=int(input('enter first number: '))
            num2=int(input('enter second number: '))
            divide(num1,num2)
    # prints error message if wrong value entered
    except ValueError:
        print('enter valid number')
    except:
        print('something went wrong')
# starts the first function where a user has to select which function
user_input()