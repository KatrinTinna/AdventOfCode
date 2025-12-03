import sys

data = sys.stdin.read().strip()


result = 0
current = 50

for turn in data.splitlines():
    rotation = turn[0]
    num = int(turn[1:])
    if rotation == "R":
        current += num
    else:
        current -= num
    if current % 100 == 0:
        result += 1


print("Result: ", result)
