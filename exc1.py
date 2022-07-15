

from collections import OrderedDIct

od1=OrderedDIct()

for i in range (int(input())):
    word=input()
    if word not in od1:
        od1[word]=1
    else:
        od1[word]+=1

print (len(od1))
print (*od1.values())
