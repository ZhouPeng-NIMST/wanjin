#coding:utf-8
import os
import numpy as np
import xlrd
import datetime
from xlutils.copy import  copy

import matplotlib.pyplot as plt
import matplotlib
import math
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY, YearLocator
from scipy.optimize import curve_fit

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=os.path.join(os.path.dirname(__file__),'simsun.ttf'), size=7)



def Cal_sigma(x):
    x_mean = np.nanmean(x)
    x2sum = np.nansum(pow((x - x_mean), 2))

    sigma = np.sqrt(x2sum / len(x))

    return sigma

# def Cal_Cs(sigma, waterofyear, Mean):

def MainPro():
    filename = ur'D:\wanjin\Z指数.xlsx'
    readbook = xlrd.open_workbook(filename)
    wb = copy(readbook)
    # sheet = readbook.sheet_by_name(u'总损失量')

    for nn in range(12):
        sheet = readbook.sheet_by_index(nn)    # 读取损失总量数据
        x =  sheet.col_values(1)[1:]
        strtime =  sheet.col_values(0)[1:]

        strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]

        Mean = np.nanmean(x)
        sigma = Cal_sigma(x)

        X = (x - Mean) / sigma
        Cs = np.nansum(pow(x - Mean, 3)) / (len(x) * pow(sigma, 3))

        Z = (6.0 / Cs) * pow((Cs / 2 * X + 1), 1/3.0) - 6.0 / Cs + Cs / 6.0


        ws = wb.get_sheet(nn)

        ws.write(0, 2, 'mean')
        ws.write(0, 3, 'sigma')
        ws.write(0, 4, 'Xi')
        ws.write(0, 5, 'Cs')
        ws.write(0, 6, 'Z_index')
        for i in range(len(x)):
            ws.write(i+1, 2, Mean)
            ws.write(i+1, 3, sigma)
            ws.write(i+1, 4, X[i])
            ws.write(i+1, 5, Cs)
            ws.write(i+1, 6, Z[i])

    wb.save('./image/Z_index.xls')

def Comp_Mean_Z():
    x = [174.44, 176.29,195.25,179.43,181.74,207.85,294.55,382.01,269.21,454.49,408.90,638.44]


    Mean = np.nanmean(x)
    sigma = Cal_sigma(x)

    X = (x - Mean) / sigma
    Cs = np.nansum(pow(x - Mean, 3)) / (len(x) * pow(sigma, 3))

    Z = (6.0 / Cs) * pow((Cs / 2 * X + 1), 1/3.0) - 6.0 / Cs + Cs / 6.0

    print(Z)


def Draw_Z_Index_Graph(outfile, strdate, data):

    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)
    # plt.plot(strdate, data, '*', color = 'black', lw = 0.8)

    plt.plot(strdate, data[53519], '.', marker ='.',color='k', lw = 0.8, label = u"惠农")
    plt.plot(strdate, data[53612], '.', marker ='^',color='r', lw = 0.8, label = u"吴忠")
    plt.plot(strdate, data[53614], '.', marker ='D',color='g', lw = 0.8, label = u"银川")
    plt.plot(strdate, data[53615], '.', marker ='+',color='b', lw = 0.8, label = u"陶乐")
    plt.plot(strdate, data[53704], '.', marker ='x',color='c', lw = 0.8, label = u"中卫")
    plt.plot(strdate, data[53705], '.', marker ='*',color='y', lw = 0.8, label = u"中宁")
    plt.plot(strdate, data[53723], '.', marker ='s',color='m', lw = 0.8, label = u"盐池")
    plt.plot(strdate, data[53806], '.', marker ='8',color='gold', lw = 0.8, label = u"海源")
    plt.plot(strdate, data[53810], '.', marker ='p',color='peru', lw = 0.8, label = u"同心")
    plt.plot(strdate, data[53817], '.', marker ='h',color='brown', lw = 0.8, label = u"固原")
    plt.plot(strdate, data[53903], '.', marker ='v',color='wheat', lw = 0.8, label = u"西吉")
    plt.plot(strdate, data[53910], '.', marker ='.',color='tan', lw = 0.8, label = u"六盘山")

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

    ax.set_xlim(xstart, xend)
    # ax.set_ylim(150, 450)

    formatter = DateFormatter('%Y')
    ax.xaxis.set_major_locator(formatter)
    ax.xaxis.set_major_locator(YearLocator(base=5))
    # ax.set_xlabel(str, fontsize=14)
    # ax.xaxis.set_label_coords(0.75, -2.5)


    plt.title(u'Z指数时间序列图', fontproperties=font, fontsize=12)

    ax.set_xlabel(u'年   份', fontproperties=font, fontsize=10)
    # ax.set_ylabel(u'降水量/mm', fontproperties=font, fontsize=10)
    ax.legend(loc='upper right', prop=font, fontsize=6, edgecolor ='white')
    # plt.savefig(outfile, dpi=200, bbox_to_anchor='tight')

    plt.show()


if __name__ == '__main__':
    # Comp_Mean_Z()

    filename = u'./image/Z值所有站点综合.xlsx'
    readbook = xlrd.open_workbook(filename)

    # print(readbook.sheet_names())
    # sheet = readbook.sheet_by_name(u'降水量')
    sheet = readbook.sheet_by_index(0)

    src_data = {}

    strtime =  sheet.col_values(0)[1:67]
    for i in range(12):
        data =  sheet.col_values(1+i)[1:67]
        data= np.array(data)
        data[data==-999.0] = np.nan
        stationID = sheet.col_values(1+i)[0]
        if not src_data.has_key(stationID):
            src_data.update({ stationID : data})
        else:
            src_data[stationID].append( data )

    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]

    Draw_Z_Index_Graph("./image/Z_index_graph.png", strDate, src_data)

