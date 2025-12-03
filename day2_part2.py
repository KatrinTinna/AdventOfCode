id_ranges = input().split(",")

result = 0
for id_range in id_ranges:
    id_range = id_range.split("-")
    first = int(id_range[0])
    last = int(id_range[1])
    for i in range(first, last + 1):
        i = str(i)
        for pattern_length in range(1, len(i)// 2 +1):
            flag = 1
            for x in range(0, len(i)- pattern_length, pattern_length):

                if i[x: x+ pattern_length ]  != i[x + pattern_length : x + 2*pattern_length ]:
                    flag = 0
                    break
            if flag == 1:
                result += int(i)
                break
            





print(result)
