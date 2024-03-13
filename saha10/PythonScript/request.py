import requests

url = 'https://bus.busan.go.kr/busanBIMS/bus_map1/bims_web/popup2/RealTimeBus.aspx?BNUM=1010-A'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f'Error : {response.status_code}')
