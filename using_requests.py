import requests
import sys

def getInfo(category, id):
    url = 'http://jsonplaceholder.typicode.com/{}/{}'.format(category, id)
    response = requests.get(url)
    # we can receive json
    d = response.json() # this CONVERTS the json to a dict
    # we also have it as plain text
    t = response.text # this is plain text
    print(type(t), type(d))
    # access the geo members
    print('Lat: {} Lon: {}'.format(d['address']['geo']['lat'], d['address']['geo']['lng'] ))

if __name__ == '__main__':
    # check if there were arguments - provide defaults
    if len(sys.argv) > 1:
        category = sys.argv[1] # users, posts, photos, albums, todos
        id = sys.argv[2] # 1, 2, 3...
    else:
        category = 'users'
        id=1
    # pass arguments to the request
    getInfo(category, id)