#!/usr/bin/env python
# coding: utf-8

# # 11. 데이터 정렬
# 데이터를 어떤 기준에 따라 정렬

# In[71]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[2]:


df.sort_values('키')  #'키' 기준으로 오름차순 정렬


# In[10]:


df.sort_values('키',ascending = False)  # 키 기준으로 내림차순


# In[16]:


df.sort_values(['수학', '영어'], ascending = False)  # 수학, 영어 점수 기준으로 내림차순. 수학이 동점일 경우 영어가 높은 사람이 먼저나온다.


# In[19]:


df.sort_values(['수학', '영어'])  # 수학, 영어 점수 기준으로 오름차순. 수학이 동점일 경우 영어가 낮은 사람이 먼저 나옴


# In[68]:


df.sort_values(['수학', '영어'], ascending = [True, False])  # 수학 점수는 오름차순, 영어점수는 내림차순. 수학이 동점일 경우 영어가 높은 사람이 먼저 나옴


# In[25]:


df['키'].sort_values()


# In[26]:


df['키'].sort_values(ascending = False)


# In[76]:


df.sort_index()    # 여기서 정렬이 안되는 버그발생했는데.. 엑셀파일 지원번호에 공백이 들어간 row  있어서 발생했다!

