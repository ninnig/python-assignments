

import math
import os
import random
import re
import sys


# Complete the 'biggerIsGreater' function below.

# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    ans = ''
    n=len(w)
    w=list(w)
    
   i=n-2
   while i>=0 and w[i]>=w[i+1]:
    i -= 1
    
if i== -1:
    ans="no answer"
else:
    j=n-1
    while j>=1 and w[j]<=w[i]:
        j-=1
        
w[i],w[j]=w[j],w[i]
w="".join(w)
ans=w[:i+1]+ w[:i+1][::-1]
return ans
