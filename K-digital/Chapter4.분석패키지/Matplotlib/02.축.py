#!/usr/bin/env python
# coding: utf-8

# # 2. 축

# In[6]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[2]:


x = [1,2,3]
y = [2,4,8]


# ### 그래프 제목,  제목 폰트, 폰트사이즈 정하기

# In[7]:


plt.plot(x,y)
plt.title('꺾은선 그래프', fontdict = {'family': 'Malgun Gothic', 'size':20})


# ### 축 이름 설정

# In[9]:


plt.plot(x,y)
plt.xlabel('X축')
plt.ylabel('Y축')


# ### 축이름과 폰트 색상 설정

# In[13]:


plt.plot(x,y)
plt.xlabel('X축', color = 'red')
plt.ylabel('Y축', color = '#00aa00')  # RGB컬러도 가능!


# ### 축 이름의 위치 설정

# In[14]:


plt.plot(x,y)
plt.xlabel('X축', color = 'red', loc = 'right')  # left, right, center 
plt.ylabel('Y축', color = '#00aa00', loc = 'top')  # top, bottom, center


# ### x,y축 틱 설정

# In[16]:


plt.plot(x,y)
plt.xticks([1,2,3])
plt.yticks([3,6,9,12])
plt.show()

