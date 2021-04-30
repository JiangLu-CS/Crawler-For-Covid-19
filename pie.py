import pyecharts
from pyecharts.charts import Pie
import pandas as pd
import pymongo
import pyecharts.options as opts
from pyecharts.charts import Line,Page
from pyecharts.commons.utils import JsCode
client = pymongo.MongoClient('localhost', 27017)
mydb = client['news']
table = mydb['chinaday']

attr = ["亚洲", "北美洲", "大洋洲", "欧洲"]
v1 = [14423086, 12340969, 30289, 12446514]

pie = (
    Pie()
    .add(
    attr,
    v1
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="洲饼图"))
)
pie.render(path="饼图汇总.html")