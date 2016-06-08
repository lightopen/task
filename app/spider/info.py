# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

# 为了数据在数据库的存储，将数据转化为值为“标签”和“数值”组成的元组的字典
legal = ["a1", "a2", 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15']

def for_model(info_list):
    for_model_d = {}
    i = 0
    while i < 15:
        for_model_d[legal[i]] = str(info_list[i])
        i += 1
    return for_model_d

# 抽象出来重复的解析过程
def table_parser(table):
    soup = BeautifulSoup(table, 'html.parser', from_encoding='utf-8')
    ths = soup.find_all('th')
    keys = []
    for th in ths:
        text = th.get_text()
        keys.append(text)
    tds = soup.find_all('td')
    values = []
    for td in tds:
        values.append(td.get_text())
    i = 0
    l = []
    while i < len(keys):
        l.append((keys[i], values[i]))
        i += 1
    return l

# 爬虫程序， 返回一个信息list，股票完整代码字符串，和图表url字符床，解析失败则全部返回false
def get_info(code):
    r = requests.get("http://finance.yahoo.com/q;_ylt=Avwusdy.Ly1HO8mOg5ASa9FZM_J_?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s=%s"
                 % code)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    table1 = str(soup.find('table', id='table1'))
    if not table1:
        return False, False, False
    table2 = str(soup.find('table', id='table2'))
    l1 = table_parser(table1)
    l2 = table_parser(table2)
    l1.extend(l2)
    title = soup.find('div', class_="title").get_text()
    image = soup.find('img', src=re.compile(r'chart'))['src']
    print(len(l1))
    return l1, title, image





