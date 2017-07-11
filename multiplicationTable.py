#!/usr/bin/env python3
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
ws = wb.active
N=int(input('please input your number: '))
for i in range(2,N+2):    #初始化行1和列A
    ws.cell(row=i, column=1).value = i - 1
    ws.cell(row=i, column=1).font = Font(bold=True)
    ws.cell(row=1, column=i).value = i - 1
    ws.cell(row=1, column=i).font = Font(bold=True)
for rowNum in range(2,N+2):   #计算填充乘法表
    for columnNum in range(2,N+2):
        ws.cell(row=rowNum,column=columnNum).value = ws.cell(row=rowNum,column=1).value * ws.cell(row=1,column=columnNum).value
filename = str(N) + 'x' + str(N) + '.xlsx'
wb.save(filename)
