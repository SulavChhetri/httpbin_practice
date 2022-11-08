import requests
import json

payload = {
    'name': 'Sulav',
    'surname': 'Thapa'
}

files = {
    'file': open('myfile.csv', 'rb')
}
url = 'https://httpbin.org/post'
r = requests.post(url)
assert r.status_code == 200

cookie_url ='https://httpbin.org/cookies'
rc =requests.get(cookie_url)
assert json.loads(rc.text)=={
    "cookies": {}
}

cookie_del_url = 'https://httpbin.org/cookies/delete?freeform=anotherone'
rcd = requests.get(cookie_del_url)
assert json.loads(rcd.text) == {
    "cookies": {}
}

cookie_set = 'https://httpbin.org/cookies/set?freeform=sulav'
rcs = requests.get(cookie_set)
assert json.loads(rcs.text) == {
    "cookies": {
        "freeform": "sulav",
    }
}

cookie_name_set = 'https://httpbin.org/cookies/set/name/sulavthapa'
rcns = requests.get(cookie_name_set)
assert json.loads(rcns.text) == {
    "cookies": {
        "name": "sulavthapa"
    }
}
