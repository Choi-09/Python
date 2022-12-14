#!/usr/bin/env python
# coding: utf-8

# # 1. 인구 피라미드

# In[ ]:


import pandas as pd


# ## 2012년도 남자데이터 불러오기

# ### 파일 불러오기
# + 처음부터 파일에서 필요한 부분만 불러오기

# In[40]:


file_name = '201211_201211_연령별인구현황_월간.xlsx'
df_m = pd.read_excel(file_name, skiprows=3, index_col = '행정기관', usecols='B,E:Y')
df_m.head(3)


# ### 남자데이터 첫번째 행을 숫자형으로 변환시키기

# In[16]:


df_m.iloc[0] = df_m.iloc[0].str.replace(",","").astype(int)


# In[17]:


df_m


# ## 2012년도 여자 데이터 불러오기

# In[25]:


df_f = pd.read_excel("201211_201211_연령별인구현황_월간.xlsx", skiprows=3, index_col = '행정기관', usecols='B,AB:AV')
df_f


# ### 여자데이터 컬럼명 통일시키기

# In[27]:


df_f.columns = df_m.columns
df_f


# ### 여자데이터 첫번째 행을 숫자형으로 변환시키기

# In[26]:


df_f.iloc[0] = df_f.iloc[0].str.replace(",","").astype(int)
df_f


# ### 데이터 시각화

# In[29]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[35]:


plt.figure(figsize = (10,7))
plt.barh(df_m.columns, df_m.iloc[0]//1000)   # 데이터 단위를 1,000명
plt.barh(df_f.columns, df_f.iloc[0]//1000)


# ### 남,여 대칭 그래프 만들기

# In[36]:


plt.figure(figsize = (10,7))
plt.barh(df_m.columns, -df_m.iloc[0]//1000)   # 데이터 단위를 1,000명
plt.barh(df_f.columns, df_f.iloc[0]//1000)


# ### 그래프 꾸미기

# In[39]:


plt.figure(figsize = (10,7))
plt.barh(df_m.columns, -df_m.iloc[0]//1000)   # 데이터 단위를 1,000명
plt.barh(df_f.columns, df_f.iloc[0]//1000)
plt.title('2012년도 11월 인구 피라미드')
plt.savefig('2012.11月인구피라미드.png')
plt.show()


# ## 2022년도 남자 데이터 불러오기

# In[45]:


file_name = '202211_202211_연령별인구현황_월간.xlsx'
df_m2 = pd.read_excel(file_name, skiprows=3, index_col = '행정기관', usecols='B,E:Y')
df_m2.head(3)


# ### 2022년도 남자데이터 첫번째 행 숫자형으로 변환

# In[47]:


df_m2.iloc[0] = df_m2.iloc[0].str.replace(",","").astype(int)
df_m2


# ## 2022년도 여자데이터 불러오기

# In[48]:


file_name = '202211_202211_연령별인구현황_월간.xlsx'
df_f2 = pd.read_excel(file_name, skiprows=3, index_col = '행정기관', usecols='B,AB:AV')
df_f2.head(3)


# ### 여자 데이터 컬럼명 바꾸기

# In[49]:


df_f2.columns = df_m2.columns
df_f2


# ### 여자 데이터 첫 번째 행 데이터를 숫자형으로 바꾸기

# In[51]:


df_f2.iloc[0] = df_f2.iloc[0].str.replace(",","").astype(int)
df_f2.iloc[0]


# In[54]:


plt.figure(figsize = (10,7))
plt.barh(df_m2.columns, -df_m2.iloc[0]//1000)   # 데이터 단위를 1,000명
plt.barh(df_f2.columns, df_f2.iloc[0]//1000)
plt.title('2022년도 11월 인구 피라미드')
plt.savefig('2022.11月인구피라미드.png')
plt.show()

