num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
listCompare=[num1,num2]
MinValue=min(listCompare)
HCF=1
for i in range(1,MinValue+1):
    if num1%i==0 and num2%i==0:
        HCF=i

print("Greatest common divisor",HCF)
print("Least common multiple",num1*num2/HCF)
