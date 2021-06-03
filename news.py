# coding:utf-8

# 引入相关模块
import requests
from bs4 import BeautifulSoup
import os


url = "https://news.qq.com/ninja/qqnews_tuiguang.htm"
# 请求腾讯新闻的URL，获取其text文本
wbdata = requests.get(url).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.bar-con > ul.list> li.item>a")
# 对返回的列表进行遍历
folder_path = 'log'
if not os.path.exists(folder_path):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(folder_path)
f = open(folder_path+ "/news.txt",'w')

for n in news_titles:
    # 提取出标题和链接信息
    title = n.get("title")
    link = n.get("href")
    data = {
        '标题':title,
        '链接':link
    }
    print(data)
    print(str(data), file=f)

f.close()