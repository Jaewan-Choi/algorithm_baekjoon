first_num = int(input())

num = first_num

if num >= 10:
    left_num = int(str(num)[0])
    right_num = int(str(num)[1])
    left_plus_right_num = left_num + right_num
    if left_plus_right_num >= 10:
        num = int(str(right_num) + str(left_plus_right_num)[1])
    else:
        num = int(str(right_num) + str(left_plus_right_num))
else:
    num = int(str(num) + str(num))

n = 1
while num != first_num:
    if num >= 10:
        left_num = int(str(num)[0])
        right_num = int(str(num)[1])
        left_plus_right_num = left_num + right_num
        if left_plus_right_num >= 10:
            num = int(str(right_num) + str(left_plus_right_num)[1])
        else:
            num = int(str(right_num) + str(left_plus_right_num))
    else:
        num = int(str(num) + str(num))

    n += 1

print(n)