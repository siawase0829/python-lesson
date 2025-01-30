import requests

# GETリクエスト
res = requests.get('https://www.google.com')
print(res.status_code)

# POSTリクエスト
data = {'key': 'value'}
res = requests.post('https://www.httpbin.org/post', data=data)
print(res.status_code)

# JSONデータを送信する
import json
url = 'https://api.github.com/some-endpoint'
payload = {'some': 'data'}
res = requests.post(url, data=json.dumps(payload))
print(res.status_code)

# パラメータ付きGETリクエスト
res = requests.get('https://www.httpbin.org/get', params={'key': 'value'})
print(res.status_code)

# ヘッダー付きリクエスト
url = 'https://api.github.com/some-endpoint'
headers = {'user-agent': 'my-reddit-client'}
res = requests.get(url, headers=headers)
print(res.status_code)

# Cookie付きリクエスト
url = 'http://example.com/some-endpoint'
cookies = dict(sessionid='1234567890')
res = requests.get(url, cookies=cookies)
print(res.status_code)

# ファイルを送信する
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
res = requests.post(url, files=files)
print(res.status_code)

# JSONデータを受信する
import json
url = 'https://api.github.com/events'
res = requests.get(url)
print(res.json())

# ストリーミング
url = 'http://httpbin.org/stream/100'
res = requests.get(url, stream=True)
for line in res.iter_lines():
    print(line.decode('utf-8'))

# カスタムトランスポートアダプター
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

s = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
s.mount('https://', HTTPAdapter(max_retries=retries))

# SSL検証を無効にする
import requests
res = requests.get('https://naughty.cert.org/', verify=False)
print(res.status_code)

# プロキシ
import requests
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
res = requests.get('http://example.org', proxies=proxies)
print(res.status_code)

# Basic認証
import requests
from requests.auth import HTTPBasicAuth
res = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
print(res.status_code)

# Digest認証
import requests
from requests.auth import HTTPDigestAuth
res = requests.get('https://api.github.com/user', auth=HTTPDigestAuth('user', 'pass'))
print(res.status_code)

# OAuth1認証
import requests
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('client_key', client_secret='client_secret', resource_owner_key='resource_owner_key', resource_owner_secret='resource_owner_secret')
res = requests.get(url, auth=auth)
print(res.status_code)

# OAuth2認証
import requests
from requests_oauthlib import OAuth2Session
client_id = 'your_client_id'
client_secret = 'your_client_secret'
authorization_base_url = 'https://example.com/oauth/authorize'
token_url = 'https://example.com/oauth/token'
oauth = OAuth2Session(client_id, redirect_uri='your_redirect_uri')
authorization_url, state = oauth.authorization_url(authorization_base_url)
print('Please go to {} and authorize access.'.format(authorization_url))
authorization_response = input('Enter the full callback URL ')
token = oauth.fetch_token(token_url, client_secret=client_secret, authorization_response=authorization_response)
res = oauth.get('https://example.com/api/me')
print(res.status_code)

