def findFactorial(x):
    if x<1:
        return 1
    else:
        return x*findFactorial(x-1)
def findFactorialUsingLoop(x):
    i=1
    product=1
    while i<=x:
        product=product*i
        i+=1
    return product
def findFactorialUsingRange(x):
    product=1
    for i in range(1,x+1):
        product=product*i
    return product
print(findFactorial(int(input("Give us the input"))))
print(findFactorialUsingRange(int(input("Give us the input"))))
print(findFactorialUsingLoop(int(input("Give us the input"))))

