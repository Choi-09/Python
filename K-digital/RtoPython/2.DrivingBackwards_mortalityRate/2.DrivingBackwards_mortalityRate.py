#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np


# In[15]:


# 사용가능한 시스템의 TTF 폰트 목록
import matplotlib.font_manager as font_manager
font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

print('사용가능한 TTF 폰트 개수:', len(font_list))

for f in font_list :
    if 'Na' in f :
        print(f)


# In[ ]:


#폰트 연결

# from matplotlib import font_manager, rc
# font_path = 'C:\\Users\\minnote\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumGothic.ttf'
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)


# In[62]:


df = pd.read_excel("C:/RWork/실습/02/02_역주행사고.xlsx")
df


# In[70]:


df1 = df[df['구분']=='전체']
df1


# In[57]:


df2 = df[df['구분']=='역주행']
df2


# In[65]:


import copy


# In[78]:


df3 = df1.copy()
df3


# In[87]:


df3['구분'] = '일반'
df3


# In[80]:


# loc 
df3.loc[:,"사고":"사망"] = np.array(df1.loc[:, "사고":"사망"]) - np.array(df2.loc[:, "사고":"사망"])
df3


# In[81]:


# iloc
df3.iloc[:,2:] = np.array(df1.iloc[:,2:]) - np.array(df2.iloc[:,2:])


# In[82]:


# 데이터프레임 인덱스
# 1. 행인덱스
df.index
list(df.index)


# In[83]:


# 2. 열인덱스
df.columns
list(df.columns)


# ### 치명률 구하기

# In[84]:


df1['치명률'] = round((df1['사망'] / df1['사고']*100),2)
df1


# In[97]:


df2['치명률'] = round((df2['사망'] / df2['사고']*100),2)
df2


# In[86]:


df3['치명률'] = round((df3['사망'] / df3['사고']*100),2)
df3


# In[89]:


df3.iloc[:, 2:]
df3.loc[:, ["사고", '년도']]


# In[93]:


import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'


# In[94]:


df2.loc[:, ["사고"]].plot()
df3.loc[:, ["사고"]].plot()
plt.show()


# In[95]:


y2 = list(df2['치명률'])
y3 = list(df3['치명률'])
x = list(df2['년도'])


# In[96]:


plt.plot(x, y2, 'rx-', label="역주행")
plt.plot(x, y3, 'bo--', label="일반")
plt.title("교통사고 치명률")
plt.legend()
plt.show()


# In[ ]:




