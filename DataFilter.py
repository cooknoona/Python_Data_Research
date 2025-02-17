# 결측치(Missing Value) 란? 누락된 값 또는 비어 있는 값을 의미, 결측치 가 있으면 분석 결과가 왜곡 된다
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'sex' : ['M', 'F', np.nan, 'M', 'F'],
    'score' : [5, 4, 3, 4, np.nan]
})

print(df)
print(pd.isna(df)) # 결측치 확인 True / False
print(pd.isna(df).sum) # 결측치 합계 출력

# 결측치 제거 하기 (해당 열에 해당 하는 set 을 삭제)
print(df.dropna(subset=['score']))
print(df.dropna(subset=['score', 'sex']))

# 평균 값으로 결측치 대체
exam = pd.read_csv('exam.csv')

# 임의의 결측치 생성 (결측치 는 Nan 은 null 과 같기 때문에 해당 행에서 제외하고 나머지 값을 평균으로 계산)
exam.loc[[2, 7, 14], ['math']]  = np.nan    # 2, 7, 14번의 행의 math 컬럼 값에 NaN 할당
print(exam['math'].sum())

print(exam['math'].mean().round(0))
exam['math'] = exam['math'].fillna(exam['math'].mean().round(0))
print(exam['math'].sum())


df2 = pd.DataFrame({
    'sex' : [1, 2, 1, 3, 2, 1],
    'score' : [5, 4, 3, 4, 3, 6]
})

# 이상한 값을 결측치 (Missing Value) 로 변환
df2['sex'] = np.where((df2['sex'] > 2) | (df2['sex'] < 0), np.nan, df2['sex'])
df2['score'] = np.where((df2['score'] > 5) | (df2['score'] < 0), np.nan, df2['score'])
print(df2)