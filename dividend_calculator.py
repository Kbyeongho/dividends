# 단위는 달러 $
import csv
from typing import final

#list.csv파일을 불러온다.
read_file =  open('./list.csv', 'r', encoding = 'utf-8')
companys = list(csv.reader(read_file))

#csv 주식 번호
num = 1
company = companys[num]
for i in range(1, 4):
	company[i] = float(company[i])

final_dividend = company[2] - (company[2] * (company[3] / 100))
realized_yield = (final_dividend / company[1]) * 100

print(f"{company[0]} / 배당금 : {company[2]}, 실직적인 배당금과 수익률 : {final_dividend, realized_yield}")
