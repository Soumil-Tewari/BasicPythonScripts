tuple1=eval(input("Enter a tuple"))
userQuery=(input("Enter the element to seek for"))
userRemark=input("Is userQuery string(s) or int(i)[ s for string, i for int")
if userRemark=="s":
    userQuery=userQuery
else:
    userQuery=int(userQuery)
if userQuery in tuple1:
    print(userQuery,"found")
else:
    print(userQuery, "not found")
