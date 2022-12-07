#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리

# In[2]:


import matplotlib.pyplot as plt


# ## 1. 그래프 기본

# In[7]:


x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)  # 그래프 그리기
plt.show()  # 설명없이 그래프 그리기


# ### Title 설정

# In[8]:


plt.plot(x,y)
plt.title('Line Graph')


# ### 한글 폰트 설정

# In[14]:


import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기


# In[24]:


plt.plot(x,y)
plt.title('꺾은선 그래프')


# In[25]:


# 사용 가능한 폰트 확인 
import matplotlib.font_manager as fm
fm.fontManager.ttflist
[f.name for f in fm.fontManager.ttflist]


# ### 그래프에 - 기호 깨짐현상

# In[22]:


matplotlib.rcParams['axes.unicode_minus'] = False


# In[23]:


plt.plot([-1,0,1],[-5,-1,2])

