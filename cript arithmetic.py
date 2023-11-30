from itertools import permutations
def solve_cryptarithmetic():
    for perm in permutations('0123456789', 8):
        s, e, n, d, m, o, r, y = perm
        if s == '0' or m == '0':
            continue
        send = int(s + e + n + d)
        more = int(m + o + r + e)
        money = int(m + o + n + e + y)
        if send + more == money:
            return f"SEND: {send}, MORE: {more}, MONEY: {money}"
    return "No solution found"
print(solve_cryptarithmetic())