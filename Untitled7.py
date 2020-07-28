#!/usr/bin/env python
# coding: utf-8

# In[2]:


dict1 = {21: "FTP", 22: "SSH", 23: "telnet", 80: "http"} 
newdict = dict([(value, key) for key, value in dict1.items()]) 
print(dict1)  
print()
print("keys: values") 
for i in newdict: 
    print(i, " :  ", newdict[i]) 


# In[11]:


list1 = [(1,2),(3,4),(4,5),(5,6)]
list2 = []
for tup in list1:
    res = sum(list(tup))
    list2.append(res)
print(list2)


# In[12]:


list1 = [(1,2,3),[1,2],['a','hit','less']]
list2 = []
for i in list1:
    list2 = list2 + list(i)
print(list2)


# In[ ]:





# In[ ]:





# In[ ]:




