import sys
from collections import defaultdict

def Task_4():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    items = []
    for i in range(n):
        for j in range(m):
            v = int(data[idx]); idx += 1
            items.append((v, i))
    
    items.sort()
    total = len(items)
    epoch_count = defaultdict(int)
    covered = 0
    best_range = float('inf')
    best_windows = []
    
    left = 0
    for right in range(total):
        val, ep = items[right]
        if epoch_count[ep] == 0:
            covered += 1
        epoch_count[ep] += 1
        
        while covered == n:
            rng = items[right][0] - items[left][0]
            if rng < best_range:
                best_range = rng
                best_windows = [(left, right)]
            elif rng == best_range:
                best_windows.append((left, right))
            
            lep = items[left][1]
            epoch_count[lep] -= 1
            if epoch_count[lep] == 0:
                covered -= 1
            left += 1
    best_sum = float('inf')
    best_selection = None
    
    for l, r in best_windows:
        selection = {}
        for k in range(l, r + 1):
            v, e = items[k]
            if e not in selection:
                selection[e] = v
        s = sum(selection.values())
        if s < best_sum:
            best_sum = s
            best_selection = sorted(selection.values())
    
    print(' '.join(map(str, best_selection)))

Task_4()