import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0] * (n + 2)
for _ in range(q):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r + 1] -= 1

for i in range(1, n + 1):
    cnt[i] += cnt[i - 1]

freq = sorted(cnt[1:n+1], reverse=True)
a.sort(reverse=True)

print(sum(x * y for x, y in zip(a, freq)))