import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpg = pd.read_csv('mpg.csv')
exam = pd.read_csv('./exam.csv')

print(exam.head())  # 기본적으로 앞부분 5행 출력
print(exam.tail(3)) # 데이터의 마지막 3행 출력
print(exam.shape)   # 데이터 프레임의 크기를 출력
print(exam.info())  # 변수의 속성을 출력, 결측치도 확인 가능
print(exam.describe())  # 요약 통계 정보출력

# 변수 이름 변경
mgr_new = mpg.copy()
mgr_new = mgr_new.rename(columns={'cty': 'city'})
mgr_new = mgr_new.rename(columns={'hwy': 'highway'})
print(mgr_new.head())

# 파생 변수 만들기
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
print(mpg.head())

# 조건문을 활용한 파생변수 생성
mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
count_test = mpg['test'].value_counts()
print(count_test)
count_test.plot.bar()
plt.show()

# 중첩 조건문을 활용한 연비 등급 부여
mpg['grade'] = np.where(mpg['total'] >= 30, 'A', np.where(mpg['total'] >= 20, 'B', 'C'))
count_grade = mpg['grade'].value_counts().sort_index()
count_grade.plot.bar(rot = 0)
plt.show()