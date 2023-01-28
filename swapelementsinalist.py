listSwap=eval(input("Enter a list of numbers"))
length=len(listSwap)
if length%2!=0:
    length=length-1
for i in range(0,length,2):
    listSwap[i],listSwap[i+1]=listSwap[i+1],listSwap[i]
print(listSwap)

