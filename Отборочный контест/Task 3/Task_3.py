import sys

def Task_3():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    
    safe = bytearray(n + 1)
    safe[0] = 1
    safe[n] = 1
    for i in range(k):
        x = int(data[idx]); idx += 1
        safe[x] = 1
    INF = n + 2
    dp = [INF] * (n + 1)
    dp[0] = 0
    
    for i in range(n + 1):
        if dp[i] >= INF:
            continue
        if i + 1 <= n and safe[i + 1] and dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
        if i + 2 <= n and safe[i + 2] and dp[i + 2] > dp[i] + 1:
            dp[i + 2] = dp[i] + 1
    
    if dp[n] >= INF:
        print(-1)
        return
    
    print(dp[n])
    dp_back = [INF] * (n + 1)
    dp_back[n] = 0
    for i in range(n - 1, -1, -1):
        if not safe[i] and i != 0:
            continue
        if i + 1 <= n and safe[i + 1] and dp_back[i + 1] < INF:
            dp_back[i] = min(dp_back[i], dp_back[i + 1] + 1)
        if i + 2 <= n and safe[i + 2] and dp_back[i + 2] < INF:
            dp_back[i] = min(dp_back[i], dp_back[i + 2] + 1)
    
    total = dp[n]
    path = []
    pos = 0
    while pos < n:
        nxt = pos + 1
        if nxt <= n and safe[nxt] and dp[pos] + 1 + dp_back[nxt] == total:
            path.append('1')
            pos = nxt
        else:
            path.append('2')
            pos += 2
    sys.stdout.write(''.join(path) + '\n')

Task_3()