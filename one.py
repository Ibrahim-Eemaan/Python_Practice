import re

text = 'random string myname123@mysite.com some more reasonable text'

pattern = re.compile('[a-zA-z0-9]')

result = pattern.findall(text)

print(result)