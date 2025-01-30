import requests

def request_sample(method):
    url = "http://httpbin.org/" + method
    response = requests.request(method, url)
    return response.json()

# GET
get_response = request_sample("get")
print(get_response)

# POST
post_response = request_sample("post")
print(post_response)

# PUT
put_response = request_sample("put")
print(put_response)

# DELETE
delete_response = request_sample("delete")
print(delete_response)
