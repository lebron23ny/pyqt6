
import openpyxl
wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = 'Здравствуй, мир!'
print(sheet['A1'].value)