import requests

# URLの設定
url = 'https://example.com/api/data'

# HTTPメソッドを選択する (GET, POST, PUT, DELETEなど)
method = 'GET'

# Request Payloadの設定
data = {
    'key': 'value'
}

# User-Agentの追加
headers = {'User-Agent': 'Mozilla/5.0'}

# これは基本的な場合
response = requests.request(method, url, headers=headers)

# この場合はエラーを確認する必要があります。
if response.status_code != 200:
    print(f'Error {response.status_code}: {response.text}')
else:
    print(response.text)
