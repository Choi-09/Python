#!/usr/bin/env python
# coding: utf-8

# # 4. 스타일
# 라인, 마커, 포맷

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[3]:


x = [1,2,3]
y = [2,4,8]


# In[4]:


plt.plot(x,y)


# ## (1) 라인

# ### 라인 두께 설정

# In[6]:


plt.plot(x,y, linewidth = 5)


# ### 라인 스타일 설정
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

# In[20]:


# linestyle = ''
plt.plot(x,y, marker = 'o', linestyle = "None")


# In[21]:


plt.plot(x,y, marker = 'o', linestyle = ":")


# In[22]:


plt.plot(x,y, marker = 'o', linestyle = "--")


# In[25]:


plt.plot(x,y, marker = 'o', linestyle = "-.")


# ### 라인 색상
# https://matplotlib.org/stable/gallery/color/named_colors.html

# In[26]:


plt.plot(x,y, color = 'pink')


# In[28]:


plt.plot(x,y, color = '#FF0000')


# In[29]:


plt.plot(x,y, color = 'b')


# In[30]:


plt.plot(x,y, color = 'g')


# ## (2) 마커

# ### 마커 설정
# https://matplotlib.org/stable/api/markers_api.html

# In[16]:


# marker = ''
plt.plot(x,y, marker = 'o')


# In[19]:


# marker = ''
plt.plot(x,y, marker = 'v')


# ### 마커 사이즈 

# In[17]:


# markersize = 
plt.plot(x,y, marker = 'X', markersize =10)


# In[15]:


# markersize =
plt.plot(x,y, marker = 'v', markersize =10)


# ### 마커 색상

# In[13]:


# markeredgecolor = ""
plt.plot(x,y, marker = 'v', markersize =10, markeredgecolor = "red")


# In[14]:


# markerfacecolor = ""
plt.plot(x,y, marker = 'v', markersize =10, markeredgecolor = "red", markerfacecolor = "yellow")


# ## (3) 포맷

# In[31]:


plt.plot(x,y, 'ro--')  # color, marker, linestyle 순


# In[32]:


plt.plot(x,y,'bv:')


# In[33]:


plt.plot(x,y, 'go')


# ## (4) 축약어

# In[36]:


# mfc: markerfacecolor, ms: markersize, mec: markeredgecolor, ls: linestyle
plt.plot(x,y, marker = 'o', mfc = 'red', ms ='10', mec = 'blue', ls = ':')


# ## (5) 투명도

# In[35]:


plt.plot(x,y, marker = 'o', mfc = 'red', ms ='10', alpha = 0.3)


# ## (6) 그래프 크기

# In[38]:


plt.figure(figsize=(10,5))
plt.plot(x,y)


# In[39]:


plt.figure(figsize=(5,10))
plt.plot(x,y)


# In[55]:


# dpi : dots per inch. 크기, 해상도 증가/감소
plt.figure(figsize = (10,5), dpi = 200)
plt.plot(x,y)


# ## (7) 그래프 배경색

# In[45]:


plt.figure(facecolor = 'pink')
plt.plot(x,y)


# In[51]:


plt.figure(facecolor = '#a1c3ff')
plt.plot(x,y)

