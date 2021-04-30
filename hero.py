from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import time, json, requests
from datetime import datetime
import pandas as pd
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import pymongo
import pyecharts.options as opts
from pyecharts.charts import Line,Page
from pyecharts.commons.utils import JsCode
client = pymongo.MongoClient('localhost', 27017)
mydb = client['news']
table1 = mydb['heros']
print(table1)
data = pd.DataFrame(list(table1.find()))
print(list(table1.find()))
print()
headers = ["英雄名字", "介绍", "地区", "性别"," 年龄"]
print(list(data['name'][1]))
print(data['name'])
row = []
sublist = []
for i in range(0, 100):

    sublist.append(data['name'][i])
    sublist.append(data['describe'][i])
    sublist.append(data['area'][i])
    sublist.append(data['sex'][i])
    sublist.append(data['age'][i])

    row.append(sublist)
    sublist = []
    #print(sublist)
print(row)
#list = []
#sublist = []
#for i in table:
#    print(i)
#    sublist.append(i[1])
#    sublist.append(i['describe'])
#    sublist.append(i['area'])
#    sublist.append(i['sex'])
#    sublist.append(i['age'])
#    list.append(sublist)
#rows = [list]

table = Table()
table.add(headers, row)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="英雄", subtitle="")
)
table.render("hero.html")
