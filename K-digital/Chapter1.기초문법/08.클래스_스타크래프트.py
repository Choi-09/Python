#!/usr/bin/env python
# coding: utf-8

# In[60]:


# 일반 유닛
class Unit:
    def __init__(self,name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name}유닛이 생성되었습니다.")
        
    def move(self,location):
        print(f"{self.name}: {location}방향으로 이동합니다. [속도{self.speed}]")
        
    def damaged(self, damage):
        print(f"{self.name} 유닛이 {damage}데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <=0 :
            print(f"{self.name}유닛이 파괴되었습니다.")


# In[78]:


# 공격유닛
class AttackUnit(Unit): # 상속받을 부모클래스 적어주기! 
    def __init__(self,name,hp, speed, damage):
        Unit.__init__(self,name,hp, speed)  # Unit 클래스에서 상속 
        self.damage = damage
        
    def attack(self, location):
        print(f"{self.name}: {location} 방향으로 적군을 공격 합니다. [공격력: {self.damage}]")
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    
    # 스팀팩: 일정 시간동안 이동 및 공격 속도 증가, 자기 체력 10 감소 
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name}: 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name}: 체력이 부족하여 스팀팩을 사용하지 않습니다")

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능.
    seize_developed = False # 시즈모드 개발여부. 업그레이드하면 모든 탱크에 적용
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 시즈모드 설치 후
        # 현재 시즈모드 해제상태 -> 시즈모드 설정
        if self.seize_mode == False:
            print(f"{self.name}: 시즈 모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
            
        # 현재 시즈모드 일때 -> 해제
        else: 
            print(f"{self.name}: 시즈 모드를 해제합니다.")
            self.damage/=2
            self.seize_mode = False

            

# 날 수 있는 기능 클래스
class Flyable:
    def __init__(self, speed):
        self.speed = speed
    def fly(self, name, location):
        print(f"{name}: {location}방향으로 날아갑니다. [속도: {self.speed}]")

# 공중 공격유닛
class FlyableAttackUnit(AttackUnit, Flyable):  # 상속받을 부모 클래스
    def __init__(self,name,hp,damage, speed):
        AttackUnit.__init__(self,name,hp,0, damage)  # 멤머변수 초기화  # 지상스피드는 0으로 처리 
        Flyable.__init__(self,speed)
            
    def move(self, location):
        self.fly(self.name, location)
        
# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80,20,5)
        self.clocked = False # 클로킹모드 해제상태
    
    def clocking(self):
        if self.clocked == True:
            print(f"{self.name}: 클로킹 모드를 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name}: 클로킹 모드로 전환합니다.")
            self.clocked = True


# In[79]:


# 생동감 있는 게임을 위해서 추가
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")


# In[80]:


# 게임 진행
game_start()


# In[81]:


# 마린 3마리 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()


# In[82]:


# 탱크 2개 생성
t1 = Tank()
t2 = Tank()


# In[83]:


# 레이스 1기 생성
w1 = Wraith()


# In[84]:


# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


# In[85]:


# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")


# In[86]:


#  공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):     # unit들이 특정 클래스의 인스턴스라면 
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    else:
        unit.clocking()


# In[87]:


# 전군 공격
for unit in attack_units:
    unit.attack("1시")


# In[88]:


from random import *


# In[91]:


# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음(5~20)


# In[77]:


# 게임 종료
game_over()

