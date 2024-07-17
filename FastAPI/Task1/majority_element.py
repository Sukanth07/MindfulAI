from collections import defaultdict

def majority_element(string: str) -> int:
    s = list(map(int, string.strip().split(',')))
    n = len(s)
    hmap = defaultdict(int)
    maxi = val = 0
    for i in s:
        hmap[i] += 1
        if hmap[i] > maxi:
            maxi = hmap[i]
            val = i
    return val