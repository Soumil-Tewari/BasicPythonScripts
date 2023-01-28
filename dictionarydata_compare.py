numberOfStudents=int(input("Enter number of students"))
dict1={}
for i in range(0,numberOfStudents):
    RollNum=int(input("Enter roll number for student {}".format(i+1)))
    Name=input("Enter the name")
    Marks=int(input("Enter Marks scored"))
    studList=[RollNum,Name,Marks]
    dict1[i]=studList
print("Names of students above 75 marks")
for k in dict1.values():
    if k[2]>75:
        print(k[1])
                     
                     



