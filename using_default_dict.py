from collections import defaultdict

# we can declare a fn to use as a default

def no_idea():
    return 'unknown'

if __name__ == '__main__':
    menagerie = defaultdict(no_idea)
    menagerie['a'] = 'Abominable Snowman'
    menagerie['b'] = 'Basilisk'
    print(menagerie['z'])
    print(menagerie)
