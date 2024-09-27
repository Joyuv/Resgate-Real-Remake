import json

def get_alphalist(rankdict:dict[str,int]) -> list:
    '''Função para pegar a lista de nomes do ranking removendo os números'''
    alphalist = []
    for namejones in rankdict:
        alphaname = ''
        for a in range(0,len(namejones)):
            if a == len(namejones)-1:
                break
            alphaname+= namejones[a]
        if alphaname not in alphalist:    
            alphalist.append(alphaname)
    return alphalist

def get_ocorrencias(name:str, rankdict:dict[str,int]) -> list: #nome da função está ruim, mudar depois
    namelist = []
    for namejones in rankdict.keys():
        auxname = ''
        for letra in range(len(namejones)-1):
            auxname+= namejones[letra]
        if auxname == name:
            namelist.append(namejones)
    return sorted(namelist)

def get_rankdecrescente(rankdict:dict[str,int]):
    '''Essa função ordena o ranking em ordem decrescente, da maior quantidade de pontos até a menor.

    - Parâmetros:
        - rankdict: É o arquivo ranking.json carregado e convertido em um dicionário python
    '''
    listavalues = sorted(rankdict.values(),reverse=True)
    dictdec = {}
    for pontos in listavalues:
        for name in rankdict:
            if rankdict[name] == pontos:
                dictdec.update({name:pontos})
    
    
    drank = {"jogadores":[], "pontos":[]}
    for player in dictdec:
        alphaplayer = ''
        for a in range(0,len(player)):
            if a == len(player)-1:
                break
            alphaplayer += player[a]
        drank['jogadores'].append(alphaplayer)
        drank['pontos'].append(str(dictdec[player]))
    return drank

def formatname(name:str, alphalist:list[str], namelist:list[str]) -> str: #bug em quando já tem 10 da mesma pessoa no ranking, quando isso ocorre a função coloca o nome como zagz10 e isso quebra tudo
    '''Essa função formata o nome do player para que esse nome seja colocado no json.

    - Descrição:
        Pega o nome e checa se ele está presente na lista de nomes que contém apenas letras, 
        caso não ocorra, este será o primeiro nomeado "nome0", caso contrário haverá uma checagem
        para alocar a esse nome o número de acordo com a quantidade do mesmo no ranking, e ajusta-lo
        caso haja uma diferença, por exemplo, ["zagz0", "zagz2"], nesse caso o nome retornado
        seria "zagz1", mas, caso a ordem esteja correta o nome retornado seria equivalente a soma do 
        maior número.
    
    - Parâmetros:
        - name: Nome que o player digitou na primeira tela
        - alphalist: Lista de nomes igual a name no **sem o número**
        - namelist: Lista de nomes igual a name no ranking **com o número**

    - Retorna:
        O nome formatado e pronto para ser colocado no arquivo json, por exemplo, "zagz5"
    '''
    if name not in alphalist:
        name += '0'
    else:
        if len(namelist) != 10:
            for a in range(0,len(namelist[0])):
                if namelist[0][a].isnumeric():
                    posnum = a
            mudou = False
            for a in range(len(namelist)-1,-1,-1):
                if not int(namelist[a][posnum]) == 0:
                    if int(namelist[a][posnum]) - int(namelist[a-1][posnum]) != 1:
                        name+=str(int(namelist[a][posnum])-1)
                        mudou = True
                        break
            if not mudou:
                name+=str(int(namelist[len(namelist)-1][posnum])+1)
        else:
            name = '?????'
    return name

def addranking(name: str, pontos:int, rankdict:dict[str,int]):
    '''Essa função checa se a quantidade de pontos do player é o suficiente para que ele seja  colocado no ranking, caso seja, o faz.
    
    - Parâmetros:
        - name: Nome já formatado pela função formatname()
        - pontos: A pontuação total do jogador
        - rankdict: É o arquivo ranking.json carregado e convertido em um dicionário python
    '''
    if len(rankdict) < 10:
        rankdict[name] = pontos
        with open('ranking.json', 'w') as rankwrite:
            json.dump(rankdict,rankwrite,indent=4)
    else:
        menor = {"nome":'irineu', "pontos":99999999999999}
        for player in rankdict:
            if rankdict[player] < menor['pontos']:
                menor['nome'] = player
                menor['pontos'] = rankdict[player]

        if pontos > menor['pontos']:
            if name != '?????':
                rankdict.pop(menor['pontos'])
                rankdict[name] = pontos
            else:
                rankdict[menor['nome']] = pontos
        with open('ranking.json', 'w') as rankwrite:
            json.dump(rankdict,rankwrite,indent=4)