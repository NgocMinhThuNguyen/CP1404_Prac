word_count = {}
text = input("Text: ")
strings = text.split()

for string in strings:
    number_of_string = word_count.get(string, 0)
    word_count[string] = number_of_string + 1

strings = list(word_count.keys())
strings.sort()

max_length = max((len(string) for string in strings))
for string in strings:
    print("{:{}} : {}".format(string, max_length, word_count[string]))
