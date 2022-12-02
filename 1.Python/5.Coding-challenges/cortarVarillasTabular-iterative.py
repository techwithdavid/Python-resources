def cortar_var(tam_var, lista_p):
    tabla = [0] * (tam_var+1)

    for varilla_actual in range(1, tam_var+1):
        mejor_valor = 0
        for i in range(1, varilla_actual+1):
            valor = lista_p[i] + tabla(varilla_actual-i)
            if valor > mejor_valor:
                mejor_valor = valor

        tabla[varilla_actual] = mejor_valor

    return tabla[tam_var]


if __name__ == "__main__":
    lista_p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = int(input())
    print(cortar_var(n, lista_p))
