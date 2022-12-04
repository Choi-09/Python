#!/usr/bin/env python
# coding: utf-8

# # 8. 데이터 선택(iloc)
# integer location.
# 위치를 이용하여 원하는 row에서 원하는 col을 선택

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[3]:


df.iloc[1]  # 0번째 행 위치의 데이터


# In[5]:


df.iloc[4] # 4번째 행 위치의 데이터


# In[7]:


df.iloc[0:5] # index 0~4 까지의 데이터


# In[10]:


df.iloc[0,2]   # 타이틀 제외,  index 1 row, index 2 col 데이터


# In[13]:


df.iloc[4,4]  # 타이틀 제외, index4 row, index 4 col 데이터


# In[15]:


df.iloc[[0,1],[4]]  # index 0,1 row 위치의 학생의 index 4 col('키') 데이터 출력


# In[17]:


df.iloc[[0,1], [5,6]]   # index 0,1 row 위치의 학생의 index 5,6 col('국어', '영어') 데이터 출력 


# In[19]:


df.iloc[0:5, 5:10]   # index 0~4  row 위치 학생의 index 5~9 col ('국어'~'사회') 데이터 출력
# int 슬라이싱의 경우 마지막 데이터 앞까지 불러온다!! 불포함!!!!


# In[ ]:





# In[ ]:




