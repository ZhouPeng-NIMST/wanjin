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


font = FontProperties(fname=os.path.join(os.path.dirname(__file__),'simsun.ttf'), size=7)
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']= 'sans-serif'


def Draw_Flood_Time(outfile, strdate, data, eco_loss):
    eco_loss = np.array(eco_loss)
    yearof5 = []
    for i in range(0, len(data)):
        star = i-5
        if i == 0:
            yearof5.append(data[i])
            continue

        if star <0:
            star = 0

        temp = data[star:i+1]
        yearof5.append(np.sum(temp) / len(temp))

    # fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111)

    # df = pd.DataFrame({u"受灾面积":data, u'直接经济损失':eco_loss}, index=strdate)
    # ax = df.plot(secondary_y = [u'直接经济损失'],
    #              x_compat = True,
    #              linestyle= '-',
    #              marker ='.',
    #              lw = 0.8,
    #              figsize=(8,5),
    #              rot = 0
    #              )
    fig = plt.figure(figsize=(8,5))
    ax_l = fig.add_subplot(111)
    ax_r = ax_l.twinx()
    ax_l.plot(strdate, data, '-', marker ='.',color='black', lw = 0.8, label = u'受灾面积')
    ax_r.plot(strdate, eco_loss, '--', marker ='.',color='black', lw = 0.8, label = u'直接经济损失')

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

    ax_l.set_xlabel(u'年   份', fontproperties=font, fontsize=10)
    ax_l.set_ylabel(u'农作物受灾面积(万公顷)', fontproperties=font, fontsize=10)
    ax_r.set_ylabel(u'直接经济损失(万元)', fontproperties=font, fontsize=10)
    # ax.plot(strdate, eco_loss, '--', marker ='.',color='red', lw = 0.8, label = u'直接经济损失')
    # ax.set_ylabel(u'直接经济损失(万元)', fontproperties=font, fontsize=10)
    # 线性拟合函数
    # ax.text(xstart+datetime.timedelta(days=180), 440, 'y=%.3fx+%.3f'%(k, b),  fontproperties=font, fontsize=8)
    # R2 = computeCorrelation(data, y1)
    # ax.text(xstart+datetime.timedelta(days=180), 430, 'R^2=%.3f'%(R2),  fontproperties=font, fontsize=8)
    ax_l.legend(loc='upper right',
                bbox_to_anchor = (0.97,1),
                prop=font,
                fontsize=6,
                edgecolor ='white')
    ax_r.legend(loc='upper right',
                bbox_to_anchor = (1,0.96),
                prop=font,
                fontsize=6,
                edgecolor ='white')
    ####################################################

    plt.savefig(outfile, dpi=200, bbox_to_anchor='tight')

    # plt.show()


def Draw_Drought_Time(outfile, strdate, data, eco_loss):
    eco_loss = np.array(eco_loss)
    yearof5 = []
    for i in range(0, len(data)):
        star = i-5
        if i == 0:
            yearof5.append(data[i])
            continue

        if star <0:
            star = 0

        temp = data[star:i+1]
        yearof5.append(np.sum(temp) / len(temp))

    # fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111)

    # df = pd.DataFrame({u"受灾面积":data, u'直接经济损失':eco_loss}, index=strdate)
    # ax = df.plot(secondary_y = [u'直接经济损失'],
    #              x_compat = True,
    #              linestyle= '-',
    #              marker ='.',
    #              lw = 0.8,
    #              figsize=(8,5),
    #              rot = 0
    #              )
    fig = plt.figure(figsize=(8,5))
    ax_l = fig.add_subplot(111)
    ax_r = ax_l.twinx()
    ax_l.plot(strdate, data, '-', marker ='.',color='black', lw = 0.8, label = u'受灾面积')
    ax_r.plot(strdate, eco_loss, '--', marker ='.',color='black', lw = 0.8, label = u'直接经济损失')

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

    ax_l.set_xlabel(u'年   份', fontproperties=font, fontsize=10)
    ax_l.set_ylabel(u'农作物受灾面积(公顷)', fontproperties=font, fontsize=10)
    ax_r.set_ylabel(u'直接经济损失(万元)', fontproperties=font, fontsize=10)
    # ax.plot(strdate, eco_loss, '--', marker ='.',color='red', lw = 0.8, label = u'直接经济损失')
    # ax.set_ylabel(u'直接经济损失(万元)', fontproperties=font, fontsize=10)
    # 线性拟合函数
    # ax.text(xstart+datetime.timedelta(days=180), 440, 'y=%.3fx+%.3f'%(k, b),  fontproperties=font, fontsize=8)
    # R2 = computeCorrelation(data, y1)
    # ax.text(xstart+datetime.timedelta(days=180), 430, 'R^2=%.3f'%(R2),  fontproperties=font, fontsize=8)
    ax_l.legend(loc='upper right',
                bbox_to_anchor = (0.97,1),
                prop=font,
                fontsize=6,
                edgecolor ='white')
    ax_r.legend(loc='upper right',
                bbox_to_anchor = (1,0.96),
                prop=font,
                fontsize=6,
                edgecolor ='white')
    ####################################################

    plt.savefig(outfile, dpi=200, bbox_to_anchor='tight')

    # plt.show()



if __name__ == '__main__':
    filename = ur'D:\wanjin\灾情数据\总损失量分析.xls'
    readbook = xlrd.open_workbook(filename)

    sheet = readbook.sheet_by_name(u'洪涝')
    # sheet = readbook.sheet_by_index(2)    # 读取损失总量数据


    strtime =  sheet.col_values(0)[1:41]
    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]

    AreaofCrops =  sheet.col_values(9)[1:41]
    Economic_Loss =  sheet.col_values(17)[1:41]


    Draw_Flood_Time(r"./image/Flood_times.png", strDate, AreaofCrops, Economic_Loss)

    sheet1 = readbook.sheet_by_name(u'旱灾')
    # sheet = readbook.sheet_by_index(2)    # 读取损失总量数据

    strtime =  sheet1.col_values(0)[1:41]

    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]

    AreaofCrops =  sheet1.col_values(10)[1:41]
    Economic_Loss =  sheet1.col_values(18)[1:41]

    Draw_Drought_Time(r"./image/drought_times.png", strDate, AreaofCrops, Economic_Loss)