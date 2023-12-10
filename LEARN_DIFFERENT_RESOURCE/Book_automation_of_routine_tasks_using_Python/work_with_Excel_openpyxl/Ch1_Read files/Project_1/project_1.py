import openpyxl, pprint

#Открытие рабочей книги
wb = openpyxl.load_workbook('../../censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

#Заполнить словарь данными о численности населения и переписных районах округов

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #Заполняем словарь
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

#Запись в файл
print()
print('Запись результатов...')
result_File = open("censys.py", 'w')
result_File.write('allData = ' + pprint.pformat(countyData))
result_File.close()
print('Готово.')
