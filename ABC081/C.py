from collections import Counter
from operator import itemgetter
import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))
c = np.array(sorted(Counter(A).items(), key=itemgetter(1), reverse=True))
a_to_replace = c[K:]
print(sum(a_to_replace[:,1]))