#!/usr/bin/env python3
import openpyxl
from openpyxl.utils import column_index_from_string

def rowCopy (ws1,row1,ws2,row2):
    for cell in ws1[row1]:
        ws2.cell(row=row2,column=column_index_from_string(cell.column)).value = cell.value
    return 0

def blankRowInserter (N, M, fileName):
    wb1 = openpyxl.load_workbook(fileName)
    wb2 = openpyxl.Workbook()
    ws1 = wb1.active
    ws2 = wb2.active
    if N == 1:
        for rowNum in range(1,ws1.max_row + 1):
            rowCopy(ws1,rowNum,ws2,rowNum + M)
    elif N > 1 and N <= ws1.max_row:
        for rowNum in range(1,N):
            rowCopy(ws1,rowNum,ws2,rowNum)
        for rowNum in range(N,ws1.max_row + 1):
            rowCopy(ws1,rowNum,ws2,rowNum + M)
    else:
        return 0
    wb1.close()
    wb2.save(fileName)

N = int(input('please input the row number: '))
M = int(input('how many lines would you like to insert: '))
fileName = input('please input the excel file name: ')
blankRowInserter(N, M, fileName)
