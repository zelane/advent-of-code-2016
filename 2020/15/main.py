input = [16, 11, 15, 0, 1, 7]

x = input.pop()
seen = {v: i for (i, v) in enumerate(input)}

target = 30000000
for i in range(len(input), target - 1):
    s = seen.get(x)
    seen[x] = i

    x = 0
    if s is not None:
        x = i - s

print(x)


# 0
# 8
# 14
# 8
# 2
# 165
# 1811
# 15075
# 182867
# 623065
# 0
# 10
# 65
# 2095
# 16
# 94
# 2228
# 80680
# 814903
# 0
# 9
# 91
# 181
# 1023
# 7249
# 6368
# 76878
# 66861
# 1311263
# 0
# 10
# 19
# 184
# 5834
# 39203
# 148935
# 2083996
# 0
# 8
# 35
# 614
# 576
# 7998
# 86813
# 153058
# 1867414
# 0
# 9
# 27
# 1518
# 906
# 23793
# 173873
# 874677
# 0
# 8
# 17
# 476
# 6439
# 84939
# 381816
# 3164173
# 0
# 8
# 8
# 1
# 98
# 1405
# 45015
# 60927
# 959333
# 0
# 9
# 25
# 210
# 1536
# 35921
# 1910139
