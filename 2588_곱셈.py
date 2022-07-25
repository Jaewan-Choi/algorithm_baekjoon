a = int(input())
b = int(input())

def multiplication(a, b):
    b_list = [int(str(b)[2]), int(str(b)[1]), int(str(b)[0])]

    c_1 = b_list[0] * a
    c_2 = b_list[1] * a * 10
    c_3 = b_list[2] * a * 100

    result = f"{c_1}\n{c_2//10}\n{c_3//100}\n{c_1 + c_2 + c_3}"
    print(result)

multiplication(a, b)