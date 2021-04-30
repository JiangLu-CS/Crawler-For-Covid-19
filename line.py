import time, json, requests
from datetime import datetime
import pandas as pd
import pymongo
import pyecharts.options as opts
from pyecharts.charts import Line,Page
from pyecharts.commons.utils import JsCode
client = pymongo.MongoClient('localhost', 27017)
mydb = client['news']
table = mydb['chinaday']
table1 = mydb['continent']
table2 = mydb['globalCount']

data = pd.DataFrame(list(table.find()))
data1 = pd.DataFrame(list(table1.find()))
data2 = pd.DataFrame(list(table2.find()))

date_list = list(data['date'])
confirm_list = list(data['confirm'])
nowconfirm_list = list(data['nowConfirm'])
suspect_list = list(data['suspect'])
dead_list = list(data['dead'])
heal_list = list(data['heal'])

ContinentDate_list = list(data1['date'])
ya_list = list(data1['亚洲'])
qi_list = list(data1['其他'])
bei_list = list(data1['北美洲'])
da_list = list(data1['大洋洲'])
ou_list = list(data1['欧洲'])
print(ya_list)                        # 日期

gdate_list = list(data2['date'])
gconfirm_list = list(data2['confirm'])
gnewconfirm_list = list(data2['newAddConfirm'])
gdead_list = list(data2['dead'])
gheal_list = list(data2['heal'])

line = (
    Line()
    .add_xaxis(date_list)
    # 平均线 最大值 最小值
    .add_yaxis('确诊', confirm_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('疑似', suspect_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('死亡', dead_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('治愈', heal_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('确诊未治愈', nowconfirm_list, is_smooth=True,
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                           opts.MarkPointItem(type_="min")]))

    # 隐藏数字 设置面积
    # 隐藏数字 设置面积
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False))
    # 设置x轴标签旋转角度
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
                     yaxis_opts=opts.AxisOpts(name='人数', min_=3),
                     title_opts=opts.TitleOpts(title='中国疫情曲线图'))
    )


line1 = (
    Line()
    .add_xaxis(ContinentDate_list)
    # 平均线 最大值 最小值
    .add_yaxis('亚洲', ya_list, is_smooth=True)
    .add_yaxis('其他', qi_list, is_smooth=True)
    .add_yaxis('北美洲', bei_list, is_smooth=True)
    .add_yaxis('大洋洲', da_list, is_smooth=True)
    .add_yaxis('欧洲', ou_list, is_smooth=True)

    # 隐藏数字 设置面积
    # 隐藏数字 设置面积
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False))
    # 设置x轴标签旋转角度
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
                     yaxis_opts=opts.AxisOpts(name='人数', min_=3),
                     title_opts=opts.TitleOpts(title='洲疫情曲线图'))
    )

line2 = (
    Line()
    .add_xaxis(date_list)
    # 平均线 最大值 最小值
    .add_yaxis('确诊', gconfirm_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    
    .add_yaxis('死亡', gdead_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('治愈', gheal_list, is_smooth=True,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                       opts.MarkPointItem(type_="min")]))
    .add_yaxis('新增确诊', gnewconfirm_list, is_smooth=True,
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                           opts.MarkPointItem(type_="min")]))

    # 隐藏数字 设置面积
    # 隐藏数字 设置面积
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False))
    # 设置x轴标签旋转角度
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
                     yaxis_opts=opts.AxisOpts(name='人数', min_=3),
                     title_opts=opts.TitleOpts(title='全球疫情曲线图'))
    )

page = Page()
page.add(line)
page.add(line1)
page.add(line2)
page.render('疫情曲线图汇总.html')
