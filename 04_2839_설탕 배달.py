N = int(input())

count = 0

def find3Quantity(N):
    global count

    if N < 5:
        count = -1
    else:
        i = N // 5
        for i in range(i, -1, -1):
            if (N - (i * 5)) % 3 == 0:
                count = i + (N - (i * 5)) // 3
                break
            else: count = -1

if N % 5 == 0:
    count = N // 5

elif N % 5 == 4:
    find3Quantity(N)

elif N % 5 == 3:
    count = (N // 5) + 1

elif N % 5 == 2:
    find3Quantity(N)

elif N % 5 == 1:
    find3Quantity(N)

print(count)