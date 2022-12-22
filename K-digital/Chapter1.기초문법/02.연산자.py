#!/usr/bin/env python
# coding: utf-8

# # 02. 연산자

# ### 1. 연산자

# In[1]:


# 더하기
print(1+1)


# In[2]:


# 빼기
print(3-2)


# In[3]:


# 곱하기
print(5*2)


# In[4]:


# 나누기
print(6/3)


# In[5]:


# 제곱
print(2**3) 


# In[6]:


#나머지
print(5%3)   


# In[7]:


# 몫
print(5//2)  


# In[8]:


# 논리형 연산
print(10>3)


# In[9]:


# 논리형 연산
print(4>=7)


# In[10]:


# 논리형 연산
print(5 <= 8)


# In[11]:


# 비교 연산
print(3==3)


# In[12]:


print(4==2)


# In[13]:


print(3+4 ==7)


# In[14]:


print(1!=3)


# In[15]:


print(not(1 != 3))


# In[16]:


print((3>0) and (3<5))


# In[17]:


print((3>9) & (4>1))


# In[18]:


print((3>9) | (4>1))


# In[19]:


print(5>4>3)


# In[20]:


print(5>4>7)


# In[21]:


print(3<5>1)


# ### 2. 간단한 수식

# In[22]:


print(2+3*4)


# In[23]:


print((2+3)*4)


# In[24]:


number = 2+3*4
number


# In[25]:


number = number + 2
number


# In[26]:


number +=2
number


# In[27]:


number *=2
number


# In[28]:


number /=2
number


# In[29]:


number -=2
number


# In[30]:


number %=5
number


# ### 3. 숫자처리함수

# In[31]:


print(abs(-5))


# In[32]:


print(pow(4,2))


# In[33]:


print(max(16,3))


# In[34]:


print(min(5,12))


# In[35]:


print(round(3.14))


# In[36]:


print(round(4.99))


# In[37]:


from math import *


# In[38]:


print(floor(4.99))


# In[39]:


print(ceil(4.01))


# In[41]:


print(sqrt(16))


# ### 4. 랜덤함수

# In[42]:


from random import *


# In[48]:


print(random())  # 0.0 이상 1.0 미만의 임의의 값을 생성


# In[56]:


print(random()*10)  # 0.0 이상 10.0 미만의 임의의 값을 생성


# In[58]:


print(int(random()*10) )  # 0.0 이상 10.0 미만의 임의 정수를 생성


# In[67]:


print(int(random()*10+1))     # 1 이상 10.0 이하의 임의 정수를 생성


# In[68]:


print(int(random()*45+1))    # 1이상 45 이하의 임의의 정수 생성


# In[78]:


print(randrange(1,46))  # 1이상 45 이하의 임의의 정수 생성


# In[80]:


print(randint(1,45))   # 1이상 45 이하의 임의의 정수 생성


# ### 5. 퀴즈
# 스터디 모임 가입. <br/>
# 월 4회 스터디를 하는데 3번은 온라인이고 1번은오프라인으로 진행.<br/>
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램 작성. <br/>
# 
# + 조건1: 랜덤으로 날짜 선정
# + 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# + 조건3: 매월 1~3일은 스터디 준비를 위해 제외
# 
# + 출력문: 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
# 

# In[82]:


d = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월", d, "일로 선정되었습니다.")

