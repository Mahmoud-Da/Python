import requests 
from bs4 import BeautifulSoup


loud_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(loud_url)
soup = BeautifulSoup(html.content,"html.parser")

topic = soup.find(class_="sc-fcTNbh jzYQUR")


for element in topic.find_all("a"):
  print(element.text)
