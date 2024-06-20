import sys

input = sys.stdin.readline

K, L = map(int, input().split())

lecture = dict()

for i in range(L):
    num = input().strip()
    if num in lecture:
        del lecture[num]
    lecture[num] = i

lecture = sorted(lecture.items(), key=lambda x: x[1])
for i in range(len(lecture)):
    print(lecture[i][0])
    if i == K - 1:
        break