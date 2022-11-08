import requests

payload = {
    'name': 'Sulav',
    'surname': 'Thapa'
}

files = {
    'file': open('myfile.csv','rb')
}
url = 'https://httpbin.org/post'
r = requests.post(url,data=payload,files=files)
print(r.status_code)
print(r.text)
print(r.headers)

cookie_url ='https://httpbin.org/cookies'
rc =requests.get(cookie_url)
print(rc.text)
print(rc.headers)

cookie_del_url = 'https://httpbin.org/cookies/delete?freeform=cookie'
rcd=requests.get(cookie_del_url)
print(rcd.text)
print(rcd.headers)

cookie_set = 'https://httpbin.org/cookies/set?freeform=sulav'
rcs = requests.get(cookie_set)
print(rcs.text)
print(rcs.headers)

cookie_name_set = 'https://httpbin.org/cookies/set/name/sulavthapa'
rcns = requests.get(cookie_name_set)
print(rcns.text)
print(rcns.headers)