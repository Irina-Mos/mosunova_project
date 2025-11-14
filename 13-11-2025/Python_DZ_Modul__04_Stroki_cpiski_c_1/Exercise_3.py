text = input('Enter the text: ')
counter = 0
for i in range(1, len(text) + 1):
    a = text[i - 1]
    if a == '.' or a == '!' or a == '?':
        counter += 1
print('There are', counter, 'sentences in the text.')