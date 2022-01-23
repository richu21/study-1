import requests 

m = {'age' : 15}
t=requests.post('http://192.168.1.100:105/ins/hello',json=m)
print(t)
print(t.json())
print(t.json()["age"])

# t=requests.get('http://192.168.1.100:105')
# print(t)
# print(t.json())