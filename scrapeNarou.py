import requests


def fetchNobel(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url,
                     auth=('user', 'pass'), headers=headers)
    return r.text


if __name__ == "__main__":
    url = 'https://ncode.syosetu.com/n6971fy/1/'
    response = fetchNobel(url)
    print(response)
