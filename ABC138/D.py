from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[b-1].append(a-1)
        edges[a-1].append(b-1)

    counts = [0]*N
    for _ in range(Q):
        p, x = map(int, input().split())
        counts[p-1] += x

    parent_nodes = deque()
    parent_nodes.append(0)
    visited_nodes = set()
    while parent_nodes:
        parent = parent_nodes.popleft()
        if parent in visited_nodes:
            continue
        visited_nodes.add(parent)
        for child in edges[parent]:
            if child in visited_nodes:
                continue
            counts[child] += counts[parent]
            parent_nodes.append(child)

    print(' '.join(list(map(str, counts))))

if __name__ == "__main__":
    main()