#James Zhao
#Nov 18
#Period 7
#Simple Calculator


#Initialize


#Functions
def addition():
    print('The notation for addition is: addend + addend = sum.')
    print('Please enter integers only.')
    addend1 = int(input('What is your first addend?'))
    addend2 = int(input('What is your second addend?'))
    sum = addend1 + addend2
    print('The sum is ' + str(sum) + '.')

def subtraction():
    print('The notation for subtraction is: minuend - subtrahend = difference.')
    print('Please enter integers only.')
    minuend = int(input('What is your minuend?'))
    subtrahend = int(input('What is your subtrahend?'))
    difference = minuend - subtrahend
    print('The difference is ' + str(difference) + '.')

def multiplication():
    print('The notation for multiplication is: factor * factor = product.')
    print('Please enter integers only.')
    factor1 = int(input('What is your first factor?'))
    factor2 = int(input('What is your second factor?'))
    product = factor1 * factor2
    print('The product is ' + str(product) + '.')

def division():
    print('The notation for division is: dividend / divisor = quotient.')
    print('Please enter integers only.')
    dividend = int(input('What is your dividend?'))
    divisor = int(input('What is your divisor?'))
    try:
        quotient = dividend / divisor
        print('The quotient is ' + str(quotient) + '.')
    except:
        print('The divisor cannot be 0!')
def sqrt():
    print('The notation for taking the square root is: sqrt(radicand) = root.')
    radicant = int(input('What is your radicand?'))
    try:
        root = radicant ** 0.5
        print('The root is ' + str(root) + '.')
    except:
        print('The radicand must be a nonnegative rational number!')

def openSimpleCalculator():
    print('Welcome to the Simple Calulator by Casio!')
    while True:
        print('\nWhat type of operation will you be using?')
        print('''
                1. Add
                2. Subtract
                3. Multiply
                4. Division
                5. Square Root
                6. Quit
                ''')
        operation = str(input('Please enter "1", "2", "3", "4", "5", or "6"'))
        if operation == '1':
            addition()
        elif operation == '2':
            subtraction()
        elif operation == '3':
            multiplication()
        elif operation == '4':
            division()
        elif operation == '5':
            sqrt()
        elif operation == '6':
            print('Have a good day!')
            break
        else:
            print('Please enter "1", "2", "3", "4", "5", or "6"')

#Main
openSimpleCalculator()
