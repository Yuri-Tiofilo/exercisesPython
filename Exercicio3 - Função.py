def menorVetor(vet):
    menor = vet[0]
    for i in range (0,5):
        if vet[i] < menor:
            menor = vet[i]
    return menor
vetor = []
for i in range(0, 5):
    vetor.append(int(input('Informe um numero: ')))
m = menorVetor(vetor)
print(m)