#!/usr/bin/env python
# coding: utf-8

# # 1. 자료형

# ### 1. 숫자 자료형

# In[1]:


print(5)


# In[2]:


print(-10)


# In[3]:


print(3.14)


# In[4]:


print(1000)


# In[5]:


print(5+3)


# In[6]:


print(5*3)


# In[7]:


print(3*(3+1))


# ### 2. 문자 자료형

# In[10]:


print('문자형 자료는 작은따옴표로 감싼다')


# In[9]:


print("큰따옴표도 가능")


# In[11]:


print("ㅎ"*9)


# ### 3. boolean 자료형
# 참 / 거짓

# In[12]:


print(5>10)


# In[13]:


print(5<10)


# In[14]:


print(True)


# In[15]:


print(False)


# In[16]:


print(not True)


# In[17]:


print(not False)


# In[18]:


print(not (5>10))


# ### 4. 변수

# In[28]:


# 애완동물을 소개해 주세요~
animal = "강아지"
name = '칠칠이'
age = 12
hobby = "산책"
is_senior = age >= 7


# In[30]:


print("우리집" + animal + "의 이름은" + name +"입니다")
print(name + "는" + str(age) +"살이며, 다리가 불편합니다")    # 정수형 데이터는 str()함수를 사용하여 문자형으로 바꿔준다.
print(name +"는 아주 아주 순하고 착한 강아지 입니다.")
print("날이 따뜻해지면 칠칠이"+ hobby +"을 자주시킬거에요")  
# print(name + "는 할머니 일까요?" + str(is_senior))  # boolean형 데이터는 str()함수를 사용하여 문자형으로 바꿔준다.
print(name, "는 할머니 일까요?" ,is_senior)  # ,가 들어가면 str으로 변환 할 필요없이 바로 변수 사용가능


# ### 5. 주석

# In[37]:


한_문장_주석 = "#"


# In[ ]:


여러_문장_주석 = " ''' "


# ### 6. 퀴즈
# 변수를 이용하여 다음 문장을 출력하시오

# In[43]:


station1 = "사당"
station2 = "신도림"
station3 = "인천공항"


# In[49]:


print(station1 +"행 열차가 들어오고 있습니다.")
print(station2 +"행 열차가 들어오고 있습니다.")
print(station3+"행 열차가 들어오고 있습니다.")

