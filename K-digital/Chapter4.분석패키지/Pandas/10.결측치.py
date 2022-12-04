#!/usr/bin/env python
# coding: utf-8

# # 10. 결측치
# 비어있는 데이터

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# ## fillna 데이터 채우기

# ### (1) DataFrame 전체의 NaN 데이터 채우기

# In[2]:


df.fillna('')  # NaN 데이터를 빈칸으로 채움


# In[4]:


df.fillna('없음')


# In[9]:


import numpy as np
df['학교']= np.nan  # '학교' 데이터 전체를 NaN 으로 채움
df


# In[10]:


df.fillna('모름')


# In[14]:


df.fillna('모름', inplace = True)
df


# ### (2) DataFrame 일부의 Nan 데이터 채우기

# In[15]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[20]:


df['SW특기'].fillna("확인 중", inplace = True)  #SW특기 데이터 중에서 NaN에 대해서 채움
df


# ## dropna 데이터 제외하기

# ### (1) DataFrame 중에서 모든 NaN 데이터 삭제

# In[41]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[25]:


df.dropna(inplace = True)
df


# ### (2) DataFrame 일부의 NaN 데이터 삭제

# In[27]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# + axis: index(0) or columns(1)
# + how: any or all

# In[29]:


df.dropna(axis='index', how = 'any')  # NaN 데이터가 하나라도 있는 row 데이터 삭제


# In[36]:


df.dropna(axis = 1)  # NaN이 하나라도 있는 column 삭제


# In[38]:


df['학교'] = np.nan
df


# In[40]:


df.dropna(axis = 1, how = 'all')   # column 전체가  NaN인 경우에 해당 column 삭제


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




