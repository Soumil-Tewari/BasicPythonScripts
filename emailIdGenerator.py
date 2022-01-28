def emailIdGenerator(name,domainName):
    formattedName=""
    nametoList=name.split()
    for nameParts in nametoList:
        formattedName=formattedName+nameParts
    formattedName=formattedName.lower()
    emailAddress=formattedName+"@"+domainName
    return f"{name}<{emailAddress}>"
print(emailIdGenerator("William Henry Gates (Bill Gates)","microsoft.com"))
