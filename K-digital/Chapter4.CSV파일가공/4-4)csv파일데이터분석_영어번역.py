# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:39:54 2022

@author: user
"""

import usecsv, re

E = '''hina’s stockpile of nuclear warheads has surpassed 400 in a fraction of the time previously estimated by the United States, a major Pentagon report revealed, with Beijing focusing on accelerating its nuclear expansion as it seeks to challenge the US as the world’s top super power.

In 2020, the US estimated that China had nuclear warheads numbering in the low-200s and expected the stockpile to double within a decade. Just two years later, China has reached that mark and could have some 1,500 nuclear warheads by 2035 if they continue to expand their stockpile at the current pace, according to the 2022 China Military Power report released Tuesday.

“What we’ve seen really in the past couple of years is this accelerated expansion,” said a senior defense official.

The world’s most populous country is using its burgeoning military as one of its tools to create an international system that favors its world view, posing the “most consequential and systemic challenge to US national security,” according to the report, and the larger nuclear capability is a far cry from what China used to call a “lean and efficient” nuclear deterrent. Beijing’s investment in its nuclear triad – sea, land and air-based nuclear launch options – is cause for concern in Washington.

“We see, I think, a set of capabilities taking shape and new numbers in terms of what they’re looking to pursue that raise some questions about what their intent will be in the longer term,” the senior defense official said in a briefing to reporters about the latest report.

China also conducted 135 ballistic missile tests in 2021, the report said, which is more than the rest of the world combined. (The tally excludes ballistic missiles used in the war in Ukraine, the report noted.)

The official also offered new details about the Chinese test of a hypersonic missile in July 2021 that flew around the world before hitting its target, an accomplishment that drew attention to the lagging pace of US hypersonic weapons development. The official said the Chinese system flew 40,000 kilometers and demonstrated the longest flight of any Chinese land attack weapon to date.

The Chinese military, formally known as the People’s Liberation Army, is also developing space and counterspace weapons, the report said, viewing the advanced technology as a way to deter outside intervention in a regional military conflict.
'''

K = '''중국의 핵탄두 비축량이 이전에 미국이 추정한 것보다 훨씬 짧은 시간에 400개를 넘어섰다고 주요 국방부 보고서가 밝혔으며, 중국은 세계 최고의 초강대국인 미국에 도전하기 위해 핵 확장을 가속화하는 데 집중하고 있습니다.

2020년에 미국은 중국이 200대 초반의 핵탄두를 보유하고 있으며 10년 이내에 비축량이 두 배가 될 것으로 예상했습니다. 화요일에 발표된 2022년 중국 군사력 보고서에 따르면, 불과 2년 후 중국은 그 목표에 도달했으며 현재 속도로 비축량을 계속 확대할 경우 2035년까지 약 1,500개의 핵탄두를 보유할 수 있습니다.

고위 국방 관계자는 "지난 몇 년 동안 우리가 실제로 본 것은 이러한 가속화된 확장입니다."라고 말했습니다.

보고서에 따르면 세계에서 가장 인구가 많은 국가는 급증하는 군대를 세계관을 선호하는 국제 시스템을 만드는 도구 중 하나로 사용하고 있으며 "미국 국가 안보에 가장 결과적이고 체계적인 도전"을 제기하고 있으며 더 큰 핵 능력을 보유하고 있습니다. 중국이 "간소하고 효율적인" 핵 억지력이라고 부르던 것과는 거리가 멀다. 해상, 지상 및 공중 기반 핵 발사 옵션이라는 핵 3대 요소에 대한 베이징의 투자는 워싱턴에서 우려의 원인입니다.

고위 국방 관계자는 브리핑에서 "우리는 일련의 능력이 형성되고 있고 그들이 추구하고자 하는 것과 관련하여 새로운 수치를 보고 있으며 장기적으로 그들의 의도가 무엇인지에 대해 몇 가지 질문을 제기하고 있습니다. 최신 보고서에 대해 기자에게.

보고서는 중국이 2021년에 135건의 탄도미사일 시험을 실시했는데, 이는 전 세계를 합친 것보다 많다고 밝혔다. (이 집계는 우크라이나 전쟁에서 사용된 탄도 미사일을 제외했다고 보고서는 지적했다.)

이 관리는 또한 2021년 7월 중국이 목표물에 도달하기 전에 전 세계를 비행한 극초음속 미사일의 시험에 대한 새로운 세부 정보를 제공하여 미국 극초음속 무기 개발의 뒤처진 속도에 주목했습니다. 관계자는 중국 시스템이 40,000km를 비행했으며 지금까지 중국의 지상 공격 무기 중 가장 긴 비행을 시연했다고 말했습니다.

공식적으로 인민해방군으로 알려진 중국군도 우주 및 대우주 무기를 개발하고 있으며 첨단 기술을 지역 군사 분쟁에 대한 외부 개입을 억제하는 방법으로 보고 있다고 보고서는 말했습니다.
'''

#E = re.sub(r"[[:punct:]]","",E) # punctuation: 문장기호들을 다 찾는다, "": 없애준다.
#모든 기호면 .,도 포함해서 없어지므로 다른 정규표현식 필요
E = re.sub(r"[\n]","", E)   # \n 삭제
Elist = re.split(r'\.', E) #\. : 문자 .   : Elist는 E를 .으로 나눈 원소들을 갖는다.

K = re.sub(r"[\n]","", K)
Klist = re.split(r'\.', K)

total = []

for i in range(len(Elist)): # Elist의 길이만큼 돌면서(E와 K의 길이가 같다는 전제 하에.)
    total.append([Elist[i],"|",Klist[i]])   # Elist | Klist 의 형태로 두 데이터를 붙인다.
    
usecsv.writecsv("E_KTranslate.csv", total)  #붙인 데이터를 total에 쓰고, "E_KTranslate" 이라는 csv파일로 만든다.
        
