m, n = map(int, input().split())
num_squares = m * n
if num_squares % 2 == 0:
    max_dominoes = num_squares // 2 # // used for returning integer value not float 
else:
    max_dominoes = (num_squares - 1) // 2
print(max_dominoes)
