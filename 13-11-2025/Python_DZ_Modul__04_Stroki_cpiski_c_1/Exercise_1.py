text = input('Enter the text: ')
text = text.lower()
if text == text[::-1]:
    print('This is a paliandrom')
else:
    print('This is not a paliandrom')