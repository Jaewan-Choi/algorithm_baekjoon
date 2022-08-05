a, b, v = map(int, input().split())
d = (v-b)/(a-b)
if d != int(d):
    print(int(d+1))
else:
    print(int(d))