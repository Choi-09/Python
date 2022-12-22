#!/usr/bin/env python
# coding: utf-8

# # 3. 문자열 처리

# ### 1. 문자열

# In[1]:


sentence = "나는 소녀입니다."
print(sentence)


# In[2]:


sentence2 = "파이썬은 쉬워요"
print(sentence2)


# In[4]:


sentence3 = """
나는 소녀고,
파이썬은 쉬워요
"""

print(sentence3)


# ### 2. 슬라이싱

# In[9]:


jumin = "991230-1234567"


# In[10]:


print("성별:" , jumin[7])


# In[11]:


print("연:", jumin[0:2])


# In[12]:


print("월:", jumin[2:4])


# In[13]:


print("일:", jumin[4:6])


# In[14]:


print("생년월일:", jumin[:6])


# In[16]:


print("뒷자리:", jumin[7:])


# In[17]:


print("뒷자리(뒤에서부터 카운트): ", jumin[-7:])


# ### 3. 문자열 처리함수

# In[30]:


python = "Python is Amazing"


# In[19]:


python.lower()


# In[20]:


python.upper()


# In[21]:


python[0].isupper()


# In[22]:


python[-1].isupper()


# In[23]:


len(python)


# In[24]:


python.replace("Python", "Java")


# In[33]:


index = python.index("n")
index


# In[34]:


index = python.index("n", index + 1)
index


# In[39]:


print(python.find("Java"))  # 원하는 값이 없으면 -1반환. 뒷문장 실행 ok
print("hello")


# In[38]:


print(python.index('Java'))  # 원하는 값이 없으면 error. 뒷문장 실행 X
print("hello")


# In[40]:


print(python.count("n"))


# ### 4. 문자열 포맷

# In[42]:


print("a" + "b")


# In[43]:


print("a", "b")


# In[46]:


# 방법 1: %
print("나는 %d살 입니다." %20)  # d: 정수


# In[50]:


print("나는 %s을 좋아해요." % "파이썬") #s: 문자열


# In[51]:


print("Apple은 %c로 시작해요." % "A")  #c: charactor. 문자1개


# In[52]:


print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))


# In[53]:


# 방법 2: {}
print("나는 {}살 입니다.".format(20))


# In[54]:


print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))


# In[55]:


print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))


# In[56]:


print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


# In[57]:


# 방법3: {변수명}
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))


# In[58]:


# 방법4: f-string
age = 20
color = "빨간"
print(f"{age}살이며, {color}색을 좋아해요")


# ### 5. 탈출문자

# In[66]:


# \n : 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")


# In[67]:


# \"  \'
print("저는 '최정인' 입니다. ")


# In[63]:


print('저는 "최정인"입니다.')


# In[64]:


print("저는 \"최정인\" 입니다. ")


# In[65]:


print('저는 \'최정인\' 입니다.')


# In[71]:


# \\: 문장 내에서 \
print("C:\\Users\\user\\PythonDataWorkspace")


# In[72]:


# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine")


# In[74]:


# \b: 백스페이스(한 글자 삭제)
print("Redd\b Apple")


# In[75]:


# \t: 탭
print("Red\tApple")


# ### 6. 퀴즈
# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 
# + 예) http://naver.com
# + 규칙1: http:// 부분은 제외 => naver.com
# + 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# + 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# + 생성된 비밀번호: nav51!

# In[88]:


url = "http://naver.com"
pw = url[7:].split(".")[0]  # 규칙 1,2
pw = pw[:3] + str(len(pw)) + str(pw.count('e'))+ "!"  # 규칙3
pw

