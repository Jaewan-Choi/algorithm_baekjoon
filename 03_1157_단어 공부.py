alphabet = input().upper()
alphabet_list = list(alphabet)

counts = {}
for i in alphabet_list:
    try: counts[i] += 1
    except: counts[i] = 1

biggest_count = 0
most_use_alphabet = ''
for key, count in counts.items():
    if count > biggest_count:
        biggest_count = count
        most_use_alphabet = key
    elif count == biggest_count:
        most_use_alphabet = '?'

print(most_use_alphabet)