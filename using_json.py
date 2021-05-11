import json

# here is a rather complex structure (a list of dict)
a = [{'name':'PC', 'cost':500, 'detail':{'a':'True', 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':'False', 'b':[9,8,7,6]}}]

# convert to json
a_j = json.dumps(a)

print(type(a_j), a_j)

# convert back to a structure
b = json.loads(a_j)
print(type(b), b)

# alternatives
import pickle
import datetime
now = datetime.datetime.utcnow()
p = pickle.dumps(now)
print(now, type(now), p, type(p))
# return to originl structure
n = pickle.loads(p)
print(n, type(n))