# requests 모듈을 이용해서
# 네이버 뉴스 모바일 화면에서 있는 뉴스들 제목 전체 가져오기
import requests

# headers없으면 네이버가 요청차단
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos1 = source_data.find('>')+ len('>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('</a>')
      extract_data = source_data[: pos2]
      extract_data = extract_data.strip()

      source_data = source_data[pos2+1:]
      print(i+1, extract_data)
     
