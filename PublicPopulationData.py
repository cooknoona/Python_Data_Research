import csv
import matplotlib.pyplot as plt

def gender_calc(loc_tmp):
    m = []  # 남성 데이터
    f = []  # 여성 데이터
    with open('gender.csv', encoding='cp949') as file:
        data = csv.reader(file)
        for row in data:
            if loc_tmp in row[0]:
                for i in row[3:104]:
                    m.append(-int(i))  # 남성 정보를 리스트에 저장
                for i in row[106:]:
                    f.append(int(i))  # 여성 정보를 리스트에 저장
    return m, f  # m, f 리스트 반환

loc = input("인구 통계를 검색할 지역(동)을 입력 해 주세요: ")
m, f = gender_calc(loc)  # m, f 값을 받아옴

plt.rc('font', family="Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
plt.title(f'{loc} 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()
