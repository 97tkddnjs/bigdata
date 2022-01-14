from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests

executable_path = "chromedriver.exe"

source_url ="https://newsstand.naver.com/?list=ct4"
#source_url = " https://namu.wiki/"

driver = webdriver.Chrome(executable_path = executable_path)

driver.get(source_url)  #해당 웹을 브라우저에 띄우는 것임~

req = driver.page_source

soup = BeautifulSoup(req,"html.parser")
#html_take = soup.select("#focusPanelCenter")
#print(html_take)


# soup의 select 마냥 밑으로 다 가게 만듬~
# soup.select()
contents_table =soup.find(name ='table')
table_body = contents_table.find(name='tbody')
table_rows = table_body.find_all(name ="tr")

# a 태그의 href 속성을 리스트로 추출하여

