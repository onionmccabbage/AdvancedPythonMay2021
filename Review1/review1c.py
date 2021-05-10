import requests

def getInfo():
    response = requests.get('http://jsonplaceholder.typicode.com/users')
    print(response.text)

def user_range(first=1, last=10):
    # check first and last are within bounds
    number = first
    while number <= last:
        response = requests.get('http://jsonplaceholder.typicode.com/users/{}'.format(number))
        yield response.text
        number += 1

if __name__ == '__main__':
    users = user_range(1,4)
    for i in users:
        print(i)

    users2 = user_range()
    print( 'Next user: {}'.format(users2.__next__()) ) 
    print( 'Next user: {}'.format(users2.__next__()) ) 
