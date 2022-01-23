import requests 

t=requests.post('http://192.168.1.101:105/ins')
print(t)
print(t.json())