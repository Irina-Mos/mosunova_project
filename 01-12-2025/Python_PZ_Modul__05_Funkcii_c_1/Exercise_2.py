def odd(a, b):
    if a < b:
        for i in range(a, b + 1):
            if i % 2 != 0:
                print(i)
    else:
        for i in range(b, a + 1):
            if i % 2 != 0:
                print(i)
odd(10, 1)