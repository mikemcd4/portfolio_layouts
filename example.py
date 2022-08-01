Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> import os
>>> os.chdir('c:\\Users\s4508\Downloads')
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> sheet = workbook.get_sheet_by_name('Sheet1')

Warning (from warnings module):
  File "<pyshell#5>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> 