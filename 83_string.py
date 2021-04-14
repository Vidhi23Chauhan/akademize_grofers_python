message = "This is a lorem ipsum text."

print(message)
print(message[0], message[1], message[2], message[3])
print(len(message))
print(message[5:15])
print(message[5:])
print(message[:15])

print("Index of first space: ", message.index(' '))

first_space_index = message.index(' ')
print("Text after first space:", message[first_space_index + 1:])

last_space_index = message.rindex(' ')
print("Text after last space:", message[last_space_index + 1:])

words = message.split(" ")
print(words)


"""
This is a lorem ipsum text.
T h i s
27
is a lorem
is a lorem ipsum text.
This is a lorem
Index of first space:  4
Text after first space: is a lorem ipsum text.
Text after last space: text.
['This', 'is', 'a', 'lorem', 'ipsum', 'text.']

"""