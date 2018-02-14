import requests

LOGINURL = 'http://testing-ground.scraping.pro/login?mode=login'

USER = 'admin'
PASSWORD = '12345'

session = requests.session()

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 OPR/51.0.2830.26'
}

data = {
        'usr': USER,
        'pwd': PASSWORD
}

response = session.post(LOGINURL, data=data, headers=req_headers,
                        allow_redirects=True)

print(response.status_code)
print(response.text)
print(response.cookies.items())
