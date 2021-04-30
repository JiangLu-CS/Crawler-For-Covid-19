import pyecharts.options as opts
from pyecharts.charts import Line
x=['1','2','4','8']
y=[1197,211,84,63]


line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(is_smooth=True,series_name="不同线程并行时间",y_axis=y,symbol="arrow",is_symbol_show=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="OpenMP不同线程运行时间比较"))
)
line.render("OpenMP不同线程运行时间比较.html")
