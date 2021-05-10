import requests

def getInfo():
    response = requests.get('http://jsonplaceholder.typicode.com/users/7')
    print(response.text)

if __name__ == '__main__':
    getInfo()