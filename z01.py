a = [1, 2, 3, 4, 5, 6, 7]
min = a[0]
min_old = min
for x in a:
    if min > x:
        min_old=min
        min=x

print(min_old)