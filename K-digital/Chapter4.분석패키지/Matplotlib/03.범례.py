#!/usr/bin/env python
# coding: utf-8

# # 3. 범례(legend)
# 그래프의 데이터가 어떤 것인지 알려준다.

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


# ### 범례 레전드 함수 호출

# In[3]:


plt.plot(x,y,label = '무슨 데이터?')
plt.legend()


# ### 범례 위치 설정

# In[4]:


plt.plot(x,y,label = '무슨 데이터?')
plt.legend(loc = 'upper right') 


# In[6]:


plt.plot(x,y,label = '무슨 데이터?')
plt.legend(loc = (0.5, 0.5))  # X축, Y축 기준으로 범례 위치 설정 (0~1사이)


# ![%EB%B2%94%EB%A1%80%EC%9C%84%EC%B9%98.PNG](attachment:%EB%B2%94%EB%A1%80%EC%9C%84%EC%B9%98.PNG )
