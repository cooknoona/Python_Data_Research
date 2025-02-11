# 데이터 전처리 : 주어진 데이터를 분석에 적합하도록 가공하는 작업

import pandas as pd
import numpy as np

exam = pd.read_csv('exam.csv')

# query()를 사용해 행 제한
print(exam.query('nclass == 1'))

print(exam.query('math > 50'))  # 조건문 사용

# 1반 이면서 수학 점수가 50점 이상인 경우 출력
print(exam.query('nclass == 1 & math >= 50'))

# 수학 점수가 90 점 이상 or 영어 점수가 90점 이상
print(exam.query('math >= 90 | english >= 90'))

# 필요한 변수만 추출 하기 (열 제한)
print(exam['math'])

# 여러 열 출력
print(exam[['nclass', 'math', 'english']])

# 열 제거 하기
print(exam.drop(columns='math'))

# 행 제한(query()) 과 열 제한 ([]) 조합
print(exam.query('nclass == 2')[['english', 'math']])

# 일부만 출력 하기 : 수학 점수가 50점 이상인 행만 추출한 다음, id, math 앞부분 5행까지 추출
print(exam.query('math >= 50')[['id', 'math']].head(8))

# 연습 문제1 : 11개의 컬럼 중에서 category(자동차 종류), cty(도시 연비) 추출해 새로운 데이터 생성
mpg = pd.read_csv('mpg.csv')
new_mpg = mpg[['category', 'cty']]
print(new_mpg)

# 연습 문제2 : category(자동차 종류)가 'suv' 인 자동차 와 'compact' 인 자동차 중
# 어떤 자동차 의 cty (도시 연비) 평균이 더 높은 지
suv_cty = mpg.query('category == "suv"')['cty'].mean()
compact_cty = mpg.query('category == "compact"')['cty'].mean()
if suv_cty > compact_cty:
    print(f"SUV : {suv_cty}")
else:
    print(f"COMPACT : {compact_cty}")


# 정렬
print(exam.sort_values('math', ascending = False))    # 수학 성적 기준 오름 차순 DESC

# 여러 정렬 기준 적용
print(exam.sort_values(['nclass', 'math'], ascending = [True, False]))

# 파생 변수 추가 (원본 데이터를 변경 하지 않음)
exam.assign(total = exam['math'] + exam['english'] + exam['science'])
print(exam)

# 파생 변수 추가 (원본 데이터 변형)
exam['total'] = exam['math'] + exam['english'] + exam['science']
print(exam)

print(exam.assign(test = np.where(exam['science'] >= 60, 'pass', 'fail')))

# 체이닝 메서드 활용
print(exam.assign(total = exam['math'] + exam['english'] + exam['science']).sort_values('total', ascending = False))

# 합산 연비
new_add = mpg[['cty'] + ['hwy']]

average_mpg = new_add/2

new_add.sort_values('mean', ascending = False).head(3)

mpg.assign(total = lambda x: x['cty'] + x['hwy'], mean = lambda x: x['total'] /2) \
    .sort_values('mean', ascending=False) \
    .head(3)
