import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

print("1월7일")
url = 
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')+ len('">')
      source_data = source_data[pos2:]

      pos3 = source_data.find('</a>')
      extract_data = source_data[: pos3].strip()

      source_data = source_data[pos3+1:]
      print(i+1, extract_data)
print("1월6일")
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=731&sid1=105&date=20230106'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')+ len('">')
      source_data = source_data[pos2:]

      pos3 = source_data.find('</a>')
      extract_data = source_data[: pos3].strip()

      source_data = source_data[pos3+1:]
      print(i+1, extract_data)
print("1월5일")
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=731&sid1=105&date=20230105'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')+ len('">')
      source_data = source_data[pos2:]

      pos3 = source_data.find('</a>')
      extract_data = source_data[: pos3].strip()

      source_data = source_data[pos3+1:]
      print(i+1, extract_data)
print("1월4일")
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=731&sid1=105&date=20230104'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')+ len('">')
      source_data = source_data[pos2:]
      
      pos3 = source_data.find('</a>')
      extract_data = source_data[: pos3].strip()

      source_data = source_data[pos3+1:]
      print(i+1, extract_data)
print("1월3일")
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=731&sid1=105&date=20230103'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<dt>')

for i in range(count):
      pos1 = source_data.find('<dt>')+ len('<dt>')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')+ len('">')
      source_data = source_data[pos2:]

      pos3 = source_data.find('</a>')
      extract_data = source_data[: pos3].strip()

      source_data = source_data[pos3+1:]
      print(i+1, extract_data)
