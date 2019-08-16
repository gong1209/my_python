import requests
payload = {
'startStation':'4220-臺南',
'endStation': '0990-松山',
'transfer': 'ONE',
'rideDate': '2019/08/08',
'startOrEndTime': 'true',
'startTime': '08:00',
'endTime': '20:00',
'trainTypeList': 'ALL'
}

##台鐵列車時刻表
res = requests.post("https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime",data=payload)
print(res.text)


