import requests

def get(url, params=None, **kwargs):
    return requests.get(url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return requests.post(url, data=data, json=json, **kwargs)

def put(url, data=None, **kwargs):
    return requests.put(url, data=data, **kwargs)

def delete(url, **kwargs):
    return requests.delete(url, **kwargs)

def patch(url, data=None, **kwargs):
    return requests.patch(url, data=data, **kwargs)

def head(url, **kwargs):
    return requests.head(url, **kwargs)

def options(url, **kwargs):
    return requests.options(url, **kwargs)

# Usage
url = 'https://example.com/api'

# GET
response = get(url, params={'key': 'value'})
print(response.json())

# POST
response = post(url, json={'key': 'value'})
print(response.json())

# PUT
response = put(url, data={'key': 'value'})
print(response.json())

# DELETE
response = delete(url)
print(response.json())

# PATCH
response = patch(url, data={'key': 'value'})
print(response.json())

# HEAD
response = head(url)
print(response.json())

# OPTIONS
response = options(url)
print(response.json())

