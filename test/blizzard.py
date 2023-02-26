import requests


def test_getSeason():
    url = "http://127.0.0.1:80/sc2/getseason"
    mocResponse = {
        'endDate': '1680332400',
        'number': 1,
        'seasonId': 1,
        'startDate': '1672905600',
        'year': 2023}

    response = requests.get(url)
    data = response.json()
    if mocResponse == data:
        return True
    else:
        raise NameError('getSeason() response did not match the mocResponse')
