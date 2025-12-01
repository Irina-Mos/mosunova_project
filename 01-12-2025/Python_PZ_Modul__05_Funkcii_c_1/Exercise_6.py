def prime(num):
    if num != 1 and num != 0:
        counter = 0
        for i in range(2, num):
            if num % i == 0:
                counter += 1
        if counter == 0:
            return True
        else:
            return False
    else:
        print('Enter a number other than 0 or 1.')

a = prime(263)
print(a)