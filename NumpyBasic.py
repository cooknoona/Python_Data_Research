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