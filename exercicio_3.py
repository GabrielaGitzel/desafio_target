import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


# print(dados)

menor = 0
atual = 0
maior = 0
fat_total = 0
dias_fat = 0

for i in dados:
  #  print(i['valor'])
  fat_total = i['valor'] + fat_total
  dia = i['dia']
  atual = i['valor']
  if dia == 1:
      menor = atual
      maior = atual
  if atual > 0:
      dias_fat = dias_fat + 1
  if atual < menor:
      menor = atual
  if atual > maior:
      maior = atual

media = fat_total/dias_fat
dias_fat_maior = 0

for i in dados:
    if i['valor'] > media:
        dias_fat_maior = dias_fat_maior + 1

print("O menor valor de faturamento ocorrido em um dia do mês foi de R$ {:.2f}.".format(menor))
print("O maior valor de faturamento ocorrido em um dia do mês foi de R$ {:.2f}".format(maior))
print("{} dias no mês em que o valor de faturamento diário foi superior à média mensal.".format(dias_fat_maior))