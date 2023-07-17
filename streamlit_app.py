from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

import datetime
import streamlit as st


st.subheader('西南多网格预报系统')


col1, col2 = st.columns(2)
with col1:
    d = st.date_input("模式起报日期", datetime.date(2022, 10, 13))
with col2:
    t = st.time_input('模式起报时间', datetime.time(0, 0),step = 12*3600 )
init = datetime.datetime.combine(d, t)
        
fhr = st.slider('fhr', min_value=18, max_value=132, step=6)
image=fr".\{init:%Y%m%d%H}\wrfplt_Single_pcp6_f{fhr}_NE.png"
st.image(image, caption='6h降水预报',use_column_width='auto')    
