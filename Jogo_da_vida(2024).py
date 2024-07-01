dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

[n, q] = [int(x) for x in input().split()]  # Conventer input com + de 1 elemento em int e ja atribuindo a outras variaveis
state = [['0'] * n for _ in range(n)]  # Criar listas em sequencia
new_state = [['0'] * n for _ in range(n)]
for i in range(n):
  input_line = input()
  for j in range(n):
    state[i][j] = input_line[j]

def in_bounds(x, y): 
  return min(x, y) >= 0 and max(x, y) < n  # min (menor valor entre valores) e max (maior valor entre valores)

def count_alive_neighbors(x, y):
  alive = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if in_bounds(nx, ny) and state[nx][ny] == '1':
      alive += 1
  return alive

def step():
  for i in range(n):
    for j in range(n):
      alive_neighbors = count_alive_neighbors(i, j)
      new_state[i][j] = state[i][j]
      if state[i][j] == '0' and alive_neighbors == 3:
        new_state[i][j] = '1'
      if state[i][j] == '1' and (alive_neighbors < 2 or alive_neighbors > 3):
        new_state[i][j] = '0'
  for i in range(n):
    for j in range(n):
      state[i][j] = new_state[i][j]

print()
while q > 0:
  step()
  q -= 1
for i in range(n):
  print(''.join(state[i]))

