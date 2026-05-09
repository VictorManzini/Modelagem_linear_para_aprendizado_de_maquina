import random
esportes = ["futebol", "vôlei", "basquete", "hockey", "tênis"]

for elementos in esportes:
    print(elementos)

adeptos = []
for i in range(0, len(esportes)):
    adeptos.insert(i, random.randrange(500, 2000))

for elementos in adeptos:
    print(elementos)