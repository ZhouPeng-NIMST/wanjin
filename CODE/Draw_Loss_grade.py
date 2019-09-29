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

font = FontProperties(fname=os.path.join(os.path.dirname(__file__),'simsun.ttf'), size=7)

def Draw_grade(outfile, strdate, data):

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

    print data
    print yearof5

    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)
    # plt.plot(strdate, data, '*', color = 'black', lw = 0.8)
    plt.plot(strdate, data, '-', marker ='.',color='black', lw = 0.8, label = u'直接经济损失等级')
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

    # 绘制一次拟合线性趋势线
    # k, b = curve_fit(func, range(len(data)), data)[0]
    #
    # y1 = np.array(range(len(data))) * k + b
    #
    # plt.plot([strdate[0], strdate[-1]], [y1[0], y1[-1]], color='black', lw = 0.75, label = u'线性趋势')
    #
    ax.set_xlim(xstart, xend)
    # ax.set_ylim(150, 450)

    formatter = DateFormatter('%Y')
    ax.xaxis.set_major_locator(formatter)
    ax.xaxis.set_major_locator(YearLocator(base=5))
    # ax.set_xlabel(str, fontsize=14)
    # ax.xaxis.set_label_coords(0.75, -2.5)


    plt.title(u'直接经济损失等级', fontproperties=font, fontsize=12)

    ax.set_xlabel(u'年   份', fontproperties=font, fontsize=10)
    ax.set_ylabel(u'等   级', fontproperties=font, fontsize=10)

    # 线性拟合函数
    # ax.text(xstart+datetime.timedelta(days=180), 440, 'y=%.3fx+%.3f'%(k, b),  fontproperties=font, fontsize=8)
    # R2 = computeCorrelation(data, y1)
    # ax.text(xstart+datetime.timedelta(days=180), 430, 'R^2=%.3f'%(R2),  fontproperties=font, fontsize=8)
    ax.legend(loc='upper right', prop=font, fontsize=6, edgecolor ='white')

    plt.savefig(outfile, dpi=200, bbox_to_anchor='tight')

    # plt.show()

def CalGrade(source_data):

    data = np.sort(source_data)
    N_Grade = 9    # 分多少个等级

    datasize = data.shape[0]
    re_grade = np.full(datasize, fill_value=99, dtype=np.int32)

    x = [ np.ceil(i * datasize * 100 / (N_Grade * 100))  for i in range(1, N_Grade+1)]
    x = np.array(x).astype(np.int32)
    print(x)
    print data[x-1]
    print(source_data)

    for i in range(datasize):
        for j in range(N_Grade):
            if j == 0:
                if source_data[i] < data[x[j]-1]:
                    re_grade[i] = 1
            # elif j == N_Grade - 1:
            #     if source_data[i] <= data[x[j]-1] and source_data[i] >= data[x[j-1]-1]:
            #         re_grade[i] = N_Grade
            else:
                if source_data[i] <= data[x[j]-1] and source_data[i] >= data[x[j-1]-1]:
                    re_grade[i] = j+1
    print re_grade
    return  re_grade


if __name__ == '__main__':
    filename = ur'D:\wanjin\灾情数据\总损失量分析.xls'
    readbook = xlrd.open_workbook(filename)

    # sheet = readbook.sheet_by_name(u'总损失量')
    sheet = readbook.sheet_by_index(2)    # 读取损失总量数据

    waterofyear =  sheet.col_values(17)[1:41]
    strtime =  sheet.col_values(0)[1:41]

    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]


    grade = CalGrade(waterofyear)

    Draw_grade("./image/Loss_Grade_Times.png", strDate, grade)