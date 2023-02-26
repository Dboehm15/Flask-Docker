import requests


def dockerTest():
    url = "http://127.0.0.1:80/healthcheck/test"
    stuffNthangs = {'stuff': 4,
                    'thang': 5}

    send = requests.post(url, data=stuffNthangs)

    if str(send.text) == "4 + 5 = 9":
        return True
    else:
        raise NameError('The calculation string was not returned')
