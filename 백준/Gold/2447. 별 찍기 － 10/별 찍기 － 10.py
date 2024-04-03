import sys
sys.setrecursionlimit(10**6)

def star(length):
    if length == 1:
        return ['*']

    stars = star(length // 3)
    board = []

    for s in stars:
        board.append(s * 3)
    for s in stars:
        board.append(s + ' ' * (length // 3) + s)
    for s in stars:
        board.append(s * 3)
    return board

n = int(input())
print('\n'.join(star(n)))