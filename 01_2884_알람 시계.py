from datetime import timedelta

hr, min = map(int, input().split())
a = timedelta(hours=hr, minutes=min)
b = timedelta(minutes=45)
c = str(a-b)

if 'day' in c:
    c = c.split(',')[1].strip()

result_hr = c.split(':')[0]
result_min = c.split(':')[1]

print(f"{int(result_hr)} {int(result_min)}")