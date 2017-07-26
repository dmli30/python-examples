#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def getClick(url):    #返回一个字典，键为文章标题，值为文章点击率
    r = requests.get(url)
    page = BeautifulSoup(r.text, "html.parser").find_all('div', {'class': 'post multi'})
    countDict = {}
    for article in page:
        try:
            title = article.h2.get_text().strip()
            s = article.h6.get_text().split(',')[2].strip()
        except AttributeError as e:    #如果抓取不到标签，则跳出当前循环
            print('article tag not found in ' + url)
            continue
        else:
            num = s.strip().split(':')[1]
            countDict[title] = num
    return countDict

totalClick = 0
countDic = {}
for i in range(1,9):    #总1-8页，手动修改
    url = 'https://www.muzifei.com/page_' + str(i) + '.html'
    countDic.update(getClick(url))
for item in countDic:
    print(item + '  点击率：' + str(countDic[item]))
for i in countDic.values():
    totalClick += int(i)
print('总点击率： ' + str(totalClick))
