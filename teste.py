ranking = {
    "zag": 9,
    "zgz": 5,
    "edu": 4,
    "zaz": 2,
    "zuz": 7,
    "lui": 8,
    "ban": 3,
    "das": 10,
    "kkk": 6,
    "fim":1
}

listanova = sorted(ranking.values(),reverse=True)

dicknovo = {}

for b in listanova:
    for key in ranking:
        if ranking[key] == b:
            dicknovo.update({key:b})
print(ranking)
print(dicknovo)