#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7,2,bob,10,and 4 and matche the output below.
#Desired output: Invalid input
#                Maximum is 10
#                Minimum is 2

smallest=None
largest=None
while True:
    sval=input('enter a value:')
    if sval=='done':
        break
    try:
        ival=int(sval)
    except:
        print('Invalid input')
        continue
    if smallest is None and largest is None:
        smallest=ival
        largest=ival
    elif ival<smallest:
            smallest=ival
    elif ival>largest:
        largest=ival
print('Maximum is',largest)
print('Minimum is', smallest)



