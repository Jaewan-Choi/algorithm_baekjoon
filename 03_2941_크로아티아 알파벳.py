croatian_alphabets = input()
combination_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for combination_alphabet in combination_alphabets:
    croatian_alphabets = croatian_alphabets.replace(combination_alphabet, '0')
print(len(croatian_alphabets))