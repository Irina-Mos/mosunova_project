text = input('Enter the text: ')
word = input('Enter the word: ')
text = text.lower()
word = word.lower()
word_list = []
while word != '':
    if word != '':
        word_list.append(word)
        word = input('Enter the word: ')
        word = word.lower()
for i in range(0, len(word_list)):
    if word_list[i] in text:
        word_list[i] = text.upper()
print(word_list)
print(text)