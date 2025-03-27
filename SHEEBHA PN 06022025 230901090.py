#!/usr/bin/env python
# coding: utf-8

# In[13]:


#EXPERIMENT NUMBER 2: GETTING SCATTERED WITH PANDAS, PANDAS, DATA FRAME FUNCTOINS

import pandas as pd
df=pd.DataFrame()
print(df)


# In[12]:


import pandas as pd
emp=pd.Series(['Sheebha','Shivani','Kavya','Karunya','Raziel','Roxanne'])
id=pd.Series([80,90,28,57,49,99])
frame={'Emp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\n Series to Data Frame: \n")
print(result)


# In[15]:


import pandas as pd
print("\n Extracting One Column : \n")
print(result['Emp'])


# In[18]:


print('\n Adding New Column : \n')
result['ID']=pd.Series([80,90,28,56,89,97])
result['Age']=pd.Series([29,30,31,33,28,24])
print(result)


# In[19]:


print('\n Deleting New Column: \n')
del result['Age']
print(result)


# In[20]:


print("\n Extracting The Second Row: \n")
print(result.loc[1])


# In[21]:


print("\n Slicing rows :\n", result[1:4])


# In[27]:


d2=pd.DataFrame([['Vicky',100],['Rashid',109]], columns=['Emp','ID'])
print("\n Adding new row: \n ")
print(pd.concat([result,d2]))


# In[28]:


print("\n Deleting Particular row:\n", result.drop(2))


# In[ ]:




