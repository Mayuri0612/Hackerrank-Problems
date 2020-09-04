#Roads and libraries

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    def DFS(u):
        visited.add(u)
        count = 1
        if u in ad_list:
            for v in ad_list[u]:
                if v not in visited:
                    count += DFS(v)
                    #count += 1
        return count

    if c_road > c_lib:
        return c_lib*n

    conn_com = []
    ad_list = defaultdict(list)
    visited = set()
    total = 0
    for u, v in cities:
        ad_list[u].append(v)
        ad_list[v].append(u)

    #iterate trough all cities
    for i in range(1,n+1):
        if i not in visited:
            res = DFS(i)
            conn_com.append(res)
    #total += len(conn_com)*(c_lib) + (n -len(conn_com)) * c_road
    #return total
    return (len(conn_com)*(c_lib) + (n -len(conn_com)) * c_road ) 


