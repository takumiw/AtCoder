import sys
readline = sys.stdin.readline
import networkx as nx
from networkx.algorithms import bipartite

def main():
    N = int(readline())
    R = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    B = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]

    g = nx.Graph()  # 空の無向グラフを作成
    g.add_nodes_from([i for i in range(N)], bipartite=0)
    g.add_nodes_from([N + i for i in range(N)], bipartite=1)
    edge = []
    for i, (a, b) in enumerate(R):
        for j, (c, d) in enumerate(B):
            if a < c and b < d:
                g.add_edge(i, N+j, weight=1)

    d = nx.max_weight_matching(g)
    print(len(d))

if __name__ == '__main__':
    main()