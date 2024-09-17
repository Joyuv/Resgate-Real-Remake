import json

name = 'zagz'

with open('ranking.json','r') as filer:
    jf = json.load(filer)


listanames = []
for namejones in jf:
    alphaname = ''
    for a in range(0,len(namejones)):
        if a == len(namejones)-1:
            break
        alphaname += namejones[a]

    if alphaname == name:
        listanames.append(namejones)

listanames.sort()
print(listanames)
parou  = False
for a in range(0,len(listanames)):
    for b in range(0,len(listanames[a])):
        
        if b == len(listanames[a]) - 1:
            if int(listanames[a+1][b]) - int(listanames[a][b]) != 1:
                listanames.append(name+str(int(listanames[a+1][b])-1))
                parou = True
                break
    if parou:
        break
print(listanames)

#pega todos os zagz, organiza em ordem crescente pelos ultimos numeros e então subtrai o maior pelo menor
#se o resultado for diferente de 1, então name1 vai ser 1 numero abaixo do maior