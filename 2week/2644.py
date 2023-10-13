# 촌수를 구하시오.
# 나의 위치에서 하나씩 멀어질때마다 1촌씩 늘어남.
# 첫째줄에는 전체 사람의 수가 N 입력됨.
# 둘째줄 촌수 계산해야 하는 서로 다른 두사람 S, E .


def dfs(S, E):
    q = []
    # 안했으면 0, 방문 했으면 1씩증가
    visit = [0]*(N+1)
    q.append(S)

    # q가 빈배열이 될때까지
    while q:
        c = q.pop(0)
        if c == E:
            return visit[E]

        for n in graph[c]:
            if 0 == visit[n]:
                q.append(n)

                # 노드간 거리가 1씩 늘어나도록
                visit[n] += visit[c] + 1

    return -1


# 총 인원수
N = int(input())
# 주어진 숫자 사이의 촌수
S, E = map(int, input().split())
# 총 노드의 연결 선
M = int(input())

# 0번에는 데이터가 안들어 가기 때문에 n+1을 한다.
# 해당 숫자와 연결되어 있는 다른 숫자들의 모임
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


result = dfs(S, E)

print(result)
