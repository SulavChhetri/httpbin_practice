import requests
import json


url = 'https://httpbin.org/post'
r = requests.post(url)
assert r.status_code == 200

cookie_url ='https://httpbin.org/cookies'
rc =requests.get(cookie_url)
assert rc.status_code == 200
assert json.loads(rc.text)=={
    "cookies": {}
}

cookie_del_url = 'https://httpbin.org/cookies/delete?freeform=anotherone'
rcd = requests.get(cookie_del_url)
assert rcd.status_code == 200
assert json.loads(rcd.text) == {
    "cookies": {}
}

cookie_set = 'https://httpbin.org/cookies/set?freeform=sulav'
rcs = requests.get(cookie_set)
assert rcs.status_code == 200
assert json.loads(rcs.text) == {
    "cookies": {
        "freeform": "sulav",
    }
}

cookie_name_set = 'https://httpbin.org/cookies/set/name/sulavthapa'
rcns = requests.get(cookie_name_set)
assert rcns.status_code == 200
assert json.loads(rcns.text) == {
    "cookies": {
        "name": "sulavthapa"
    }
}
