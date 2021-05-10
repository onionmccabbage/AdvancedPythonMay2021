def is_square(number):
    root = number**0.5
    check = int(number**0.5)
    return root == check

numbers = [3,12,6,16,13,4,33,9]
numbers_sq = list(filter(is_square, numbers))

for n in numbers_sq:
    print(n)