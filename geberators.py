x = range(12)

def my_range(n):
    count = 0
    while count < n:
        count += 1
        yield count


for x in my_range(100):
    print(x)
