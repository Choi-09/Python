#!/usr/bin/env python
# coding: utf-8

# # 7. 여러 데이터

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[2]:


x = [1,2,3]
y = [2,4,8]


# In[3]:


plt.plot(x,y)


# ## COVID-19 백신 종류별 접종 인구

# In[5]:


days = [1,2,3]  # 10월 1일, 2일, 3일
az = [2,4,8]  # (단위: 만 명) 1일~3일까지 az 접종인구
pfr = [5,1,3]  #화이자
md = [1,2,5] # 모더나


# ### 세 데이터 합쳐 그리기

# In[6]:


plt.plot(days, az)
plt.plot(days, pfr)
plt.plot(days, md)


# In[8]:


plt.plot(days, az, label = 'az')
plt.plot(days, pfr, label = 'pfr', marker = 'o', ls = "--")
plt.plot(days, md, label = 'md', marker = 's', ls = "-.")

plt.legend() # 범례 호출 함수


# ### 레이블(레전드)에 컬럼 지정

# In[9]:


plt.plot(days, az, label = 'az')
plt.plot(days, pfr, label = 'pfr', marker = 'o', ls = "--")
plt.plot(days, md, label = 'md', marker = 's', ls = "-.")

plt.legend(ncol=3) # 범례 호출 함수

