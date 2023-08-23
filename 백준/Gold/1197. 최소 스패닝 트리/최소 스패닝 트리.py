# 루트노드를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 노드를 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [i for i in range(1 + V)]  # 정점의 정보를 저장할 배열
info = [list(map(int, input().split())) for _ in range(E)]  # 간선과 가중치 정보를 저장하는 배열
info.sort(key=lambda x: x[2])  # 가중치에 따른 정렬
answer = 0

# 간선을 탐색하며 루트노드가 다르다면 추가
for s, e, w in info:
    if find(s) != find(e):
        union(s, e)
        answer += w

print(answer)
