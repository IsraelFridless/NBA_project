import requests


def get_data():
    seasons = ['2022', '2023', '2024']
    base_url = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query'
    response = []

    for season in seasons:
        url = f'{base_url}?season={season}&&pageSize=50'
        response.extend(requests.get(url).json())

    return response

