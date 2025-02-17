import matplotlib.pyplot as plt # 데이터 시각화 에서 가장 많이 사용 하는 라이브러리에서 pyplot 모듈 import
from docutils.nodes import label

# plt.plot([10, 20, 30, 40, 50, 60, 70], [12, 43, 25, 15, 10, 50, 70])  # X 축, Y 축 데이터
# plt.show()


# 그래프 옵션 추가
# plt.rc('font', family='Malgun Gothic')
# plt.title("제목 추가")
# plt.plot([10, 20, 30, 40], [12, 43, 25, 15])
# plt.show()

# 범례 추가
plt.rc('font', family='Malgun Gothic')
plt.title("제목 추가")
plt.plot([10, 20, 30, 40], label = "1번", color="skyblue")
plt.plot([12, 43, 25, 15], label = "2번", color="red")
plt.legend()
plt.show()