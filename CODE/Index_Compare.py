#coding:utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import datetime
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY, YearLocator
from scipy.optimize import curve_fit
import xlrd
from matplotlib.font_manager import FontProperties
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# font = FontProperties(fname=os.path.join(os.path.dirname(__file__),'simsun.ttf'), size=7)
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family']= 'sans-serif'

def Draw_Index_Compare(outfile, strdate, data):
    fig = plt.figure(figsize=(12,8))
    ax_l = fig.add_subplot(111)

    # for key in data.keys():
    #     Data =  data[key]
    #     Data[Data< -10] = np.nan
    #     print Data
    #     ax_l.plot(strdate, Data, '.', marker ='o',color='black', lw = 0.8, label = key)

    print np.array(data["PDSI"])==-999.0

    ax_l.plot(strdate, data["PDSI"], '.', marker ='o',color='r', label = u'PDSI指数')
    ax_l.plot(strdate, data["SPI"],  '.', marker ='d',color='g', lw = 0.8, label = u'SPI指数')
    ax_l.plot(strdate, data["Z"],    '.', marker ='s',color='b', lw = 0.8, label = u'Z指数')
    ax_l.plot(strdate, data["DF"],   '.', marker ='*',color='black', lw = 0.8, label = u'旱涝指数')
    ax_l.plot(strdate, data["AVG"],  '.', marker ='^',color='c', lw = 0.8, label = u'距平值')


    # plt.plot(strdate, yearof5, '--', color='r', lw = 0.8, label = u'5a滑动平均')

    ##获取时间轴的起始、结束时间
    s = np.int(strdate[0].strftime('%Y'))
    e = np.int(strdate[-1].strftime('%Y'))

    if (s % 10) > 5:
        syear = s / 10 * 10 + 5
    else:
        syear = s / 10 * 10

    if (e % 10) > 5:
        eyear = e / 10 * 10 + 10
    else:
        eyear = e / 10 * 10 + 5

    xstart = datetime.datetime.strptime(str(syear), '%Y')
    xend = datetime.datetime.strptime(str(eyear), '%Y')

    ###############################################
    # ax.set_xlim(xstart, xend)
    # formatter = DateFormatter('%Y')
    # ax.xaxis.set_major_locator(formatter)
    # ax.xaxis.set_major_locator(YearLocator(base=5))
    #
    # plt.title(u'直接经济损失等级', fontproperties=font, fontsize=12)
    #
    # ax.set_xlabel(u'年   份', fontproperties=font, fontsize=10)
    # ax.set_ylabel(u'农作物受灾面积(万公顷)', fontproperties=font, fontsize=10)
    # ax.right_ax.set_ylabel(u'直接经济损失(亿元)', fontproperties=font, fontsize=10)
    ####################################################
    ax_l.set_xlim(xstart, xend)
    formatter = DateFormatter('%Y')
    ax_l.xaxis.set_major_locator(formatter)
    ax_l.xaxis.set_major_locator(YearLocator(base=5))
    # ax.set_xlabel(str, fontsize=14)
    # ax.xaxis.set_label_coords(0.75, -2.5)
    # plt.title(u'直接经济损失', fontproperties=font, fontsize=12)


    ax_l.legend(loc='upper right',
                bbox_to_anchor = (0.95,1),
                # prop=font,
                fontsize=9,
                edgecolor ='white')
    ####################################################

    plt.savefig(outfile, dpi=200, bbox_to_anchor='tight')

    # plt.show()

if __name__ == '__main__':

    filename = ur'E:\Personal\wanjin\指标年值\汇总.xlsx'
    readbook = xlrd.open_workbook(filename)

    # sheet = readbook.sheet_by_name(u'洪涝')
    sheet = readbook.sheet_by_index(0)    # 读取指标数据


    strtime =  sheet.col_values(0)[5:71]
    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]
    print(strDate)

    Index_PDSI =  np.array(sheet.col_values(1)[5:71])
    Index_SPI =  np.array(sheet.col_values(3)[5:71])
    Index_Z =  np.array(sheet.col_values(5)[5:71])
    Index_DF =  np.array(sheet.col_values(7)[5:71])
    Index_AVG =  np.array(sheet.col_values(9)[5:71])

    Index_PDSI[Index_PDSI ==  -999.0] = np.nan
    Index_SPI[Index_SPI == -999] = np.nan
    Index_Z[Index_Z == -999] = np.nan
    Index_DF[Index_DF == -999] = np.nan
    Index_AVG[Index_AVG == -999] = np.nan

    Data = {
        "PDSI": Index_PDSI,
        "SPI":  Index_SPI,
        "Z":    Index_Z,
        "DF":   Index_DF,
        "AVG":  Index_AVG,
    }
    # print Index_PDSI
    Draw_Index_Compare("./image/IndexCompare.png", strDate, Data)



