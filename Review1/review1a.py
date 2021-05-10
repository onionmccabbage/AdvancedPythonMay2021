number = int(input('Enter number : '))
print('Using Map')
roots = map(lambda x: x**0.5, range(1,number+1))
for root in roots:
    print (root)

print('Using List comprehension')
roots = [x**0.5 for x in range(1,number+1)]
for root in roots:
    print (root)

print('Using Generator comprehension')
roots = (x**0.5 for x in range(1,number+1))
for root in roots:
    print (root)
