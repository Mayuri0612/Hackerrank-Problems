#journey to the moon Here this code is not very time efficient. I just tried it and except two test cases I was able to pass all the test cases

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    def DFS(u):
        visited.add(u)
        count = 1
        if u in ad_list:
            for v in ad_list[u]:
                if v not in visited:
                    count += DFS(v)
        return count

    conn_comp = []
    visited = set()
    ad_list = defaultdict(list)
    total = 0

    for u,v in astronaut:
        ad_list[u].append(v)
        ad_list[v].append(u)

    for i in range(0,n):
        if i not in visited:
            res = DFS(i)
            conn_comp.append(res)

    for i in range(0,len(conn_comp)):
        for j in range(i+1,len(conn_comp)):
            total += conn_comp[i] * conn_comp[j]
    return total






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
