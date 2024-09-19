import requests

def get_data():
    url = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?pageSize=1000'
    response = requests.get(url)
    return response.json()

