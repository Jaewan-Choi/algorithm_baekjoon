prime_list = []

for num in range(2, 246912):
    cnt = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            cnt += 1
            break
    if cnt == 0:
        prime_list.append(num)

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in prime_list:
        if n < i <= n * 2:
            count += 1
        
    print(count)