import censys

print(censys.allData['AK']['Anchorage'])
anchoragePop = censys.allData['AK']["Anchorage"]['pop']
print('Население округа Анкоридж в 2010 году - ' + str(anchoragePop))