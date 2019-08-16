import requests
res = requests.get("https://www.largitdata.com/course/7/")
print(res)  # 有回應  <Response [200]>
print(res.text)