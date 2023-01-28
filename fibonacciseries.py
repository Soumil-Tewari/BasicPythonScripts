UserInput=int(input("Enter the number of terms of series"))
num1=0
print(num1)
num2=1
print(num2)
n=1
while n<= UserInput-2:
    num3=num2+num1
    num1=num2
    num2=num3
    print(num3)
    n+=1
    
