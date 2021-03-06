
### 의약품별 질병 간 상관분석 ###

import pandas as pd

# '428901ATB'
print('\n', "[TOP1] '428901ATB'와 관련질병 간의 상관분석")
# '428901ATB'와 '발목을 포함한 아래다리의 골절'
print("'428901ATB'와 '발목을 포함한 아래다리의 골절'")
lst =[[62242, 70687, 84741, 86010, 86524, 86566, 81517, 81256+40237],
      [209268, 220137, 220465, 244468, 238839, 241165, 246036, 253083]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr)

# '428901ATB'와 '급성 기관지염'
print("'428901ATB'와 '급성 기관지염'")
lst =[[62242, 70687, 84741, 86010, 86524, 86566, 81517, 81256+40237],
      [12252290, 13119352, 14306530, 14932206, 15170159, 15084909,
       15896661, 16293934]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '428901ATB'와 '만성 기관지염'
print("'428901ATB'와 '만성 기관지염'")
lst =[[62242, 70687, 84741, 86010, 86524, 86566, 81517, 81256+40237],
      [376103, 384904, 417476, 373778, 378288, 371427, 387661, 421147]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '428901ATB'와 '천식'
print("'428901ATB'와 '천식'")
lst =[[62242, 70687, 84741, 86010, 86524, 86566, 81517, 81256+40237],
      [2221218, 2224166, 2095986, 1872656, 1730686, 1629665, 1631587, 1497417]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '428901ATB'와 '천식 지속상태'
print("'428901ATB'와 '천식 지속상태'")
lst =[[62242, 70687, 84741, 86010, 86524, 86566, 81517, 81256+40237],
      [52573, 66509, 109524, 118616, 112264, 105113, 66946, 48833]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '428901ATB'와 '의학적으로 확인되지 않은 호흡기결핵'
print("'428901ATB'와 '의학적으로 확인되지 않은 호흡기결핵'(2010-2015)")
lst =[[62242, 70687, 84741, 86010, 86524, 86566],
      [62230, 57319, 55124, 51915, 48191, 45716]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '428901ATB'와 '의학적으로 확인된 호흡기결핵'
print("'428901ATB'와 '의학적으로 확인된 호흡기결핵'(2010-2015)")
lst =[[62242, 70687, 84741, 86010, 86524, 86566],
      [55412, 53770, 54669, 52657, 49553, 46898]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'
print('\n', "[TOP2] '220902ATB'와 관련질병 간의 상관분석")
# '220902ATB'와 '감기'
print("'220902ATB'와 '감기'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [5025136, 4835957, 5095481, 5067950, 4918726, 4698713, 4595608, 4525661]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'와 '만성 부비동염'
print("'220902ATB'와 '만성 부비동염'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [1970019, 2018695, 2115655, 2123180, 2141145,
       2121735, 2207931, 2224629]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'와 '급성 부비동염'
print("'220902ATB'와 '급성 부비동염'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [4327992, 4063857, 4134305, 4159578, 4016005, 4007711, 4168561, 4116088]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'와 '상기도의 기타질환'
print("'220902ATB'와 '상기도의 기타질환'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [380363, 424935, 444896, 448824, 469745, 447441, 439766, 451570]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'와 '급성 상기도감염'
print("'220902ATB'와 '급성 상기도감염'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [7014043, 6677425, 6840598, 6603249, 6585501, 6277081, 6152058, 5976475]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '220902ATB'와 '알러지성 비염'
print("'220902ATB'와 '알러지성 비염'")
lst =[[40117, 39934, 42563, 51464, 54299, 50686, 51283, 52940+25239],
      [5569432, 5557107, 5984984, 6091834, 6301156, 6237961, 6682306,
       6841314]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'
print('\n', "[TOP3] '186101ATB'와 관련질병 간의 상관분석")
# '186101ATB'와 '양성 류마티스 관절염'
print("'186101ATB'와 '양성 류마티스 관절염'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [75642, 80862, 87799, 93359, 98330, 104724, 109123, 113419]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 '기타 류마티스 관절염'
print("'186101ATB'와 '기타 류마티스 관절염'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [227607, 225419, 214412, 198439, 184226, 172030, 160903, 147487]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (퇴행성 관절염)기타 관절염
print("'186101ATB'와 '(퇴행성 관절염)기타 관절염'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [1060604, 1067716, 1095776, 1083168, 1081663, 1059957, 1080615,
       1085882]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (전립선암) 전립선증식증
print("'186101ATB'와 '(전립선암) 전립선증식증'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [787803, 842069, 917599, 989478, 1040086, 1073147, 1152399,
       1213324]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (전립선암) 전립선의 악성 신생물
print("'186101ATB'와 '(전립선암) 전립선의 악성 신생물'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [43678, 50390, 56798, 63127, 67934, 72054, 81701, 89843]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (오십견) 어깨병변
print("'186101ATB'와 '(오십견) 어깨병변'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [1642494, 1791644, 1916479, 1978070, 2041201, 2094985, 2190208,
       2271751]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (오십견) 어깨 및 위팔의 골절
print("'186101ATB'와 '(오십견) 어깨 및 위팔의 골절'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [114016, 117041, 121420, 128160, 131673, 134060,
       134776, 136452]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (오십견) 어깨 및 위팔 부위의 근육 및 힘줄의 손실
print("'186101ATB'와 '(오십견) 어깨 및 위팔 부위의 근육 및 힘줄의 손실'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [117208, 135922, 155348, 172945, 176709, 181801, 187569, 190171]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '186101ATB'와 (폐암) 기관지 및 폐의 악성 신생물
print("'186101ATB'와 '(폐암) 기관지 및 폐의 악성 신생물'")
lst =[[39458, 39303, 41805, 45874, 48165, 50709, 51603, 53381+26066],
      [81723, 86124, 94831, 100580, 102568, 105990, 114808, 120079]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '421001ATB'
print('\n', "[TOP4] '421001ATB'와 관련질병 간의 상관분석")
# '421001ATB'와 '구역 및 구토'
print("'421001ATB'와 '구역 및 구토'")
lst =[[6601, 25296, 38716, 40532, 42409, 43600, 45055, 45479+22773],
      [357640, 357096, 404948, 414297, 420288, 595762, 654669, 633645]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '421001ATB'와 '기능성 소화불량'
print("'421001ATB'와 '기능성 소화불량'")
lst =[[6601, 25296, 38716, 40532, 42409, 43600, 45055, 45479+22773],
      [611654, 637203, 673649, 664637, 621705, 630072, 603623, 612385]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '222901ATB'
print('\n', "[TOP5] '222901ATB'와 관련질병 간의 상관분석")
# '222901ATB'와 '위궤양'
print("'222901ATB'와 '위궤양'")
lst =[[25421, 139437, 36103, 37181, 42517, 40850, 45194, 47727+23927],
      [1388929, 1353374, 1279644, 1183751, 1102193, 1044235, 1020855,
       954402]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '222901ATB'와 '위염 및 십이지장염'
print("'222901ATB'와 '위염 및 십이지장염'")
lst =[[25421, 139437, 36103, 37181, 42517, 40850, 45194, 47727+23927],
      [5443938, 5571478, 5796726, 5642399, 5375714, 5584384, 5393505,
       5306707]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '268000ATB'
print('\n', "[TOP6] '268000ATB'와 관련질병 간의 상관분석")
# ''268000ATB'와 '(기침, 가래) 감기'
print("'268000ATB'와 '(기침, 가래) 감기'")
lst =[[36920, 36370, 39736, 38427, 41247, 33730, 35345, 35780+16371],
      [5025136, 4835957, 5095481, 5067950, 4918726,
       4698713, 4595608, 4525661]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'
print('\n', "[TOP7] '101804ACH'와 관련질병 간의 상관분석")
# '101804ACH'와 '급성 기관지염'
print("'101804ACH'와 '급성 기관지염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [12252290, 13119352, 14306530, 14932206, 15170159, 15084909, 15896661, 16293934]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '상세불명의 만성 기관지염'
print("'101804ACH'와 '상세불명의 만성 기관지염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [376106, 384904, 417476, 373778, 378288, 371427, 387661, 421147]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '단순성 및 점액화농성 만성 기관지염'
print("'101804ACH'와 '단순성 및 점액화농성 만성 기관지염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [555443, 567394, 580648, 508158, 502437, 464527, 448463, 436360]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '급성인지 만성인지 명시되지 않은 기관지염'
print("'101804ACH'와 '급성인지 만성인지 명시되지 않은 기관지염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [1726675, 1873035, 2264090, 2155665, 2322925, 2363825, 2487776, 2537636]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '급성 후두염 및 기관염'
print("'101804ACH'와 '급성 후두염 및 기관염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [3573202, 3442803, 3510619, 3896099, 3360783, 3186320, 3339400, 3377432]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '급성 폐색성 후두염 및 후두개염'
print("'101804ACH'와 '급성 폐색성 후두염 및 후두개염'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [149405, 127415, 151834, 144862, 136906, 129864, 141005, 134568]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '101804ACH'와 '‘간’의 섬유증 및 경변증'
print("'101804ACH'와 '‘간’의 섬유증 및 경변증'")
lst =[[35940, 37201, 40063, 42328, 45956, 40706, 29890, 28002+13918],
      [76921, 79635, 84726, 87565, 85097, 87123, 90883, 90088]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# ''133301ATB''
print('\n', "[TOP8] '133301ATB'와 관련질병 간의 상관분석")
# '133301ATB'와 '위궤양'
print("'133301ATB'와 '위궤양'")
lst =[[36219, 35475, 36917, 36053, 35151, 30940, 24374, 22377+11570],
      [1388929, 1353374, 1279644, 1183751, 1102193,
       1044235, 1020855, 954402]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '133301ATB'와 '십이지장궤양'
print("'133301ATB'와 '십이지장궤양'")
lst =[[36219, 35475, 36917, 36053, 35151, 30940, 24374, 22377+11570],
      [331204, 327722, 327478, 311474, 299523, 283583, 286477, 286543]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '133301ATB'와 '위-식도 역류병'
print("'133301ATB'와 '위-식도 역류병'")
lst =[[36219, 35475, 36917, 36053, 35151, 30940, 24374, 22377+11570],
      [2847763, 3107033, 3378715, 3533638, 3635931, 3873549, 4179510, 4287987]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '133301ATB'와 '위염'
print("'133301ATB'와 '위염'")
lst =[[36219, 35475, 36917, 36053, 35151, 30940, 24374, 22377+11570],
      [5443938, 5571478, 5796726, 5642399, 5375714, 5584384, 5393505,
       5306707]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '271800ATB'
print('\n', "[TOP9] '271800ATB'와 관련질병 간의 상관분석")
# '271800ATB'와 '위궤양'
print("'271800ATB'와 '위궤양'")
lst =[[5829, 7190, 13719, 15174, 17232, 27795, 33590, 37009+18422],
      [1388929, 1353374, 1279644, 1183751, 1102193, 1044235, 1020855, 954402]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '271800ATB'와 '십이지장궤양'
print("'271800ATB'와 '십이지장궤양'")
lst =[[5829, 7190, 13719, 15174, 17232, 27795, 33590, 37009+18422],
      [331204, 327722, 327478, 311474, 299523, 283583, 286477, 286543]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')

# '271800ATB'와 '위-식도 역류병'
print("'271800ATB'와 '위-식도 역류병'")
lst =[[5829, 7190, 13719, 15174, 17232, 27795, 33590, 37009+18422],
      [2847763, 3107033, 3378715, 3533638, 3635931, 3873549,
       4179510, 4287987]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr, '\n')