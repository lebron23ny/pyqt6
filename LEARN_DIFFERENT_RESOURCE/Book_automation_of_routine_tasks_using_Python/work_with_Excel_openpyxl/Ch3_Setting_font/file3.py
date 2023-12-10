
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

fontObj = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt Italic'



wb.save('styles1.xlsx')