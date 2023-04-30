from itertools import combinations, islice
from math import comb

def edges7in10():
    allEdges = combinations(range(5), 2)
    for sel in combinations(allEdges, 7):
        yield sel

assert sum(1 for _ in combinations(range(5), 2)) == comb(5, 2) == 10
assert sum(1 for _ in edges7in10()) == comb(10, 7) == 120
# print(*combinations(range(5), 2))
# print(*islice(edges7in10(), 10), sep='\n')
