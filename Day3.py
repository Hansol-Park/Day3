## Too many error occured in Visual Studio 2022
## Now, i'll use pycharm to code

#11 011 변수 사용하기
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

#012 변수 사용하기
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.

시가총액 = 2980000000000
현재가 = 50000
Per = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(Per, type(Per))

#013 문자열 출력
#변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
#두 변수를 이용하여 아래와 같이 출력해보세요.

s = "Hello"
t = "Python"
print(s+"!",t)

#14 파이썬을 이용한 값 계산
#아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3

print( 2 + 2 * 3)

#015 type 함수
#type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.

a = 132
print(type(a))

#16,17 문자열을 정수로 변환
#문자열 '720'를 정수형으로 변환해보세요.

num = 720
result = str(num)
print(result,type(result))

#18 문자열을 실수로 변환
#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

num2 = 15.79
result2 = float(num2)
print(result2, type(result2))

#19 문자열을 정수로 변환
#year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

year = "2020"
RecentYear = int(year)

print("작년 :",RecentYear-1)
print("올해 :",RecentYear)
print("내년 :",RecentYear+1)

#20 파이썬 계산
#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

Monthly = 48584
Total_Price = Monthly * 36
print(Total_Price)
