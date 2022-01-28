def countEachElement(text):
    text=text.split()
    newText=""
    for i in text:
        newText=newText+i
    dic={}
    for i in newText.lower():
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    return dic
  
print(type(countEachElement("I am moving on in Python")))