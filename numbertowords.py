dic={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",
     9:"Nine",0:"Zero"}
number=int(input("Enter a number"))
length=len(str(number))
numberInString=str(number)
text=""
for i in numberInString:
           text=text+dic[int(i)]+" "
print(text)
           


           
     
     
