import csv
with open('seoul.csv', 'r', encoding = 'cp949') as file:
    data = csv.reader(file)
    header = next(data)
    max_temp = -999 # 최고 기온 값을 저장한 변수
    max_date = ""   # 최고 기온이 가장 높았던 날짜를 지정 할 변수
    for row in data:
        if row[-1] == '':
            row[-1] = -999  # 결측치 값
            row[-1] = float(row[-1])
            print(row)
            if max_temp < row[-1]:
                max_date = row[0]
                max_temp = row[-1]
print(f"기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 {max_date} 이며, {max_temp}(도) 입니다.")