n = 1
creator_list = []
while n <= 10000:
    numbers = list(str(n))
    sum_numbers = 0
    for number in numbers:
        sum_numbers += int(number)
    creator = n + sum_numbers
    creator_list.append(creator)
    n += 1

for i in range(1, 10000):
    if i in creator_list:
        pass
    else:
        print(i)