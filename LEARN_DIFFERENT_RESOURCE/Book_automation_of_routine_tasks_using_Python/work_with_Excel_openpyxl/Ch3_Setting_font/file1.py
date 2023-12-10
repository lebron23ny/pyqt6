import openpyxl

from openpyxl.styles import Font


wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Здравствуй мир!'
wb.save('slykews.xlsx')