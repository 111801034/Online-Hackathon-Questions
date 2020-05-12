from operator import itemgetter
from collections import Counter
from collections import deque
import queue as Q
import math
import copy as c

def solution():
    # Write your code here
    NM = list(map(int, input().rstrip().split()))
    n = NM[0]
    m = NM[1]
    players = []
    for _ in range(n):
        player = list(map(int, input().rstrip().split()))
        players.append(player)
    sports = [i+1 for i in range(m)]
    sports_hash = {}
    for ele in sports:
        sports_hash[ele] = 0
    ans = n
    while(len(sports_hash.keys())>1):
        for i in range(n):
            for j in range(m):
                if(players[i][j] in sports_hash.keys()):
                    sports_hash[players[i][j]]+=1
                    break
        ma = -math.inf
        for key in sports_hash.keys():
            if(sports_hash[key]>ma):
                ma = sports_hash[key]
                max_key = key
        ans = min(ans, sports_hash[max_key])
        del sports_hash[max_key]
        for key in sports_hash.keys():
            sports_hash[key] = 0
    print(ans)

solution()
