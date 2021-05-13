# zip in Python is nothing to do with compression or archives

days = ('Mon', 'Tue', 'Wed', 'Thur')
fruits = ['banana', 'orange', 'kiwi', 'Durian']
drinks = ('coffee', 'tea', 'water', 'milk')
afters = ['tiramasu', 'ice cream', 'pie', 'creme caramel']

j = zip(days, fruits, drinks, afters)

for d, f, dr, a in j:
    print('On {} I ate {} with {} followed by {}'.format(d, f, dr, a))