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