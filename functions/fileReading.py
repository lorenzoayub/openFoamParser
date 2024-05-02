def readFile(path: str) -> list:
    

    def removeLineBreaks(lista):
        nova = []
        for j in range(len(lista)):
            if '\n' in lista[j]:
                nova.append(lista[j].replace('\n',''))
            else:
                nova.append(lista[j])
        return nova
    
    def removeEmptyElements(lista):
        nova = []
        for j in range(len(lista)):
            if lista[j] == '':
                pass
            else:
                nova.append(lista[j])
        return nova

    def removeComments(lista):
        nova = []
        for j in range(len(lista)):
            if '//' in lista[j]:
                nova.append(lista[j].split('//')[0])
            else:
                nova.append(lista[j])
        return nova
    with open(path) as arquivo:
        lines = arquivo.readlines()

        # Check if there is a header
        header = False
        if lines[0] == '/*--------------------------------*- C++ -*----------------------------------*\\\n':
            header = True
        
        if header:
            for i in range(len(lines)):
                if lines[i] == '\\*---------------------------------------------------------------------------*/\n':
                    break
        cleanLines = removeEmptyElements(removeComments(removeLineBreaks(lines[i+1::])))

    return cleanLines

