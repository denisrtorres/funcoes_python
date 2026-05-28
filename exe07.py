def fatorial(n):
    res = 1
    for i in range (1,n+1):  #Intervalo aberto, então é obrigatório colocar "+1", pq ele para no N e não o conta.
        res = res * i
    return res

print(fatorial(5))