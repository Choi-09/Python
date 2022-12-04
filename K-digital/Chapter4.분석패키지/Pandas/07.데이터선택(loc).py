#!/usr/bin/env python
# coding: utf-8

# # 7. 데이터 선택(loc)
# 이름을 이용하여 원하는 row에서 원하는 column 을 선택

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[8]:


df.loc['1번']  # index '1번'에 해당하는 전체 데이터 


# In[15]:


# df.loc['5번'] #?? 


# In[17]:


df.loc['1번', '국어']  # index '1번'에 해당하는 국어 데이터


# In[21]:


df.loc[['1번', '2번'], '영어']  # index '1번', '2번'에 해당하는 영어 데이터


# In[23]:


df.loc[['1번', '2번'], ['영어', '수학']]   # index '1번', '2번'에 해당하는 영어, 수학 데이터


# In[27]:


df.loc['1번':'6번', '국어': '사회'] # index '1번' ~'5번'까지, '국어' ~ '사회' 까지의 데이터.
# 끝 데이터도 포함!! 

