import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts
import pandas as pd
import pymongo
import pyecharts.options as opts
from pyecharts.charts import Line,Page
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
from pyecharts import options
client = pymongo.MongoClient('localhost', 27017)
mydb = client['news']
table = mydb['globalStatistic']
data = pd.DataFrame(list(table.find()))

datan = []

to_english = {'中国': 'China', '丹麦': 'Denmark', '以色列': 'Israel', '伊拉克': 'Iraq', '俄罗斯': 'Russia', '克罗地亚': 'Croatia',
              '冰岛': 'Iceland', '加拿大': 'Canada', '爱尔兰': 'Ireland', '北马其顿': 'North Macedonia', '博茨瓦纳': 'Botswana', '印度': 'India',
              '厄瓜多尔': 'Ecuador', '哥伦比亚': 'Colombia', '圣马力诺': 'San Marino', '埃及': 'Egypt', '墨西哥': 'Mexico', '奥地利': 'Austria',
              '尼日利亚': 'Nigeria', '尼泊尔': 'Nepal', '巴基斯坦': 'Pakistan', '巴林': 'Bahrain', '巴西': 'Brazil', '希腊': 'Greece', '德国': 'Germany',
              '挪威': 'Norway', '摩纳哥': 'Monaco', '斯里兰卡': 'Sri Lanka', '新西兰': 'New Zealand', '柬埔寨': 'Cambodia', '格鲁吉亚': 'Georgia',
              '比利时': 'Belgium', '法国': 'France', '泰国': 'Thailand', '澳大利亚': 'Australia', '爱沙尼亚': 'Estonia', '瑞典': 'Sweden',
              '瑞士': 'Switzerland', '白俄罗斯': 'Belarus', '科威特': 'Kuwait', '科特迪瓦': 'Côte d\'Ivoire', '立陶宛': 'Lithuania', '罗马尼亚': 'Romania',
              '芬兰': 'Finland', '英国': 'United Kingdom', '荷兰': 'Netherlands', '菲律宾': 'Philippines', '西班牙': 'Spain', '越南': 'Vietnam',
              '阿塞拜疆': 'Azerbaijan', '阿富汗': 'Afghanistan', '阿尔及利亚': 'Algeria', '阿曼': 'Oman', '阿联酋': 'UAE', '马来西亚': 'Malaysia',
              '黎巴嫩': 'Lebanon', '韩国': 'Korea', '伊朗': 'Iran', '意大利': 'Italy', '新加坡': 'Singapore', '日本': 'Japan', '钻石公主号': 'Diamond Princess',
              '美国': 'United States', '捷克': 'Czech Rep.', '印度尼西亚': 'Indonesia', '卡塔尔': 'Qatar', '多米尼加': 'Dominica', '卢森堡': 'Luxembourg',
              '葡萄牙': 'Portugal', '亚美尼亚': 'Armenia', '约旦': 'Jordan', '安道尔': 'Andorra', '塞内加尔': 'Senegal', '沙特阿拉伯': 'Saudi Arabia',
              '突尼斯': 'Tunisia', '拉脱维亚': 'Latvia', '摩洛哥': 'Morocco', '乌克兰': 'Ukraine', '阿根廷': 'Argentina', '智利': 'Chile', '波兰': 'Poland',
              '匈牙利': 'Hungary', '斯洛文尼亚': 'Slovenia', '波黑': 'Bosnia and Herzegovina', '南非': 'South Africa', '法属圭亚那': 'French Guiana',
              '巴勒斯坦': 'Palestine', '不丹': 'Bhutan', '喀麦隆': 'Cameroon', '梵蒂冈': 'Vatican', '塞尔维亚': 'Serbia', '斯洛伐克': 'Slovakia',
              '秘鲁': 'Peru', '多哥': 'Togo', '列支敦士登公国': 'Principality of Liechtenstein', '哥斯达黎加': 'Costa rica', '马耳他': 'Malta',
              '马尔代夫': 'Maldives', '巴拉圭': 'Paraguay', '摩尔多瓦': 'Moldova', '文莱': 'Brunei', '孟加拉国': 'Bangladesh', '保加利亚': 'Bulgaria',
              '阿尔巴尼亚': 'Albania', '塞浦路斯': 'Cyprus', '布基纳法索': 'Burkina Faso', '蒙古国': 'Mongolia', '巴拿马': 'Panama', '土耳其': 'Turkey',
              '牙买加': 'Jamaica', '玻利维亚': 'Bolivia', '洪都拉斯': 'Honduras', '圭亚那': 'Guyana', '古巴': 'Cuba', '加纳': 'Ghana', '加蓬': 'Gabon',
              '特立尼达和多巴哥': 'Trinidad and Tobago', '肯尼亚': 'Kenya', '哈萨克斯坦': 'Kazakhstan', '埃塞俄比亚': 'Ethiopia', '几内亚': 'Guinea',
              '苏丹': 'Sudan', '委内瑞拉': 'Venezuela', '乌拉圭': 'Uruguay', '危地马拉': 'Guatemala', '安提瓜和巴布达': 'Antigua and Barbuda',
              '苏里南': 'Suriname', '毛里塔尼亚': 'Mauritania', '斯威士兰': 'Swaziland', '卢旺达': 'Rwanda', '纳米比亚': 'Namibia',
              '赤道几内亚': 'Equatorial Guinea', '塞舌尔': 'Seychelles', '中非共和国': 'Central African Rep.', '乌兹别克斯坦': 'Uzbekistan',
              '刚果（布）': 'Republic of Congo', '刚果（金）': 'Dem. Rep. Congo', '巴哈马': 'Bahamas', '利比里亚': 'Liberia', '坦桑尼亚': 'Tanzania',
              '索马里': 'Somalia', '贝宁': 'Benin', '利比亚': 'Libya', '黑山': 'Montenegro', '冈比亚': 'Gambia', '巴巴多斯': 'Barbados',
              '吉尔吉斯斯坦': 'Kyrgyzstan', '赞比亚': 'Zambia', '毛里求斯': 'Mauritius', '斐济': 'Fiji', '尼加拉瓜': 'Nicaragua', '萨尔瓦多': 'El Salvador',
              '乍得': 'Chad', '尼日尔': 'Niger', '海地': 'Haiti', '佛得角': 'Cape verde', '马达加斯加': 'Madagascar', '津巴布韦': 'Zimbabwe',
              '巴布亚新几内亚': 'Papua New Guinea', '东帝汶': 'East Timor', '乌干达': 'Uganda', '厄立特里亚': 'Eritrea', '莫桑比克': 'Mozambique',
              '叙利亚': 'Syria', '多米尼克': 'Dominica', '红宝石公主号': 'Ruby Princess', '缅甸': 'Myanmar', '伯利兹': 'Belize', '老挝': 'Lao PDR',
              '马里': 'Mali', '几内亚比绍': 'Guinea - Bissau', '安哥拉': 'Angola', '特克斯和凯科斯群岛': 'Turks and Caicos Islands',
              '圣基茨和尼维斯': 'Saint Kitts and Nevis', '蒙特塞拉特岛': 'Montserrat', '安圭拉': 'Anguilla', '圣卢西亚': 'Santa lucia', '格林纳达': 'Grenada',
              '新喀里多尼亚': 'New Caledonia', '阿鲁巴': 'Aruba', '法属波利尼西亚': 'French Polynesia', '直布罗陀': 'Gibraltar', '马提尼克岛': 'Martinique',
              '塞拉利昂': 'Sierra Leone', '布隆迪': 'Burundi', '马拉维': 'Malawi', '吉布提': 'Djibouti', '圣多美和普林西比': 'Sao Tome and Principe',
              '南苏丹': 'S. Sudan', '也门': 'Yemen', '圣文森特岛': 'Saint Vincent', '西撒哈拉': 'Western Sahara', '科摩罗': 'Comoros', '塔吉克斯坦': 'Tajikistan'}
print(data['name'])
print(data['confirm'])
for i in range(0, 180):
    print(data['name'][i])
    try:
        datan.append((to_english[data['name'][i]],int(data['confirm'][i])))
    except KeyError:
        print(data['name'][i] + "没有")

map_world = Map()
map_world.set_global_opts(title_opts=options.TitleOpts(
    # 设置是否为分段显示
    title="世界实时疫情图"),
    visualmap_opts=options.VisualMapOpts(is_piecewise=True,
                                         # 自定义数据范围和对应的颜色，这里我是取色工具获取的颜色值，不容易呀。
                                         pieces=[
                                             # 不指定 max，表示 max 为无限大（Infinity）。
                                             {"min": 100000,
                                              "label": '>100000人', "color": "#7f1a13"},
                                             {"min": 10000, "max": 99999,
                                              "label": '10000-99999人', "color": "#a9251b"},
                                             {"min": 1000, "max": 9999,
                                              "label": '1000-9999人', "color": "#d5514d"},
                                             {"min": 100, "max": 999,
                                              "label": '100-999人', "color": "#e57c6d"},
                                             {"min": 50, "max": 99,
                                              "label": '50-99人', "color": "#f19d8a"},
                                             {"min": 10, "max": 49,
                                              "label": '10-49人', "color": "#f6c6b6"},
                                             {"min": 1, "max": 9,
                                              "label": '1-9人', "color": "#fbe6dc"}]))
print(datan)
map_world.add("确诊", datan, maptype="world")
map_world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map_world.set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
map_world.render("world.html")  # 生成html文件

c = (
    Map().set_global_opts(title_opts=options.TitleOpts(
    # 设置是否为分段显示
    title="世界实时疫情图"),
    visualmap_opts=options.VisualMapOpts(is_piecewise=True,
                                         # 自定义数据范围和对应的颜色，这里我是取色工具获取的颜色值，不容易呀。
                                         pieces=[
                                             # 不指定 max，表示 max 为无限大（Infinity）。
                                             {"min": 1000000,
                                              "label": '>100000人', "color": "#7f1a13"},
                                             {"min": 100000, "max": 99999,
                                              "label": '10000-99999人', "color": "#a9251b"},
                                             {"min": 10000, "max": 9999,
                                              "label": '1000-9999人', "color": "#d5514d"},
                                             {"min": 1000, "max": 999,
                                              "label": '100-999人', "color": "#e57c6d"},
                                             {"min": 500, "max": 99,
                                              "label": '50-99人', "color": "#f19d8a"},
                                             {"min": 100, "max": 49,
                                              "label": '10-49人', "color": "#f6c6b6"},
                                             {"min": 10, "max": 9,
                                              "label": '1-9人', "color": "#fbe6dc"}]))

    .add("确诊", datan, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=10000000),
    )
    .render("map_world.html")
)
print("生成完成！！！")