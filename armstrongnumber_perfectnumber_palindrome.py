
num1=input("Enter a number")
#check for armstrong number
length=len(num1)
summation=0
#fetching sum
for i in num1:
    value=int(i)
    value=value**length
    summation=summation+value
if summation==int(num1):
    print(num1, "is an Armstrong number")
else:
    print(num1,"is not an Armstrong number")

#check for palindrome
alpha=0
beta=len(num1)-1
gamma=0
while gamma<=length-1:
    if num1[alpha]!=num1[beta]:
        print(num1, "is not a palindrome")
        break
    
    gamma+=1
    alpha+=1
    beta-=1
else:
    print(num1, "is a palindrome")
      

    
#check for perfect number
sumPN=0
for k in range(1,int(num1)):
    if int(num1)%k==0:
        sumPN=sumPN+k
if sumPN==int(num1):
    print(num1, "is a perfect number")
else:
    print(num1, "is not a perfect number")

        
    
    
    
           
