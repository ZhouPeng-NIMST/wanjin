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



'''

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
'''