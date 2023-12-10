
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Высокая строка'
sheet['B2'] = 'Ширикий столбец'
#Настройка высоты и ширины
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
wb.save('dimensions.xlsx')
