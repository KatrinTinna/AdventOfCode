id_ranges = input().split(",")

result = 0
for id_range in id_ranges:
    id_range = id_range.split("-")
    first = int(id_range[0])
    last = int(id_range[1])
    for i in range(first, last + 1):
        if len(str(i)) % 2 != 0:
            continue
        middle = len(str(i)) // 2
        i = str(i)
        if i[0:middle] == i[middle : len(i)]:
            result += int(i)


print(result)
