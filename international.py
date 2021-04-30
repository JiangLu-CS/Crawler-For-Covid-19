'''
爬取给定国家的疫情历史信息
'''
import requests
import xlwt
import datetime
import json
import sys
import pymongo
import json

def getURLContent(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    response = requests.post(url, headers=headers)
    return response.status_code, response

def chinadata():

        print("开始爬取中国的疫情数据... ... ")
        url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList'
        status_code, data = getURLContent(url)


        if status_code != 200:
            print("数据爬取失败,状态码%d" % (status_code))
            sys.exit()
        data = data.json()["data"]
        if data == None:
            print("数据爬取数据为空" )
        print(data['chinaDayList'])

        for data_i in data['chinaDayList']:
            print(data_i)

            statistic = {
            'confirm': data_i['confirm'],
            'date': data_i['date'],
            'dead': data_i['dead'],
            'deadRate': data_i['deadRate'],
            'heal': data_i['heal'],
            'healRate': data_i['healRate'],
            'importedCase': data_i['importedCase'],
            'noInfect': data_i['noInfect'],
            'nowConfirm': data_i['nowConfirm'],
            'nowSevere': data_i['nowSevere'],
            'suspect': data_i['suspect']
            }
        #worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

            client = pymongo.MongoClient('localhost', 27017)
            mydb = client['news']
            collection = mydb['chinaday']
            result = collection.insert(statistic)
            print(result)


def statisticGlobal():
    print("开始爬取各国累计确诊的疫情数据... ... ")
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    status_code, data = getURLContent(url)
    if status_code != 200:
        print("数据爬取失败,状态码%d" % (status_code))
        sys.exit()
    data = data.json()["data"]
    if data == None:
        print("数据爬取数据为空")
    print(data)

    for data_i in data:
        print(data_i)
        statistic = {
            'confirm': data_i['confirm'],
            'confirmAdd': data_i['confirmAdd'],
            'confirmAddCut': data_i['confirmAddCut'],
            'confirmCompare': data_i['confirmCompare'],
            'continent': data_i['continent'],
            'date': data_i['date'],
            'dead': data_i['dead'],
            'deadCompare': data_i['deadCompare'],
            'heal': data_i['heal'],
            'name': data_i['name'],
            'nowConfirm': data_i['nowConfirm'],
            'nowConfirmCompare': data_i['nowConfirmCompare'],
            'suspect': data_i['suspect']
        }
        # worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['globalStatistic']
        result = collection.insert(statistic)
        print(result)




def Globalall():
    print("开始爬取全球累计确诊的疫情数据... ... ")
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/' \
          'list?modules=FAutoGlobalDailyList'
    status_code, data = getURLContent(url)
    if status_code != 200:
        print("数据爬取失败,状态码%d" % (status_code))
        sys.exit()
    data = data.json()["data"]
    if data == None:
        print("数据爬取数据为空")
    print(data)

    for data_i in data['FAutoGlobalDailyList']:
        print(data_i)
        print(data_i['date'])
        print(data_i['all']['confirm'])
        statistic = {
            'date': data_i['date'],
            'confirm': data_i['all']['confirm'],
            'dead': data_i['all']['dead'],
            'heal': data_i['all']['heal'],
            'newAddConfirm': data_i['all']['newAddConfirm'],
            'deadRate': data_i['all']['deadRate'],
            'healRate': data_i['all']['healRate'],
        }
        ## worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['globalCount']
        result = collection.insert(statistic)
        print(result)

def allheros():
    print("开始爬取英雄数据... ... ")
    url = 'https://eyesight.news.qq.com/sars/toheros'
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    print(html)
    data = json.loads(html)['data']['allHeros']
    for i in data:
        print(i['name'])
        statistic = {
            'name': i['name'],
            'describe': i['desc'],
            'area': i['area'],
            'sex': i['sex'],
            'age': i['age'],
        }
        ## worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['heros']
        result = collection.insert(statistic)
        print(result)

def allcountries():
    print("开始爬取具体国家数据... ... ")
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoforeignList'
    status_code, data = getURLContent(url)
    if status_code != 200:
        print("数据爬取失败,状态码%d" % (status_code))
        sys.exit()
    data = data.json()["data"]
    if data == None:
        print("数据爬取数据为空")
    print(data)

    for data_i in data['FAutoforeignList']:

        if 'children' in data_i:
            for i in data_i['children']:
                print(i['name'])
                statistic = {
                    'countryName': data_i['name'],
                    'statesName': i['name'],
                    'nameMap': i['nameMap'],
                    'confirmAdd': i['confirmAdd'],
                    'confirm': i['confirm'],
                    'dead': i['dead'],
                    'heal': i['heal']

                }
                ## worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

                client = pymongo.MongoClient('localhost', 27017)
                mydb = client['news']
                collection = mydb['states']
                result = collection.insert(statistic)
                print(result)

def continent():
    print("开始爬取具体国家数据... ... ")
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoContinentStatis'
    status_code, data = getURLContent(url)
    if status_code != 200:
        print("数据爬取失败,状态码%d" % (status_code))
        sys.exit()
    data = data.json()["data"]
    if data == None:
        print("数据爬取数据为空")


    for data_i in data['FAutoContinentStatis']:
        print(data_i)
        statistic = {
            'date': data_i['date'],
            '亚洲': data_i['statis']['亚洲'],
            '其他': data_i['statis']['其他'],
            '北美洲': data_i['statis']['北美洲'],
            '大洋洲': data_i['statis']['大洋洲'],
            '欧洲': data_i['statis']['欧洲']

        }
        ## worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）

        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['continent']
        result = collection.insert(statistic)
        print(result)

def TopAndTail():
    print("开始爬取具体国家数据... ... ")
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoHealDeadRateRankList'
    status_code, data = getURLContent(url)
    if status_code != 200:
        print("数据爬取失败,状态码%d" % (status_code))
        sys.exit()
    data = data.json()["data"]
    if data == None:
        print("数据爬取数据为空")
    print(data)


    for data_i in data['FAutoHealDeadRateRankList']['deadHead']:
        print(data_i)
        statistic = {
            'type': "死亡率最高",
            'country': data_i['country'],
            'confirm': data_i['confirm'],
            'heal': data_i['heal'],
            'dead': data_i['dead'],
            'healRate': data_i['healRate'],
            'deadRate': data_i['deadRate']

        }
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['rank']
        result = collection.insert(statistic)
        print(result)
        ## worksheet.col(0).width = 128 * 20  # 设置excel中第A列的宽度（方便日期数据展示）
    for data_i in data['FAutoHealDeadRateRankList']['healHead']:
        print(data_i)
        statistic = {
            'type': "治愈率最高",
            'country': data_i['country'],
            'confirm': data_i['confirm'],
            'heal': data_i['heal'],
            'dead': data_i['dead'],
            'healRate': data_i['healRate'],
            'deadRate': data_i['deadRate']

        }
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['rank']
        result = collection.insert(statistic)
        print(result)

    for data_i in data['FAutoHealDeadRateRankList']['deadTail']:
        print(data_i)
        statistic = {
            'type': "死亡率最低",
            'country': data_i['country'],
            'confirm': data_i['confirm'],
            'heal': data_i['heal'],
            'dead': data_i['dead'],
            'healRate': data_i['healRate'],
            'deadRate': data_i['deadRate']

        }
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['rank']
        result = collection.insert(statistic)
        print(result)
    for data_i in data['FAutoHealDeadRateRankList']['healTail']:
        print(data_i)
        statistic = {
            'type': "治愈率最低",
            'country': data_i['country'],
            'confirm': data_i['confirm'],
            'heal': data_i['heal'],
            'dead': data_i['dead'],
            'healRate': data_i['healRate'],
            'deadRate': data_i['deadRate']

        }
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['news']
        collection = mydb['rank']
        result = collection.insert(statistic)
        print(result)

if __name__ == "__main__":
    TopAndTail()
    #continent()
    #allcountries()
    #allheros()
    #Globalall()
    #statisticGlobal()
    # 添加要爬取疫情数据的国家
    #chinadata()

    # 保存
