from datetime import datetime
from bs4 import BeautifulSoup
import json
import requests

"""현재 날짜"""
year = datetime.today().year
month = datetime.today().month
day = datetime.today().day


def crawling(day):
    """웹페이지 크롤링"""
    webpage = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={day}%EC%9D%BC").text
    soup = BeautifulSoup(webpage, "html.parser")
    links = soup.find_all("a", class_="news_tit")

    """오늘부터 +2일까지의 기사들 파일 입력"""

    for page in range(day, day+3):
        f = open(f"C:\\Users\\W45176\\Desktop\\trade\\{year}-{month}-{day}.txt", 'w')
        webpage = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={day}%EC%9D%BC").text
        soup = BeautifulSoup(webpage, "html.parser")
        links = soup.find_all("a", class_="news_tit")
        for a in links:
            href = a.attrs['href']
            title = a.attrs['title']
            print(f"{year}-{month}-{day}, {title},>, {href}")
            f.write(f"{year}-{month}-{day}, {title},>, {href}\n\n")
        day+=1
        f.close()
        print()


url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
app_key = "4d4dde1f5c4fa95d72975bfc08bde904"
code = "cKYd1EZzgg779bDI4YNBxtTdt-JZr86oIi0RaCEs1CQvohxVyAM-XOvxXkVQpUM0yJBIKwopcSEAAAF2XGNt4A"

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)

headers = {
    "Authorization" : "Bearer " + tokens['access_token']
}
data = {
    "template_object" : json.dumps({
        "object_type" : "text",
        "text" : "Hello, world",
        "link" : {
            "web_url" : "www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)

print(tokens['access_token'])
print(response.status_code)


#crawling(day)
