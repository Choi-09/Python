#!/usr/bin/env python
# coding: utf-8

# # 11. 누적 막대 그래프

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[3]:


df = pd.read_excel('../Pandas/score.xlsx',)
df


# ### 겹치는 막대 그래프

# In[6]:


plt.bar(df['이름'], df['국어'])
plt.bar(df['이름'], df['영어'])


# ### 누적 막대 그래프(2 데이터)

# In[14]:


plt.bar(df['이름'],df['영어'])
plt.bar(df['이름'],df['국어'],bottom = df['영어'])


# ### 누적 막대 그래프 (3 데이터)

# In[18]:


plt.bar(df['이름'],df['영어'])
plt.bar(df['이름'],df['국어'],bottom = df['영어']) #영어를 밑에
plt.bar(df['이름'],df['수학'],bottom = df['국어']+df['영어'])  # 국어, 영어 모두 밑에 


# ### label, xticks 설정

# In[19]:


plt.bar(df['이름'],df['영어'], label = "영어")
plt.bar(df['이름'],df['국어'],label = '국어', bottom = df['영어']) #영어를 밑에
plt.bar(df['이름'],df['수학'],label = '수학', bottom = df['국어']+df['영어'])  # 국어, 영어 모두 밑에 

plt.xticks(rotation = 60)

