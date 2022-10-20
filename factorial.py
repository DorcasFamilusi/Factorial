def factorial(num): #7*6*5*4*3*2*1-num
    fact = 1
    while(num != 0):
        fact *= num
        num = num-1
    print("Factorial is", fact)

num = int(input('Enter a number: '))
factorial(num)

