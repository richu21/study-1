l = [1]
t= {
    'name' : 'abc',
    'age' : 25,
    'sex' : 'M',
    'txt' : l.copy()
}

if 'age' in t :
    print("hii")

t.pop('sex')
l.append(15)
m = l.copy()
m.append("hello")

print(t)
