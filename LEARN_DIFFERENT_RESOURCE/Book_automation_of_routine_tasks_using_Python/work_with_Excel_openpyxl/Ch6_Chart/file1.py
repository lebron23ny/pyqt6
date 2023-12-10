import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):
    sheet['A' + str(i)] = i



refObj = openpyxl.chart.Reference(sheet, min_col = 1, min_row=1, max_col=1, max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='Ряд 1')
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'Моя диаграмма'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')