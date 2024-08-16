def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (word.lower() in (root_word.lower() or other_words.lower())) or ((root_word.lower() or other_words.lower()) in word):
            same_words.append(word)
    return f'{same_words}'

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))