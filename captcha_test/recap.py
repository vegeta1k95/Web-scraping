from python3_anticaptcha import NoCaptchaTaskProxyless as nc

from requests import session

ANTICAPTCHA_KEY = "" # Брать с аккаунта на anti-captcha.com

# Тестовые данные
TEST_DATA_KEY = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'  
URL = 'https://www.google.com/recaptcha/api2/demo'


result = nc.NoCaptchaTaskProxyless(anticaptcha_key = ANTICAPTCHA_KEY)\
                                .captcha_handler(websiteURL=URL,
                                                 websiteKey=TEST_DATA_KEY)


key = result['solution']['gRecaptchaResponse']

s = session()

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 OPR/51.0.2830.26'            
          }

data = {'g-recaptcha-response': key}

response = s.post(URL, data=data, headers=headers)

print(response.status_code)
print(response.text)


