import json


l = {'hah':123,'ddd':222,'ccc':333}
print(type(l))
print((l.get('ccc')))
h = json.dumps(l)
print(type(h))
t = json.loads(h)
print(t.get('ddd'))


import yaml

# with open('ddd.yaml') as f:
#     data = yaml.Loader(f,Loader=yaml.CLoader)
#     print(data['login'])

with open('ddd.yaml') as f:
    data = yaml.load(f, Loader=yaml.CLoader)
    print(data['login']['user']['ele'])
