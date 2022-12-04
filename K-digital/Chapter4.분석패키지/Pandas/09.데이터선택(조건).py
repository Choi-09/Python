#!/usr/bin/env python
# coding: utf-8

# # 9. 데이터 선택(조건)
# 조건에 해당하는 데이터 선택

# In[9]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[11]:


df['키'] >= 185  # 학생들의 키가 185 이상 여부를 True / False 


# In[13]:


filt = (df['키']>=185) # 필터를 적용해서 키가 185 이상(조건)인 학생만 반환
df[filt]


# In[15]:


df[~filt] # not filt인 학생 데이터만 추출


# In[16]:


df[df['키']>=185]


# In[20]:


df.loc[filt, '수학']  # 키가 185이상인 학생들의 '수학'데이터


# In[22]:


df.loc[filt, ['영어','수학', '과학']]  # 키가 185 이상인 학생들의 '영어', '수학', '과학' 데이터


# ## 다양한 조건

# ### (1)  & 조건: 그리고

# In[25]:


df.loc[filt & (df['학교'] == '북산고')]  # 키가 185 이상인 '북산고' 학생 데이터


# ### (2)  | 조건: 또는

# In[27]:


df.loc[(df['키']<170) | (df['키']>200)]  # 키가 170 미만이거나 200 초과인 학생 데이터


# ### (3)  str 함수

# In[29]:


filt = df['이름'].str.startswith('송')  #'송'씨 성을 가진 사람
df[filt]


# In[31]:


filt = df['이름'].str.contains('태')  #이름에 '태'가 들어가는 사람
df[filt]


# In[32]:


df[~filt]  # 이름에 '태'가 들어가지 않는 사람


# In[36]:


lang = ["Python", "Java"]
filt = df["SW특기"].isin(lang)  # SW특기가 "Python" 이거나 "Java"인 학생 추출
df[filt]


# In[37]:


df


# In[41]:


lang = ["python", "java"]
filt = df['SW특기'].str.lower().isin(lang)  # SW특기를 모두 소문자로 바꿔서 PYTHON 이라고 적은 태산 학생까지 추출
df[filt]


# In[46]:


filt = df['SW특기'].str.contains("Java", na = False)  # NaN 데이터에 대해서 False 설정
df[filt]


# + dtype = bool 을 확인 해 보았을 때 True, False가 나와야 데이터에 접근하고 추출/변경 등이 가능한데 Nan 데이터는 T/F가 아닌 NaN이기 때문에 데이터를 찾을 때 오류가 뜬다. 그래서 na = True or na = False 를 설정해줘야함!

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




