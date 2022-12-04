#!/usr/bin/env python
# coding: utf-8

# # 6. 데이터 선택(기본)

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# ## column 선택(label)

# In[3]:


df['이름']


# In[4]:


df[['이름', '키']]


# ## Column 선택(정수 index)

# In[5]:


df.columns


# In[8]:


df.columns[0]  # column이 너무 많아 처음부터 이름을 모르는 경우에는 인덱스 번호를 통해 컬럼명을 알아낸 후 데이터에 접근 가능


# In[7]:


df.columns[2]


# In[12]:


df[df.columns[2]] # df['이름'] 과 동일한 동작


# In[14]:


df[df.columns[-1]] # 맨 우측 끝에 있는 값을 가져옴


# ## 슬라이싱

# In[15]:


df


# In[17]:


df['영어'][:4]  # 타이틀 제외 0~ 3까지 4명의 영어 점수 데이터를 가져옴


# In[20]:


df[['이름', '키']][:3]  # 0~2까지 3명의 이름, 키 정보를 가져옴


# In[21]:


df[3:]

