#!/usr/bin/env python
# coding: utf-8

# # 14. 원그래프 심화

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[4]:


values = [30, 25, 20,13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'ETC']

plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False)  # labels: 레이블 넣기  # autopct: 비율표시 ('%.1f : 소숫점첫째자리까지')
plt.show() 


# ### 색 변경

# In[12]:


values = [30, 25, 20,13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'ETC']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf','#9bf6ff', '#a0c4ff']

plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False, colors = colors)
plt.show() 


# ### 그래프 간격 띄우기

# In[14]:


values = [30, 25, 20,13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'ETC']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf','#9bf6ff', '#a0c4ff']
explode = [0.05] * 6

plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False, colors = colors, explode = explode)
plt.show() 


# ### 도넛모양 그래프
# + wedgeprops = {'width': }

# In[19]:


wedgeprops = {'width':0.8}
plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False, colors = colors,explode = explode, wedgeprops=wedgeprops)
plt.show()


# ### explode 문제점 개선
# explode 적용 시 그래프가 어긋나는 문제 개선
# + edgecolor
# +linewidth

# In[ ]:


wedgeprops = {'width':0.8, 'edgecolor':'w', 'linewidth':2}

plt.pie(values, labels = labels, autopct = '%.1f%%', startangle=90, counterclock=False, colors = colors, wedgeprops=wedgeprops)
plt.show()


# ### 10%미만 수치 없애기
# + custom_autopct 함수 정의

# In[28]:


def cumtom_autopct(pct):
    # return ('%.1f%%' % pct) if pct >=10 else ''
    # return '{:.1f}%'.format(pct) if pct >= 10 else ''
    return '{:.0f}%'.format(pct) if pct >= 10 else ''
    
plt.pie(values, labels = labels, autopct = cumtom_autopct, startangle=90, counterclock=False, colors = colors, wedgeprops=wedgeprops)
plt.show()


# ### 그래프 안 수치 위치이동
# + pctdistance = (0~1사이)

# In[29]:


plt.pie(values, labels = labels, autopct = cumtom_autopct, startangle=90, counterclock=False, colors = colors, wedgeprops=wedgeprops, pctdistance = 0.7)
plt.show()


# ### DataFram 활용

# In[30]:


import pandas as pd


# In[32]:


df = pd.read_excel('../Pandas/score.xlsx')
df


# In[33]:


# 학교별 학생 인원수 파악
grp = df.groupby('학교')
grp


# In[39]:


values = [grp.size()['북산고'], grp.size()['능남고']]
labels = ['북산고', '능남고']

plt.pie(values, labels=labels)
plt.title('소속 학교')
plt.show()

