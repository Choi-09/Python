#!/usr/bin/env python
# coding: utf-8

# # 9. 예외처리
# 어떤 오류가 발생했을 때 처리해주는 것

# ### 예외처리

# In[13]:


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요:")))
    nums.append(int(input("두 번째 숫자를 입력하세요:")))
    # nums.append(int(nums[0] / nums[1]))
    
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다. ")
    
except ZeroDivisionError as err:
    print(err)
    
except Exception as err: 
    print("알 수 없는 오류가 발생했습니다.")
    print(err)


# ### 에러 발생시키기

# In[14]:


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요"))
    num2 = int(input("두 번째 숫자를 입력하세요"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print(f"{num1} / {num2} = {num1}/{num2}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")


# ### 사용자 정의 예외처리

# In[30]:


class BigNumberError(Exception):
    def __init__(self,message):
            self.message = message
            
    def __str__(self):
            return self.message      

try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값: {num1}, {num2}")
    print(f"{num1} / {num2} = {num1}/{num2}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요22")
    print(err)


# ### finally
# + 예외처리 중 정상처리 / 오류발생 관계없이 무조건 실행.
# + try문의 마지막에 쓸 수 있다.

# In[31]:


class BigNumberError(Exception):
    def __init__(self,message):
            self.message = message
            
    def __str__(self):
            return self.message      

try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값: {num1}, {num2}")
    print(f"{num1} / {num2} = {num1}/{num2}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요22")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


# ### 퀴즈
# 치킨집 자동주문시스템 제작. 시스템 코드 확인 후 적절한 예외처리 구문 넣기.
# 
# + 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리.
#         - 출력메시지: "잘못된 값을 입력하였습니다."
# + 조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#          치진 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         - 출력메시지: "재고가 소진되어 더 이상 주문을 받지 않습니다."

# In[43]:


class SoldOutError(Exception):
    pass
        
chicken = 10
waiting = 1
try:
    while(True):
        print(f"남은 치킨: {chicken}")
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print(f"[대기번호 {waiting}] {order}마리 주문이 완료되었습니다.")
            waiting +=1
            chicken -= order 
        if chicken == 0:
            raise SoldOutError
        
except ValueError:
    print("잘못된 값을 입력하였습니다. 1마리 이상 주문 가능")
except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

