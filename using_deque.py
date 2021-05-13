from collections import deque # double ended queue

def palindrome(word):
    dq = deque(word)
    # print(type(dq))
    while len(dq) > 1:
        if dq.popleft() == dq.pop():
            return True
        else:
            return False
    return True

if __name__ == '__main__':
    my_text = palindrome('any text')
    racecar = palindrome('racecar')
    radar = palindrome('radar')
    adam = palindrome('madam im adam')
    print(my_text, racecar, radar, adam)
