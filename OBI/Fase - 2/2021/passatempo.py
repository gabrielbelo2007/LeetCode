# GPT - Analisar

def solve_puzzle(L, C, grid, row_sums, col_sums):
    from collections import defaultdict

    # Dicionário para armazenar os valores das variáveis
    variable_values = {}
    
    # Dicionário para contar a frequência das variáveis nas linhas e colunas
    variable_count_row = [defaultdict(int) for _ in range(L)]
    variable_count_col = [defaultdict(int) for _ in range(C)]
    
    # Preenchendo os dicionários de contagem
    for i in range(L):
        for j in range(C):
            variable = grid[i][j]
            variable_count_row[i][variable] += 1
            variable_count_col[j][variable] += 1
    
    # Laço até que todas as variáveis sejam resolvidas
    while len(variable_values) < L * C:
        # Verificar linhas
        for i in range(L):
            if len(variable_count_row[i]) == 1:
                var = next(iter(variable_count_row[i]))
                value = row_sums[i]
                for j in range(C):
                    if grid[i][j] in variable_values:
                        value -= variable_values[grid[i][j]]
                variable_values[var] = value
                for j in range(C):
                    variable_count_col[j][grid[i][j]] -= 1
                    if variable_count_col[j][grid[i][j]] == 0:
                        del variable_count_col[j][grid[i][j]]
                variable_count_row[i].clear()
        
        # Verificar colunas
        for j in range(C):
            if len(variable_count_col[j]) == 1:
                var = next(iter(variable_count_col[j]))
                value = col_sums[j]
                for i in range(L):
                    if grid[i][j] in variable_values:
                        value -= variable_values[grid[i][j]]
                variable_values[var] = value
                for i in range(L):
                    variable_count_row[i][grid[i][j]] -= 1
                    if variable_count_row[i][grid[i][j]] == 0:
                        del variable_count_row[i][grid[i][j]]
                variable_count_col[j].clear()
    
    # Ordenar e imprimir os resultados
    for variable in sorted(variable_values):
        print(variable, variable_values[variable])

if __name__ == "__main__":
    # Entrada
    L, C = map(int, input().split())
    grid = []
    row_sums = []
    for _ in range(L):
        *variables, row_sum = input().split()
        grid.append(variables)
        row_sums.append(int(row_sum))
    col_sums = list(map(int, input().split()))
    
    solve_puzzle(L, C, grid, row_sums, col_sums)