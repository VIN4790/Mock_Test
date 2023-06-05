#!/usr/bin/env python
# coding: utf-8

# In[33]:


def solution(arr):    
    arr2=[]
    j=0
    for i in range(len(arr)):
        if arr[i]==0:
            arr2.append(arr[i])
        
        else:
            arr2.insert(j,arr[i])
            j=j+1
    return arr2
              
print(solution([0,1,0,12,3]))
    
        


# In[ ]:




