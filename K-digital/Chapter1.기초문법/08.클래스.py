#!/usr/bin/env python
# coding: utf-8

# # 8. 클래스

# In[3]:


# 마린 : 공격 유닛. 군인, 총을 쏠 수 있음
name = "마린"  #유닛 이름
hp=40  # 유닛 체력
damage = 5 # 유닛의 공격력
print(f"{name}유닛이 생성되었습니다.")
print(f"체력{hp}, 공격력{damage}\n")


# In[4]:


# 탱크: 공격 유닛. 탱그, 포를 쏠 수 있는데 일반모드 / 시즈모드가 있다.
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print(f"{tank_name}유닛이 생성되었습니다.")
print(f"체력{tank_hp}, 공격력{tank_damage}\n")


# In[5]:


def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력{damage}]")
    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)


# In[9]:


# 탱크 추가 
tank_name2 = '탱크2'
tank_hp2 = 150
tank_damage2 = 35

print(f"{tank_name2}유닛이 생성되었습니다.")
print(f"체력{tank_hp2}, 공격력{tank_damage2}\n")

## 계속 추가하기 힘들어요..! 


# ### 클래스 작성
# + class 이름: 
#          def __init__(self, val1, val2, val3,...):

# In[63]:


# 일반 유닛
class Unit:
    def __init__(self,name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name}유닛이 생성되었습니다.")
        
    def move(self,location):
        print("[지상유닛 이동]")
        print(f"{self.name}: {location}방향으로 이동합니다. [속도{self.speed}]")
        
marine1 = Unit("마린", 40,5)
marine2 = Unit("마린", 40,5)
tank1 = Unit("탱크", 40,4)


# ### init 함수
# + __ __ : 생성자 
# + 객체: class(설계도)로부터 만들어지는 것(제품) ex) marine1, tank1 등 
# + 호출시 self를 제외한 인자 수와 같은 수를 던져줘야한다. 

# ### 멤버변수
# + 클래스 내에서 정의된 변수
# + self.

# In[66]:


# 레이스: 공중유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80,5)
print(f"유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}")  # 레이스 멤버변수를 불러 쓴다. 


# In[67]:


# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80,5)
wraith2.clocking = True  # 외부에서 clocking 이라는 변수를 할당함. wraith2에만 적용. 
if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")


# ### 메소드
# + attack, damaged 함수로 메소드 만들기

# In[68]:


# 공격 유닛
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print(f"{self.name}: {location} 방향으로 적군을 공격 합니다. [공격력: {self.damage}]")
    def damaged(self, damage):
        print(f"{self.name} 유닛이 {damage}데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <=0 :
            print(f"{self.name}유닛이 파괴되었습니다.")

# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)


# ### 상속
# + Unit 클래스와 AttackUnit 클래스에 공통되는 부분이 있는데, Unit의 상속을 받아서 AttackUnit에서 쓴다.

# In[77]:


class AttackUnit(Unit): # 상속받을 부모클래스 적어주기! 
    def __init__(self,name,hp, speed, damage):
        Unit.__init__(self,name,hp, speed)  # Unit 클래스에서 상속 
        self.damage = damage
        
    def attack(self, location):
        print(f"{self.name}: {location} 방향으로 적군을 공격 합니다. [공격력: {self.damage}]")
        
    def damaged(self, damage):
        print(f"{self.name} 유닛이 {damage}데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <=0 :
            print(f"{self.name}유닛이 파괴되었습니다.")
            
# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16,5)
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)


# ### 다중상속
# + 부모클래스가 여러개

# In[102]:


# 드랍쉽: 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격불가

# 날 수 있는 기능 클래스
class Flyable:
    def __init__(self, speed):
        self.speed = speed
    def fly(self, name, location):
        print(f"{name}: {location}방향으로 날아갑니다. [속도: {self.speed}]")

        
# 공중 공격 유닛 클래스        
class FlyableAttackUnit(AttackUnit, Flyable):  # 상속받을 부모 클래스
    def __init__(self,name,hp,damage, speed):
        AttackUnit.__init__(self,name,hp,0, damage)  # 멤머변수 초기화  # 지상스피드는 0으로 처리 
        Flyable.__init__(self,speed)

# 발키리: 공중 공격 유닛, 한 번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "3시")


# ### 메소드 오버라이딩
# + 부모클래스의 메소드 말고 자식클래스의 메소드를 사용하고 싶을 때 새롭게 메소드를 정의해서 사용할 수 있는데, 이것을 오버로딩이라고 한다.

# In[99]:


# 벌쳐: 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

# 배틀크루저: 공중유닛, 체력도 굉장히 좋고, 공격력도 좋음.
cruiser = FlyableAttackUnit("배틀크루저", 500,25,3)

vulture.move("11시")
cruiser.fly(cruiser.name,"9시")


# In[104]:


# 지상유닛 move와 공중유닛 fly 함수를 구분해서 써야하는데 굉장히 번거롭기 때문에 오버라이딩.
# 공중 공격 유닛 클래스 재정의    
class FlyableAttackUnit(AttackUnit, Flyable):  # 상속받을 부모 클래스
    def __init__(self,name,hp,damage, speed):
        AttackUnit.__init__(self,name,hp,0, damage)  # 멤머변수 초기화  # 지상스피드는 0으로 처리 
        Flyable.__init__(self,speed)
            
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
cruiser = FlyableAttackUnit("배틀크루저", 500,25,3)
cruiser.move("9시")


# ### pass
# + 코드안적어도 일단 오류안내고 패스 

# In[105]:


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
    
# 서플라이 디폿 : 건물, 1개 건물 = 8유닛 생성가능. 
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# In[108]:


# # 다른 예
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")
# def game_over():
#     pass

# game_start()
# game_over()


# ### super
# + self 는 가져오지 않는다.
# + 다중상속에서는 첫번째 호출되는 함수만 받을 수 있기 때문에 사용하지 않는다.

# In[ ]:


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)  # super로도 부모클래스 상속받을 수 있는데, super를 쓸 때는 self 가져오지 않는다. 
        self.location = location


# ### 퀴즈
# 
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# 
# (출력예제) <br/>
# 총 3대의 매물이 있습니다. <br/>
# 강남 아파트 매매 10억 2010년<br/>
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# In[2]:


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
house3 = House('송파', '빌라', '월세', '500/50', '2000년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"총 {len(houses)}대의 매물이 있습니다.")
for house in houses:
    house.show_detail()

