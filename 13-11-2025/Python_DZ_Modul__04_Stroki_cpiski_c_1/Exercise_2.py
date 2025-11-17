text = input('Enter the text: ')
word = input('Enter the word: ')
text = text.lower()
word = word.lower()
word_list = []
new_text = text
while word != '':
    if word != '':
        word_list.append(word)
        word = input('Enter the word: ')
        word = word.lower()
word_list_re = word_list[:]
for i in range(0, len(word_list)):
    if word_list[i] in text:
        word_list_re[i] = word_list_re[i].upper()
        new_text = new_text.replace(word_list[i], word_list_re[i])
print(new_text)

