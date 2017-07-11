#!/usr/bin/env python3
import openpyxl
from openpyxl.utils import column_index_from_string

def blankRowInserter (N, M, fileName):
    wb1 = openpyxl.load_workbook(fileName)
    ws1 = wb1.active
    if N > ws1.max_row:   #如果N大于总行数，则不用插入，因为本来也是空的
        print('This excel is too small to do anything,try another file!')
        return 0
    else:
        wb2 = openpyxl.Workbook()
        ws2 = wb2.active
        for rowOfCell in ws1[1:N-1]:    #两层循环，第一层得到一个由单元格元组组成的元组
            for cell in rowOfCell:    #第二层得到单元格，两个for循环拷贝前N行
                ws2[cell.coordinate].value = cell.value
        for rowOfCell in ws1[N:ws1.max_row]:    #对于剩下的行，行号加M再进行拷贝
            for cell in rowOfCell:
               ws2.cell(row = cell.row + M, column = column_index_from_string(cell.column)).value = cell.value    #用到了column字母转数字
        print('work done!')
        wb2.save(fileName)
        return 0

N = int(input('please input the row number: '))
M = int(input('how many lines would you like to insert: '))
fileName = input('please input the excel file name: ')
blankRowInserter(N, M, fileName)
