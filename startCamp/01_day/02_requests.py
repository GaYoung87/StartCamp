# 필요한 페이지 가지고오는 방법
# 페이지입력하는 것도 우리가 요청하는 것! -> requests: 파이썬에서 요청하는 모듈
import requests
import bs4 # Beautiful Soup 받은 문서를 보기좋게, 검색하기 좋게 만들어줘

url = 'https://finance.naver.com/sise/'

response = requests.get(url) # response.text -> 문자형형태로 그대로 반환(요청에대한 응답)
print(response)
print(response.status_code)  # ex. 우리가 존재하는 페이지들어가면 200으로 나옴.
# requests.get('주소').status_code -> ex. 404 : 해당페이지는 존재하지 않습니다.
html = response.text #네이버금융이라는 페이지 파일 전체를 텍스트파일로 가지고 있음(응답받은 것을 모두 텍스트로 전환)
# 전부 다 문자열(str) -> 우리가 원하는 정보만 얻을 수 있게 하는것이 bs4
soup = bs4.BeautifulSoup(html, 'html.parser') #parsing = text로 되어있어 우리가 접근할 수 없는 것들을 우리가 접근할 수 있는 형태를 가진 객체로 바꿔주는 것 #접근가능한 값으로 soup으로 가지고옴
kospi = soup.select_one('#KOSPI_now').text #요청받은 것에서 글자만 뽑아줘! #ID로 접근하려면 #을 붙여라 #select_one을 통해 soup을 가지고온다. 
# #KOSPI_now를 알 수 있는 방법은 탐색기(요소검사) 왼쪽에 네모난거누르면 내가 원하는 것에 가져가서 누르면 그 부분의 이름을 알려준다!!
# 이때 #KOSPI_now 는 selector 경로
# .select(selector) : 문서 안에 있는 특정 내용을 모두 뽑아줘 -> list형태로 반환(여러 값들을 다 가지고와달라)
# .select_one(selector) : 문서 안에 있는 특정 내용을 하나만 뽑아줘 -> 변수로 저장


print(kospi)

#searchform -> 이것은 select(?)이다. 이렇게 가능하다!! 이것만 알고 있으면 ok