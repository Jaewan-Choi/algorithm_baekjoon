n = int(input())

count = 0
for i in range(n):
    word_alphabet_list = list(input())

    sequential_duple_delete_list = []
    i = 0
    for word_alphabet in word_alphabet_list:
        if i == 0:
            sequential_duple_delete_list.append(word_alphabet)
            i += 1
        else:
            if sequential_duple_delete_list[i-1] != word_alphabet:
                sequential_duple_delete_list.append(word_alphabet)
                i += 1

    if len(sequential_duple_delete_list) == len(set(sequential_duple_delete_list)):
        count += 1

print(count)