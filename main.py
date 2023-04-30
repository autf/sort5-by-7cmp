from itertools import combinations, islice, permutations
from math import comb, perm

count = lambda iterable: sum(1 for _ in iterable)

Idx = range(5)
allEdges = lambda: combinations(Idx, 2)


def edges7in10():
    yield from combinations(allEdges(), 7)


assert count(combinations(Idx, 2)) == comb(5, 2) == 10
assert count(edges7in10()) == comb(10, 7) == 120
# print(*combinations(range(5), 2))
# print(*islice(edges7in10(), 10), sep='\n')


def blackBoxes():
    values = ((i + 1) * 10 for i in Idx)  # to distinguish from indices
    yield from permutations(values)


assert count(blackBoxes()) == perm(5) == 120
# print(*blackBoxes(), sep='\n')
# print(*islice(blackBoxes(), 10), sep='\n')


def isThisOne(E) -> bool:
    for V in blackBoxes():
        less = [[] for _ in Idx]  # if i -> j: j in less[i]
        for i, j in E:
            if V[i] > V[j]:
                less[i].append(j)
            else:
                less[j].append(i)
        # print(*less, sep='\n')
        # raise SystemExit

        def hasPath(i, j):
            assert V[i] > V[j]
            todo = [i]
            done = [False] * len(Idx)
            done[i] = True
            while todo:
                x = todo.pop()
                for y in less[x]:
                    if y == j:
                        return True
                    if not done[y]:
                        todo.append(y)
                        done[y] = True
            return False

        for i, j in allEdges():
            if V[i] < V[j]:
                i, j = j, i
            if not hasPath(i, j):
                return False
        return True


def findAll():
    for E in edges7in10():
        if isThisOne(E):
            yield E


def printDotGraph(E):
    print("graph {")
    for i, j in E:
        print(f"    {i} -- {j};")
    print("}")


ans = [*findAll()]
print("found:", len(ans))
n = 1
for E in ans[:n]:
    print(*E)

# printDotGraph(next(findAll()))
