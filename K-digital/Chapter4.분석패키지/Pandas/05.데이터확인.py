#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# ## DataFrame 확인
# 계산을 할 수 있는 데이터에 대해서 Column별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌

# In[6]:


df.describe()


# In[7]:


df.info()


# In[11]:


df.head() #c 처음 5개의 row를 가져옴


# In[14]:


df.head(7) # 처음부터 7개의 row를 가져옴


# In[16]:


df.tail() # 마지막 5개 row를 가져옴


# In[18]:


df.tail(3)  # 마지막 3개 row를 가져옴


# In[22]:


df.values  # 데이터가 2차원 배열로 출력


# In[20]:


df.index


# In[23]:


df.columns


# In[28]:


df.shape  # row, column 갯수를 보여준다. 타이틀 제외하고.


# In[27]:


df


# ## Series 확인

# In[30]:


df['키'].describe()


# In[31]:


df['키'].min()


# In[32]:


df['키'].max()


# In[34]:


df['키'].nlargest(3)  # 키 큰 사람 순서대로 3명 데이터


# In[35]:


df['키'].mean()


# In[36]:


df['키'].sum()


# In[39]:


df['SW특기'].count()  # Naan값 제외


# In[41]:


df['학교'].unique()  # 중복값 제외한 값


# In[43]:


df['학교'].nunique() # 중복값 제외한 값의 갯수

