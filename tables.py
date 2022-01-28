def findTable(number,tablesUpTo):
    for i in range(1,tablesUpTo+1):
        print(f"{number}X{i} ={number*i}")
print("Table Calculator")
findTable(int(input("Enter the number")),int(input("No Upto")))