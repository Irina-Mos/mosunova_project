text = input('Enter the text : ')
# hi! nice to meet you! my name is John Smith. i am 19 and a student in college. i go to college in New York. my favorite courses are Geometry, French, and History. english is my hardest course. my professors are very friendly and smart. it’s my second year in college now. i love it!
# 1
new_text = text[0].upper()
new_text += text[1]
for i in range(1, len(text) - 1):
    a = text[i - 1]
    if a == '.' or a == '!' or a == '?':
        new_text += text[i + 1].upper()
    else:
        new_text += text[i + 1]
print(new_text)
# 2
counter_digit = 0
for i in range(0, len(text)):
    n = text[i]
    if n.isdigit():
        counter_digit += 1
print('There are', counter_digit, 'digits in the text.')
# 3
counter_ex = 0
for i in range(0, len(text)):
     if text[i] == '!':
        counter_ex += 1
print('There are', counter_ex, 'exclamation marks in the text.')
# 4
counter_punc = 0
for i in range(0, len(text)):
    n = text[i]
    if n.isdigit() == False and n.isalpha() == False and n != ' ':
        counter_punc += 1
print('There are', counter_punc, 'punctuation marks in the text.')
