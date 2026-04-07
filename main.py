lista_notas = []

for num in range(3):
    nota = float(input('Digite uma nota: '))
    lista_notas.append(nota)

def calculo_notas(lista):
    soma = 0
    for n in lista:
        soma += n
    media = soma / len(lista)
    return media

def verificar_media(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

media_final = calculo_notas(lista_notas)
situacao = verificar_media(media_final)

print(f'Notas: {lista_notas}')
print(f'Média: {media_final:.2f}')
print(f'Situação: {situacao}')