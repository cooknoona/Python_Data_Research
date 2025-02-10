# Numpy : 파이썬 에서 과학적 계산을 위한 핵심 라이브러리, 아나콘다를 사용하면 기본 포함
# - 다차원 배열 객체 제공, 고성능 수학 연산 지원

import numpy as np
data = [0, 1, 2, 3, 4, 5]   # 리스트, {} 딕셔너리, () 튜플

a1 = np.array(data) # 리스트를 numpy 배열로
print(a1)

# 정수와 실수가 혼합된 경우는 전부 실수로 변환
data2 = [0, 1, 2, 3.14, 4, 5.5, 6, 7, 8.99]
a2 = np.array(data2)
print(a2)

# 배열의 속성 확인
x = np.array([0.1, 0.2, 0.3])
print(x.shape)  # 배열의 형태
print(x.dtype)

y = np.array(([1, 2, 3], [4, 5, 6]))
print(y.shape)
print(y.dtype)

# 특정 범위의 배열 생성
a3 = np.arange(0, 10, 2)    # 0 ~ 10 미만, 증감값 2
print(a3)

a4 = np.arange(10)  # 0 ~ 10 미만, 증감값 1
print(a4)

# 2차원 배열 생성
a5 = np.arange(12).reshape(4, 3)
print(a5)
print(a5.shape)

# 주어진 범위를 3번째 값으로 일정한 간격으로 추가
a6 = np.linspace(1, 10)
print(a6)

# 특정한 숫자로 채워진 배열 생성
a7 = np.zeros(10)
print(a7)

a8 = np.zeros((3, 4))
print(a8)

a9 = np.ones(10)
print(a9)

a10 = np.ones((5, 5))
print(a10)

a11 = np.eye(5) # 5 x 5 단위 행렬
print(a11)

# 배열의 데이터 타입 변환
a12 = np.array(['1.5', '0.44', '3.14', '3.14599'])
print(a12)
print(a12.dtype)

num_a12 = a12.astype(float)
print(num_a12)

a13 = np.array(["1", "2", "3", "4", "5", "6", "7"])
num_a13 = a13.astype(int)
print(num_a13)

# 난수 배열의 생성
# rand() : 0 ~ 1 미만의 실수로 난수 배열을 생성
a14 = np.random.rand(2, 3)
print(a14)

a15 = (np.random.rand(6) * 45) + 1
print(a15.astype(int))

# 지정한 범위에 해당하는 정수로 난수 배열을 생성 : randint()
a16 = np.random.randint(10, size = (5, 10)) # 0 ~ 9 사이의 임의의 값을 사이즈 만큼 생성
print(a15)

# Numpy 사칙연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
# 통게 연산
arr3 = np.arange(10)
print(f"합계 : {arr3.sum()}, 평균 : {arr3.mean()}")
print(f"표준편차 : {arr3.std()}, 분산 : {arr3.var()}")
print(f"최솟값 : {arr3.min()}, 최댓값 : {arr3.max()}")

arr4 = np.array([9, 8, 7, 2, 3, 4, 6])
print(np.sort(arr4))  # 오름차순 정렬
print(np.argsort(arr4))  # 정렬된 인덱스 반환

arr5 = np.array([1,2,3,4,5])

#인덱싱
print(arr5[0])
print(arr5[2])
# 슬라이싱
print(arr5[1:4]) #[2,3,4]

# 1번 문제 : 1 부터 10까지의 숫자로 이루어진 1차원 배열을 생성하고, 모든 요소에 5를 더한 결과를 출력하세요.

test1 = np.arange(1, 11, 5)
print(f"5를 더한 1차원 배열: {test1}")

# 2번 문제 : 1부터 9 까지의 숫자를 사용해 3X3 크기의 2차원 배열을 생성하고 출력하세요.

test2 = np.arange(1, 10).reshape(3, 3)
print(f"2차원 배열: {test2}")

# 3번 문제 : 1부터 20 까지의 숫자로 이루어진 배열을 생성하고, 다음을 계산 하세요.
# 1. 배열의 합계
# 2. 배열의 평균
# 3. 배열의 최대값과 최소값

test3 = np.arange(1, 20)
print(f"합게 : {test3.sum()}")
print(f"평균 : {test3.mean()}")
print(f"최소 값 : {test3.min()}, 최대 값 : {test3.max()}")

# 4번 문제 : 0에서 100 사이의 난수를 10개 생성하고, 50 이상인 값을 출력

test4 = np.random.randint(1, 101, 10)
print(f"난수 값: {test4[test4 > 50]}")
print(f"난수 값의 갯수: {test4[test4 > 50].shape}")
