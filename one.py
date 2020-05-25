word_count = {
    'l': 3,
    'like': 1,
    'the': 3
}

#list.item()
print(word_count.items())
print(list(word_count.items()))

#list.keys()
print(word_count.keys())

#list.value()
print(word_count.values())

#list.remove()
word_count.pop('l')
print(word_count)

#pop item
word_count.popitem
print(word_count)


#MUTABILITY

#lists[] are mutable
#tuples() are immutable
#t = (1,2,3) this is unchangeable, just like rock
#l = [1,2,3] this is changeable

#IMMUTABLES
#tuples, floats, booleans

#MUTABLE
#list, dictionaries, ordereddict



#REGEX - REGEX - REGEX

import re

text = 'random string. myname.@gmail.com'

pattern = re.compile('[@]')

result = pattern.search(text)

print(result)
