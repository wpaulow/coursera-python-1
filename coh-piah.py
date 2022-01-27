import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto): # pega uma grande string e a divide em uma série de strings em uma lista, separadas pelos caracteres .!?
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca): # pega uma string e devolve uma lista de strings separadas pelos caracters ,:;
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def media_palavras(lista_palavras):
    tamanhoTotal = 0
    for i in range(0, len(lista_palavras)):
        tamanhoTotal += len(lista_palavras[i])
    mediaPalavras = tamanhoTotal / len(lista_palavras)

    return mediaPalavras


def type_token(lista_palavras):
    # retorna a relação Type-Token
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)


def hapax_legomana(lista_palavras):
    # retorna a relação Hapax Legomana
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)

    
def media_sentencas(sentencas):
    totalChar = 0
    lista = []
    for i in range(0, len(sentencas)):
        lista += separa_palavras(sentencas[i])
    for j in range(0, len(lista)):
        totalChar += len(lista[j]) 
    mediaSentencas = totalChar / len(sentencas)
        
    return mediaSentencas


def complex_sentenca(lenFr, lenSent):

    return lenFr / lenSent


def media_frases(frases):
    totalChar = 0
    for i in range(0, len(frases)):
        lista = separa_palavras(frases[i])
        for j in range(0, len(lista)):
            totalChar += len(lista[j])
        mediaFrases = totalChar / len(frases)
        
    return mediaFrases


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    total = 0
    similaridadeAB = 0
    for i in range(0, 6):
        total += abs(as_a[i] - as_b[i])
    similaridadeAB = total / 6
    
    return similaridadeAB # quanto menor o número, mais similar ao COH-PIAH o texto é


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
##    listaPalavras = separa_palavras(texto)
    listaPalavras = []
    sentencas = separa_sentencas(texto)
    frases = []
    for i in range(len(sentencas)):
        frases += separa_frases(sentencas[i])

    for i in range(len(frases)):
        listaPalavras += separa_palavras(frases[i])
    
    law = media_palavras(listaPalavras)
    rtt = type_token(listaPalavras)
    rlh = hapax_legomana(listaPalavras)
    las = media_sentencas(sentencas)
    cas = complex_sentenca(len(frases), len(sentencas))
    lap = media_frases(frases)
    
    return [law, rtt, rlh, las, cas, lap]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    isCopiah = False
    compara = compara_assinatura(calcula_assinatura(textos[0]), ass_cp)
    similaridades.append(compara)
    menorAss = compara
    indexMenorAss = 0
    for i in range(1, len(textos)):
        compara = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        similaridades.append(compara)
        if compara < menorAss:
            menorAss = compara
            print(compara)
            indexMenorAss = i

    indexTexto = indexMenorAss + 1
    return indexTexto

def main():
    ass_b = le_assinatura()
    txts = le_textos()
    nCohpiah = avalia_textos(txts, ass_b)
    print("O autor do texto " + str(nCohpiah) + " está infectado com COH-PIAH.")

main()
    












