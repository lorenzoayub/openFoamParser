def writingDict(dataList):
    
    # def createParentDictsList(lista, listaNiveis):
    #     parentsList = []
    #     for i in range(len(listaNiveis)):
    #         if listaNiveis[i] == 0:
    #             parentsList.append('None')
    #         if listaNiveis[i] > 0:


    def transformaEmDict(texto):
        dados = texto.split(' ')
        chave = dados[0]
        valor: str = ''
        for indice in range(1, len(dados)):
            valor = valor + dados[indice]
            if indice != len(dados) - 1:
                valor = valor + ' '
        
        # Remove "indentation spaces" and dot-comma
        valor = valor.lstrip().replace(';', '')
        return {chave: valor}
    

    listaNova = dataList 
    
    for i in range(len(listaNova)):
        if listaNova[i] != '{':
            if '{' in listaNova[i]:
                listaNova[i].remove('{')
                listaNova.insert(i+1, '{')
        elif listaNova[i] != '}':
            if '}' in listaNova[i]:
                listaNova[i].remove('}')
                listaNova.insert(i+1, '}')
    

    print(f'\nlistaNova = {listaNova}\n listaNova len = {len(listaNova)}\n')    

    

    # Create list with levels
    levelList: list = []
    actualLevel: int = 0
    
    for j in range(len(listaNova)):
        if listaNova[j] == '{':
            levelList.append(-1)
            actualLevel += 1
        elif listaNova[j] == '}':
            levelList.append(-1)
            actualLevel -= 1
        else:
            levelList.append(actualLevel)

    # Get maximum level
    levelMaximo: int = max(levelList)

    newDict = {}
    print(f'\n\nlevelList len: {len(levelList)}\n')
    # print(f'\n Nivel maximo: {levelMaximo}\n')
    for i in range(1,len(listaNova)):
        # print(f'levelList[i]: {levelList[i]}\tlevelList[i+1]: {levelList[i+1]}')
        if levelList[i-1] == 0 and levelList[i] == 0:
            newDict.update(transformaEmDict(listaNova[i-1]))
    return newDict
