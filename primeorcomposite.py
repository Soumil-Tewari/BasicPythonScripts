num=int(input("Enter a number"))
if num!=0 and num!=1:
    condition=False
    for i in range(2,num):
        if num%i==0:
            condition=True
            break

    if condition==True:
        print(num, "is composite")
    else :
        print(num, "is prime")
else:
    print("The number is neither prime nor composite")
        
