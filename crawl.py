from bs4 import BeautifulSoup
import requests
from urllib import parse
from lxml import etree
import pymongo
from fake_useragent import UserAgent
global flag
import time
import datetime
flag = 0

target = "https://search.sina.com.cn/?q=%E6%96%B0%E5%86%A0%E7%96%AB%E6" \
         "%83%85&c=news&from=channel&ie=utf-8"
def parse_detail_page(detail_url):
    req = requests.get(url=detail_url)
    req.encoding = 'utf-8'
    html = req.text
    print('打印页面中')
    bf = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
    body = bf.find('div', class_= 'article')
    hei = ""
    selector = etree.HTML(html)
    title = bf.find('h1', class_='main-title')
    bod = selector.xpath("//*[@id='article']/p/text()")
    DATE = selector.xpath("//*[@id='top_bar']/div/div[2]/span[1]/text()")
    source = selector.xpath("//*[@id='top_bar']/div/div[2]/a/text()")
    author = selector.xpath("//*[@id='top_bar']/div/div[2]/span[2]/a/text()")
    for b in bod:
        hei += b;
    if (title and hei and DATE and source and author):
        print(title.text)
        sinanews = {
            'title': title.text,
            'DATE': DATE[0],
            'source':source[0],
            'author':author[0],
            'derivefrom': '新浪新闻',
            'body': hei
        }
        client = pymongo.MongoClient('localhost',27017)
        mydb = client['news']
        collection = mydb['allnews']
        result = collection.insert(sinanews)
        print(result)


def spidermainsina(target):
    ua = UserAgent()
    print(ua.chrome)
    headers = {"User-Agent": ua.chrome}
    print(ua.random)
    req = requests.get(url=target,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html,'html.parser')
    html = req.text
    titles = bf.find_all('div', class_='box-result clearfix')
    # texts = bf.find_all('p', class_='content')
    for title in titles:
        b = title.find('a')
        print(b.get('href'))
        parse_detail_page(b.get('href'))
    selector = etree.HTML(html)
    base = 'https://search.sina.com.cn/'
    global flag
    if(flag == 0):
        next10url = selector.xpath("//*[@id='_function_code_page']/a[10]/@href")
        next10url = parse.urljoin(base,next10url[0])
        flag = 1


    else:
        next10url = selector.xpath("//*[@id='_function_code_page']/a[12]/@href")
        next10url = parse.urljoin(base, next10url[0])

    if (next10url):
        print(next10url)
        spidermainsina(next10url)




    #https://search.sina.com.cn/?q=%e6%96%b0%e5%86%a0%e7%96%ab%e6%83%85&c=news&from=channel&col=&range=all&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page={}


def main(h, m):

    while True:
        now = datetime.datetime.now()   # 获取当前时间
        print(now.hour, now.minute)
            # 判断时间
        if now.hour in h and now.minute in m:

            print("开始执行一次爬虫")
            spidermainsina(target)
        if now.hour == 22 and now.minute == 10:
            print("一天的爬虫结束了")
            return


        time.sleep(60)


if __name__ == '__main__':
    spidermainsina(target)
    main(h=[8, 10, 12, 14, 16, 18, 20,22], m=[0])


