import re
text = 'Today I drink 4 couples of coffee. Yesterday was 6.'

pattern = re.compile(r"[\w\s]*")
val = re.finditer(pattern, text)
for i in val:
    print(i)

pattern = re.compile(r"[\w]{5}")
val = re.search(pattern, text)
print(val.group())

pattern = re.compile(r"[\w]{5}")
val = re.finditer(pattern, text)
for i in val:
    print(i)

pattern = re.compile(r"[\w]{0,1}")
val = re.search(pattern, text)
print(val.group())

pattern = re.compile(r"[\w]{0,1}")
val = re.finditer(pattern, text)
for i in val:
    print(i)
