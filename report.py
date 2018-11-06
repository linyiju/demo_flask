import requests
from bs4 import BeautifulSoup

def get_draft(url): #收集新聞稿
    resp = requests.get(url)
    if resp.status_code is 200:
        resp.encoding = "UTF-8"
        soup = BeautifulSoup(resp.text,"html.parser")
        scope1 = soup.select("#tab1")
        scope2 = scope1[0].select(".taba")

        hot_lines=[]

        for line in scope2: #集成一個list
             hot_lines.append(line.text)

        return hot_lines#顯示出來的list回傳到hot_lines

def speech(report): #把草稿轉變成字串
    text ="大家好"+" "+"歡迎來到超蝦新聞\n"
    i=0
    for news in report:
        text = text+"第"+str(i+1)+"則"+"時間"+news[:2]+"點"+news[3:5]+"分"+news[5:]+"\n"
        i+=1
    return text