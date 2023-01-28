string=input("Enter the string")
sumVow=0
sumCon=0
for z in string.replace(" ","").lower():
    if z.isalpha()==True:
        if z=="a"  or z=="e" or z=="i" or z=="o" or z=="u":
            sumVow=sumVow+1
        else:
            sumCon=sumCon+1
print("No of vowels",sumVow)
print("No of constant", sumCon)

        
dict1={}
dict2={}
for i in range(0,len(string)):
    if string[i].islower()==True:
        if string[i] in dict1:
            dict1[string[i]]+=1
        else:
            dict1[string[i]]=1
    elif string[i].isupper()==True:
        if string[i] in dict2:
            dict2[string[i]]+=1
        else:
            dict2[string[i]]=1
sum1=0
sum2=0
for k,j in dict1.items():
    sum1=sum1+j
print("No of lowercase letters",sum1)
for d,m in dict2.items():
    sum2=sum2+m
print("No of uppercase letters",sum2)
    
    
