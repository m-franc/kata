text = "bonjour-hello-ohayou"
word_list = text.split("-")
new_word_list = []
for i in word_list:
    if (i != word_list[0]):
        i = i.capitalize()
    new_word_list.append(i)
camel_case_text = ''.join(new_word_list)
print(camel_case_text)