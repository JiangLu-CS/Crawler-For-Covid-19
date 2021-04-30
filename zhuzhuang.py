from datetime import datetime
import pandas as pd
import pymongo
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar,Page
client = pymongo.MongoClient('localhost', 27017)
mydb = client['news']
table = mydb['rank']
# 读取数据
data = pd.DataFrame(list(table.find()))
dataDeadTop = data[data['type'] == '死亡率最高']
dataHealTop = data[data['type'] == '治愈率最高']
dataHealTail = data[data['type'] == '治愈率最低']
dataDeadTail = data[data['type'] == '死亡率最低']
page = Page()
# 选择需要显示的字段




dataDeadTopcountry_list = list(dataDeadTop['country'])
dataDeadTophealRate_list = list(dataDeadTop['healRate'])
dataDeadTopdeadRate_list = list(dataDeadTop['deadRate'])

dataHealTopcountry_list = list(dataHealTop['country'])
dataHealTophealRate_list = list(dataHealTop['healRate'])
dataHealTopdeadRate_list = list(dataHealTop['deadRate'])

dataHealTailcountry_list = list(dataHealTail['country'])
dataHealTailhealRate_list = list(dataHealTail['healRate'])
dataHealTaildeadRate_list = list(dataHealTail['deadRate'])

dataDeadTailcountry_list = list(dataDeadTail['country'])
dataDeadTailhealRate_list = list(dataDeadTail['healRate'])
dataDeadTaildeadRate_list = list(dataDeadTail['deadRate'])

bar1 = (
    Bar()
    .add_xaxis(dataDeadTopcountry_list)

    .add_yaxis('死亡率', dataDeadTopdeadRate_list)
    .add_yaxis('治愈率', dataDeadTophealRate_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="死亡率最高的国家", subtitle="百分比"))

    )

bar2 = (
    Bar()
    .add_xaxis(dataHealTopcountry_list)

    .add_yaxis('死亡率', dataHealTopdeadRate_list)
    .add_yaxis('治愈率', dataHealTophealRate_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="治愈率最高的国家", subtitle="百分比"))

    )

bar3 = (
    Bar()
    .add_xaxis(dataDeadTailcountry_list)

    .add_yaxis('死亡率', dataDeadTaildeadRate_list)
    .add_yaxis('治愈率', dataDeadTailhealRate_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="死亡率最低的国家", subtitle="百分比"))

    )

bar4 = (
    Bar()
    .add_xaxis(dataHealTailcountry_list)

    .add_yaxis('死亡率', dataHealTaildeadRate_list)
    .add_yaxis('治愈率', dataHealTailhealRate_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="治愈率最低的国家", subtitle="百分比"))

    )

page.add(bar1)
page.add(bar2)
page.add(bar3)
page.add(bar4)
page.render('死亡治愈比例.html')
