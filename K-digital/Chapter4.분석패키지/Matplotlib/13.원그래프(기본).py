#!/usr/bin/env python
# coding: utf-8

# # 13. 원 그래프(기본)

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# ### 원 그래프 그리기
# + labels: 레이블 표시 
# + autopct : 비율 표시 
# + startangle: 시작점 설정
# + counterclock: 시계방향(F), 반시계방향(T) 설정

# In[9]:


values = [30, 25, 20,13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'ETC']

plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False)  # labels: 레이블 넣기  # autopct: 비율표시 ('%.1f : 소숫점첫째자리까지')
plt.show()                                                                                       # ('%.1f%% : 소숫점첫째자리, %기호까지') 


# ### 그래프 간격 띄우기
# + explode

# In[16]:


values = [30, 25, 20,13, 10, 2]
# values = [1,1,1,1,1,1]  :꼭 합100을 맞출 필요는 없다. 비율로도 가능 
labels = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'ETC']

#explode = [0.2,0.1,0,0,0,0]
explode = [0.05]*6

plt.pie(values, labels=labels, explode = explode)
plt.show()


# ### 범례(legend)
# + legend

# In[20]:


plt.pie(values, labels = labels, explode = explode)
plt.legend(loc = (1.2,0.3))
plt.show()


# ### 그래프, 범례 제목
# + title

# In[24]:


plt.pie(values, labels = labels, explode = explode)
plt.title('언어별 선호도')
plt.legend(loc = (1.2,0.3), title = '언어별 선호도')
plt.show()

