def cortar_var(tam_var, lista_p, memory):
    if tam_var == 0:
        return 0
    if memory[tam_var] != -1:
        return memory[tam_var]

    mejor_valor = 0
    for i in range(1, tam_var+1):
        valor = lista_p[i] + cortar_var(tam_var-i, lista_p, memory)
        if valor > mejor_valor:
            mejor_valor = valor

    memory[tam_var] = mejor_valor
    return mejor_valor

if __name__ == "__main__":
    lista_p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = int(input())
    memo = [-1] * (n+1)
    print(cortar_var(n, lista_p, memo))
