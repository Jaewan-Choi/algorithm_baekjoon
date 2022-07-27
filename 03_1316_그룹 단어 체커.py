n = int(input())
word_list = []
i = 0
while i < n:
    word_list.append(input())
    i += 1

count = 0
for word in word_list:
    word_alphabet_list = list(word)

    sequential_duple_delete_word_alphabet_list = []
    i = 0
    for word_alphabet in word_alphabet_list:
        if i == 0:
            sequential_duple_delete_word_alphabet_list.append(word_alphabet)
            i += 1
        else:
            if sequential_duple_delete_word_alphabet_list[i-1] != word_alphabet:
                sequential_duple_delete_word_alphabet_list.append(word_alphabet)
                i += 1

    if len(sequential_duple_delete_word_alphabet_list) == len(set(sequential_duple_delete_word_alphabet_list)):
        count += 1

print(count)