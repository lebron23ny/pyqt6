import openpyxl
wb = openpyxl.Workbook()
print(wb.sheetnames)
sheet = wb.active
print(sheet.title)
#Меняем название листа
sheet.title = "Spam Bacon Eggs Sheet"

wb.save('examply_copy.xlsx')