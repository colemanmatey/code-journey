# for statement
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, "has", len(word), "alphabets")


# range() function
for i in range(5):
    print(i)


# looping through a list using range() and len() functions
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
