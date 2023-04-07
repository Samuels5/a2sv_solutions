n, m, a = map(int, input().split())

num_rows = n // a
if n % a != 0:
    num_rows += 1

num_cols = m // a
if m % a != 0:
    num_cols += 1

num_flagstones = num_rows * num_cols

print(num_flagstones)