def min_contractions_to_palindrome(n, lst):
    # Use dois ponteiros para verificar a lista
    left = 0
    right = n - 1
    operations = 0

    while left < right:
        if lst[left] == lst[right]:
            left += 1
            right -= 1
            
        elif lst[left] > lst[right]:
            lst[right - 1] += lst[right]
            right -= 1
            operations += 1
            
        elif lst[left] < lst[right]:
            lst[left + 1] += lst[left]
            left += 1
            operations += 1

    return operations

# Leitura dos dados de entrada
n = int(input())
lst = list(map(int, input().split()))

# Chamada da função para obter o número mínimo de operações
result = min_contractions_to_palindrome(n, lst)

# Impressão do resultado
print(result)