# for문

# for x in iterable 객체:
#   ---

for i in range(5):
    print(i, end=" ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10 2칸씩
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 1 ~ 10 까지 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"sum = {tot}")

print(sum(range(1, 11)))

s = "hi한글"

for c in s:
    print(c, end=" ")

print(len(s))

# 구구단 출력
# 2 * 1 = 2     2 * 2 = 4   2 * 3 = 6 ...

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:2d}", end="   ")
    print()