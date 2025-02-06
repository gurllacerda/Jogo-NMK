# This is the Python script for your project
def eh_tabuleiro(arg):
    """
    Verifica se o parametro é um tabuleiro válido ou não e retorna TRue se for e FAlse se não for 
    Parâmetros:
    arg: tuplo

    Return:
    Boolean
    
    """
    if type(arg) !=tuple or len(arg) < 2 or len(arg) >100:
        return False
    
    else:
        for coluna in range(len(arg)):
            if type(arg[coluna]) != tuple or len(arg[coluna]) >= 100 or len(arg[coluna]) < 2 or len(arg[coluna]) != len(arg[coluna - 1]):
                return False
            else:
                for j in range(len(arg[coluna])):
                    if type(arg[coluna][j]) != int or -1 > arg[coluna][j] or 1 < arg[coluna][j]:
                        return False
    return True

def eh_posicao(arg):
    """
    Verifica se o parametro passado é um inteiro, maior que zero e menor que o numero máximo de posições possiveis 
    e retorna um boolean

    Parametros:
    num(inteiro): posição a ser validada

    return:
    retorna True se for uma posição possivel e False se for impossivel  

    """
    isPosition = False
    if type(arg) == int: 
        if arg > 0 and arg <= 100*100:
            isPosition = True 
    return isPosition

def transforma_tuplo(tuplo):
    """
    Função auxiliar que transforma um tabuleiro em um unico extenso tuplo

    parametros:
    tuplo(tuple): tabuleiro a ser transformado

    retorno:
    tuple: o tabuleiro convertido

    """
    
    tuploFinal = ()
    for linha in tuplo:
        for coluna in linha:
            tuploFinal += (coluna,)
    return tuploFinal

def verifica_tabuleiro_pos(tab,pos):
    """
    Função para verificar se é um tabuleiro e é uma posição retornando True se isso for verdadeiro 
    """
    return eh_tabuleiro(tab) and eh_posicao(pos)
        
def obtem_dimensao(tab):
    """
    Calcula a dimensão do tabuleiro

    parametros:
    tab(tuple): tuplo base para calculo das dimensões

    retorno:
    tuple: as dimensões do tabuleiro tab
    
    """
    quantidadeLinhas = 0 
    quantidadeColunas = 0
    if(eh_tabuleiro):
        for linha in range(len(tab)):
            quantidadeLinhas = linha + 1
            for coluna in range(len(tab[linha])):
                quantidadeColunas = coluna + 1

        tuplo_final = (quantidadeLinhas, quantidadeColunas)
        return tuplo_final

def obtem_valor(tab, pos):
    """
    obtem o valor real de uma posição dentro do tabuleiro

    parametros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): posição do tabuleiro 

    retorno:
    inteiro: o valor real da posição
    """

    numColunas = len(tab[0])
    linhaPosicao = (pos - 1) // numColunas 
    colunaPosicao = (pos-1) % numColunas

    return tab[linhaPosicao][colunaPosicao]


def obtem_coluna(tab, pos):
    """
    Obtem as  posições dos elementos pertencentes a coluna da posição especificada

    parametros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): posição do tabuleiro que vai servir de base para conseguir a coluna

    retorno:
    tuple: tuplo com as posições da coluna da posição especificada
    """
    tuplo_resposta = ()
    numColunas = len(tab[0]) 
    coluna = (pos - 1) % numColunas 
    primeiraPosicao = (coluna + 1) # primeiro elemento da coluna, como para fazer a divisão foi trabalhado em um indice 0, deve-se somar um a resposta
    tuplo_resposta = (primeiraPosicao,)
    while primeiraPosicao + numColunas <= len(tab) * numColunas:
        primeiraPosicao += numColunas #a cada volta do loop adiciona o numero de colnas ao valor, logo pegando o valor da linha abaixo
        tuplo_resposta += (primeiraPosicao,)
    return tuplo_resposta

        
def obtem_linha(tab, pos):
    """
    Obtem as posições dos elementos pertencentes a linha da posição especificada

    parametros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): posição do tabuleiro que vai servir de base para conseguir a linha

    retorno:
    tuple: Tuplo com as posições dos elementos pertencentes a linha da posição especificada
    
    """
    tuplo_resposta = ()
    numColunas = len(tab[0])
    linhaPosicao = (pos - 1) // numColunas 
    primeira_posicao_linha = (linhaPosicao * numColunas) + 1 
    for i in range(numColunas):
        tuplo_resposta += (primeira_posicao_linha+i,)

    return tuplo_resposta

def obtem_diagonais(tab, pos):
    """
    Obtem as posições dos elementos pertencentes as diagonais da posição especificada

    parametros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): posição do tabuleiro que vai servir de base para conseguir as diagonais

    retorno:
    tuple: Tuplo com dois tuplos:
                                tuplo[0] posições do elementos pertencentes a diagonal primária da posição especificada
                                tuplo[1] posições do elementos pertencentes a diagonal secundária da posição especificada
    """
    diagonal_primaria = ()
    diagonal_secundaria = ()
    posicaoVerdadeira = pos -1
    numLinhas = len(tab)
    numColunas = len(tab[0])
    linhaPosicao = (posicaoVerdadeira) // numColunas #determina a linha do elemento 
    colunaPosicao = (posicaoVerdadeira) % numColunas #determina a coluna do elemento 
    linP, colP = linhaPosicao, colunaPosicao

    while linP >= 0 and colP >= 0:
        posicao_linear = linP * numColunas + colP + 1 #lógica para cons3eguir a posição sem usar range(len(x))
        diagonal_primaria = (posicao_linear,) + diagonal_primaria
        linP -= 1
        colP -= 1


    linP = linhaPosicao + 1 #como no while acima eu ja consegui o elemento na [linhaPosicao][colunaPosicao], o elemento seguinte deve-se adicionar 1
    colP = colunaPosicao + 1
    while linP < numLinhas and colP < numColunas:
        posicao_linear = linP * numColunas + colP + 1 #formula de posicao linear para conseguir a posição na matriz que começa com 1 
        diagonal_primaria = diagonal_primaria + (posicao_linear,)
        linP += 1
        colP += 1 


    linS = linhaPosicao 
    colS = colunaPosicao 
    while linS >= 0 and colS < numColunas:
        # diagonal_primaria = (tab[linP][colP],) + diagonal_primaria
        posicao_linear = linS * numColunas + colS + 1 #formula de posicao linear para conseguir a posição na matriz que começa com 1 
        diagonal_secundaria = diagonal_secundaria + (posicao_linear,) 
        linS -= 1
        colS += 1

    linS = linhaPosicao + 1
    colS = colunaPosicao - 1
    while linS < numLinhas and colS >= 0:
        # diagonal_primaria = (tab[linP][colP],) + diagonal_primaria
        posicao_linear = linS * numColunas + colS + 1 #formula de posicao linear para conseguir a posição na matriz que começa com 1 
        diagonal_secundaria = (posicao_linear,) + diagonal_secundaria
        linS += 1
        colS -= 1

    tuplo_resposta = (diagonal_primaria, diagonal_secundaria)
    return tuplo_resposta 
    


def tabuleiro_para_str(tab):
    """
    Transforma um tuplo em uma string representando um tabuleiro

    Paramêtros:
    tab(tuple): tabuleiro a ser percorrido

    Retorno:
    string: Cadeia de caracteres que representa o tabuleiro

    """
    numLinhas = len(tab)
    numColunas = len(tab[0])
    string_resposta = ""

    for linha in range(len(tab)):
        for elemento in range(len(tab[linha])):
            if elemento != numColunas - 1 :    #elemento começa em 0
                if tab[linha][elemento] == 1:
                    string_resposta += "X---"
                elif tab[linha][elemento] == 0:
                    string_resposta += "+---"
                else:
                    string_resposta += "O---"
            elif elemento == numColunas -1:
                if tab[linha][elemento] == 1:
                    string_resposta += "X" 
                elif tab[linha][elemento] == 0:
                    string_resposta += "+"
                else:
                    string_resposta += "O"

                if linha != numLinhas -1:
                    string_resposta += "\n" + ("|   " * (numColunas-1)) + "|\n"
    return string_resposta

def eh_posicao_valida(tab, pos):
    """
    Verifica se a posição passada como parâmetro é uma posição pertencente as posições do tabuleiro

    tab(tuple): tabuleiro a ser percorrido
    pos(int): Posição que vai ser validada pela função

    retorno:
    Boolean: Se For uma posição do tabuleiro return True, senão retunr False
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos):
        tabuleiro = transforma_tuplo(tab)
        if not (pos <= len(tabuleiro)):
            return False
        else: 
            return True
    else:
        raise ValueError("eh_posicao_valida: argumentos invalidos") 
    
def eh_posicao_livre(tab, pos):
    """
    Verifica se uma posição pertencente ao tabuleiro está livre, ou seja, seu valor é 0

    Parâmetros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): Posição que vai ser validada pela função

    Retorno:
    Boolean: Se for uma posição livre, retorna True, senão retorna False
    """
    if not verifica_tabuleiro_pos(tab,pos) or not eh_posicao_valida(tab,pos):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    
    tabuleiro = transforma_tuplo(tab)
    if tabuleiro[pos -1 ] == 0:
        return True
    else:
        return False

def obtem_posicoes_livres(tab):
    """
    Retorna as posições livres em um tabuleiro onde o valor é 0.
    A função percorre o tabuleiro e identifica todas as posições onde o valor é 0,
    que indicam posições livres. A posição no tabuleiro é retornada como um índice
    linear baseado em uma numeração que começa em 1.


    Parâmetros:
    tab(tuple): Tabuleiro a ser percorrido

    Retorno:
    tuple: Tuplo com as posições do tabuleiro onde o valor é igual a 0
    """
    tuplo_resposta = ()
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    tabuleiro = transforma_tuplo(tab)
    for posicao in range(len(tabuleiro)):
        if tabuleiro[posicao] == 0:
            tuplo_resposta += (posicao + 1,)

    return tuplo_resposta

def obtem_posicoes_jogador(tab, num):
    """
    Obtem as posições do tabuleiro os quais tem seus valores iguais a "num"(sendo num um jogador, -1 ou 1)
    Parâmetros:
    tab(tuple): Tabuleiro a ser percorrido
    num(int): Valor que representa o jogador, peças brancas ou pretas

    Retorno:
    tuple: Tuplo com as posições do tabuleiros os quais seus valores são iguais a num
    """
    if not (eh_tabuleiro(tab)) or num != -1 and num != 1:
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    tuplo_resposta = ()
    tabuleiro = transforma_tuplo(tab)

    for posicao in range(len(tabuleiro)):
        if tabuleiro[posicao] == num:
            tuplo_resposta += (posicao + 1,)

    return tuplo_resposta

def obtem_posicoes_adjacentes(tab, pos):
    """
    Obtem as posições que são adjacentes a posição especificada, ou seja, pensando em uma matriz, as posições do quadrado em volta de pos
    
    Parâmetros:
    tab(tuple): tabuleiro a ser percorrido
    pos(int): Posição que vai servir de base para conseguir as posições adjacentes a ela

    Retorno:
    tuple: Um tuplo contendo as posições lineares adjacentes à posição fornecida.
    """
    if not (verifica_tabuleiro_pos(tab, pos) and eh_posicao_valida(tab,pos)):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    
    tuplo_final = ()
    posicaoVerdadeira = pos -1
    numLinhas = len(tab)
    numColunas = len(tab[0])
    linhaPosicao = (posicaoVerdadeira) // numColunas 
    colunaPosicao = (posicaoVerdadeira) % numColunas 
    
    if linhaPosicao > 0: #não estiver na linha superior
        if colunaPosicao > 0: #não estiver na linha mais a esquerda
            tuplo_final += (pos - numColunas - 1,)  
        tuplo_final += (pos - numColunas,)  
        if colunaPosicao < numColunas - 1: #não estiver na coluna mais a direita
            tuplo_final += (pos - numColunas + 1,)  

    if colunaPosicao > 0:#não estiver na coluna mais a direita
        tuplo_final += (pos - 1,)  
    if colunaPosicao < numColunas - 1: #não estiver na coluna mais a esquerda 
        tuplo_final += (pos + 1,)  

    if linhaPosicao < numLinhas - 1: #não estiver na linha mais abaixo do tabuleiro
        if colunaPosicao > 0: #não estiver na coluna mais a esquerda do tabuleiro
            tuplo_final += (pos + numColunas - 1,)  
        tuplo_final += (pos + numColunas,) 
        if colunaPosicao < numColunas - 1: #não estiver na coluna mais a direita do tabuleiro 
            tuplo_final += (pos + numColunas + 1,)  

    return tuplo_final

def distancia_chebyshev(posicaoCentral, pos2):
    #Função auxiliar
    """
    Obtem a distancia entre duas posições atraves da fórmula da distancia de Chebyshev utilizando as coordenadas da posição

    Parâmetros:
    posicaoCentral(tuple): Coordenadas da posição central do tabuleiro
    pos2(tuple): Coordenadas da posição que queremos calcular a distancia

    Retorno:
    int: A distância de Chebyshev entre as duas posições
    """
    """Calcula a distância de Chebyshev entre duas posições."""
    return max(abs(posicaoCentral[0] - pos2[0]), abs(posicaoCentral[1] - pos2[1]))

    #m = linhas, n = colunas

def distancia_manhatan(posicaoCentral,pos2):

    return abs(posicaoCentral[0] - pos2[0]) + abs(posicaoCentral[1] - pos2[1])


def ordena_posicoes_tabuleiro(tab, tup):
    """
    Ordena as posições no tabuleiro com base na distância de Chebyshev até o centro.
    Em caso de empate nas distâncias, a função ordena as posições numericamente.

    Parâmetros:
    tab (tuple): Tabuleiro a ser percorrido.
    tup (tuple): Um tuplo contendo as posições a serem ordenadas.

    Retorno:
    tuple: Um novo tuplo contendo as posições ordenadas pela distância ao centro do tabuleiro.
    """
    
    tabuleiro = transforma_tuplo(tab)
    numLinhas = len(tab)
    numColunas = len(tab[0])

    posicoes_unicas = () 
    for pos in tup:
        if pos not in posicoes_unicas:
            posicoes_unicas += (pos,)

    if type(tup) != tuple or len(posicoes_unicas) > len(tabuleiro) or not eh_tabuleiro(tab) or len(tup) == 0:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos") 

    # if len(tup) == 0 or len(tup) > len(tabuleiro):
    #     raise ValueError("ordena_posicoes_tabuleiro: tamanho de tup inválido")

    # Calcula a posição central do tabuleiro (usando coordenadas)
    posicao_central = (numLinhas // 2) * numColunas + (numColunas // 2) +1
    
    # Função auxiliar para converter uma posição no tabuleiro em coordenadas
    def pos_para_coordenadas(pos):
        linha = (pos - 1) // numColunas
        coluna = (pos - 1) % numColunas
        return (linha, coluna)
    
    def sort_key(pos): #Função que define a transformação de cada item para ordenar
        if eh_posicao_valida(tab,pos):
            # print(posicao_central, pos)
            # print(pos_para_coordenadas(pos))
            distancia_ao_centro = distancia_manhatan(pos_para_coordenadas(posicao_central), pos_para_coordenadas(pos))
        return distancia_ao_centro, pos
    
    return tuple(sorted(posicoes_unicas, key=sort_key)) #Objeto que vai ser ordenado, Função que transforma cada item do objeto antes de ordenar

tab = ((1,0,0,1),(-1,1,0,1),(-1,0,0,-1))
tuploPosicoes = ()
tabPosicoes = (1,2,3,4,5,6,7,8,9,10,11,12)

# print(tabPosicoes)

print(ordena_posicoes_tabuleiro(tab, tabPosicoes))

def marca_posicao(tab,pos,jog):
    """
    Marca uma posição no tabuleiro com o valor do jogador.
    
    Parâmetros:
    tab(tuple): Um tuplo de tuplos representando o tabuleiro de jogo.
    pos(int): A posição no tabuleiro que deve ser marcada (de 1 até o número de posições no tabuleiro).
    jog(int): O valor que representa o jogador (-1 ou 1), que será usado para marcar a posição.

    Retorno:
    tuple: Um novo tabuleiro (tuplo de tuplos) com a posição 'pos' marcada com o valor de 'jog'.
    """
    if not verifica_tabuleiro_pos(tab,pos) or not eh_posicao_valida(tab,pos) or not eh_posicao_livre(tab,pos):
        raise ValueError("marca_posicao: argumentos invalidos")
    
    tuplo_resposta = ()
    numLinhas = len(tab)
    numColunas = len(tab[0])
    pos0index = pos -1
    linhaPosicao = pos0index // numColunas
    colunaPosicao = (pos - 1) % numColunas

    for i in range(numLinhas):
        if i == linhaPosicao: #quando a linha do for == linha que a pos pertence
            nova_linha = ()
            for j in range(numColunas):
                if j == colunaPosicao:
                    nova_linha += (jog,) #se for coluna da posicao adiciona o valor
                else:
                    nova_linha += (tab[i][j],)#senão apenas copia o valor original
            tuplo_resposta += (nova_linha,)
        else:
            tuplo_resposta += (tab[i],)

    return tuplo_resposta   

def verifica_jogador(jog):
    """
    Verifica se o jogador(jog) especificado pode ser considerado como jogador, ou seja, ser -1 ou 1

    Parâmetros:
    jog(int): Valor a ser validado para ver se é jogador ou não

    Retorno:
    boolean: Se for jogador True, senão False
    
    """
    if type(jog) != int or (jog != -1 and jog != 1):
        return False
    return True

def verifica_k_linhas(tab,pos,jog,k):

    """
    Verifica se existe uma combinação de peças do jogador 'jog' em uma linha, coluna ou diagonal
    que contenha pelo menos 'k' peças consecutivas, incluindo a posição 'pos'.

    Parâmetros:
    tab(tuple): Tabuleiro a ser percorrido
    pos(int): Posição que vai ser validada pela função
    jog(int): Jogador o qual as peças vão ser validadas
    k(int): Número mínimo de peças consecutivas

    Return:
    boolean: Retorna True se houver pelo menos 'k' peças consecutivas do jogador 'jog' na linha, 
             coluna ou diagonais que incluam a posição 'pos'. Caso contrário, retorna False.
    
    """
    if type(k) != int or not int(k) > 0 or not verifica_tabuleiro_pos(tab, pos) or not eh_posicao_valida(tab, pos) or not verifica_jogador(jog) :
        raise ValueError("verifica_k_linhas: argumentos invalidos")

    indexsLinhaPosicao = obtem_linha(tab,pos)
    indexsColunasPosicao = obtem_coluna(tab,pos)
    indexDiagonaisPosicao = obtem_diagonais(tab,pos)
    def num_consecutivos(tup, jog):
        #função auxiliar para apanhar os valores iguais ao jogador e comparar com k
        # retorna True se o numero de peças iguais consecutivas for maior que k
        if tup is None or tup == ():
            return False
        listaValores = ()
        for elemento in range(len(tup)):
                listaValores += (obtem_valor(tab, tup[elemento]),)
        valor = obtem_valor(tab,pos)
        consecutivos = 0
        for i in range(len(listaValores)):
            if valor == jog:
                if listaValores[i] == jog:
                    consecutivos += 1
                else:
                    consecutivos = 0
                if consecutivos >= k:
                    return True
        
        return False

    return num_consecutivos(indexsColunasPosicao,jog) or num_consecutivos(indexsLinhaPosicao,jog) or  \
           num_consecutivos(indexDiagonaisPosicao[0],jog) or num_consecutivos(indexDiagonaisPosicao[1],jog)


def eh_fim_jogo(tab,k):
    """
    Verifica se algum dos jogadores venceu ou se não há mais expaços livres no tabuleiro
    Parâmetros:
    tab(tuple): Tabuleiro a ser validado
    k(int): Numero de peças minimos consecutivas que o jogador deve ter

    Retorno:
    boolean: Retorna True se um dos jogadores venceu ou 
             não tem mais espaçoes livres no tabuleiro e False caso contrário 
    """
    numLinhas = len(tab)
    numColunas = len(tab[0])
    if type(k) != int or k <= 0 or not eh_tabuleiro(tab) or len(tab) == 0 or k > numLinhas or k > numColunas:
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    
    if obtem_posicoes_livres(tab)==():
        return True
    
    for pos in range(1, numLinhas * numColunas + 1): #testa todas as posições posíveis do tabuleiro com 1 e -1
        if verifica_k_linhas(tab, pos, 1, k) or verifica_k_linhas(tab, pos, -1, k):
            return True
    
    return False


def escolhe_posicao_manual(tab):
    """
    Permite ao jogador escolher manualmente uma posição livre no tabuleiro para realizar sua jogada.

    Parâmetros:
    tab (tuple): Tabuleiro a ser percorrido

    Retorno:
    int: Retorna a posição escolhida pelo jogador, se for uma posição válida e livre. 
    """
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    
    posicao = input("Turno do jogador. Escolha uma posicao livre: ")


    
    if not posicao.isdigit():
        return escolhe_posicao_manual(tab)
    else:
        if eh_posicao_valida(tab,int(posicao)) and eh_posicao_livre(tab,int(posicao)):
                return int(posicao)
        else:
            return escolhe_posicao_manual(tab)

def escolhe_posicao_auto(tab,jog,k,lvl):
    """
    Faz com que o computador jogue em uma posição escolhida automaticamente,
    baseando em um nível de dificuldade
    Parâmetros:
    tab(tuple): O tabuleiro a ser percorrido
    jog(int): O número que representa o jogador atual (1 ou -1).
    k(int): O número de peças consecutivas necessárias para vencer o jogo.
    lvl(str): O nível de dificuldade da jogada automática. Pode ser:

    Retorno:
    int: A posição escolhida para jogar, representada como um número inteiro 
    """

    tabuleiro = transforma_tuplo(tab)
    numLinhas = len(tab)
    numColunas = len(tab[0])

    def pos_para_coordenadas(pos):
        linha = (pos - 1) // numColunas
        coluna = (pos - 1) % numColunas
        return (linha, coluna)
    

    if not eh_fim_jogo(tab, k):
        #normal: verificar para qual o maior L possivel menor ou igual a K tal que verificaklinhas seja true (verificar todos os L, sempre verificar se é maior que o anterior) 
        if lvl == "facil":
           return estrategia_facil(tab,jog)
                    
        if lvl == "normal":
            return estrategia_normal(tab,jog,k,numLinhas,numColunas)

def estrategia_facil(tab,jog):
    """
    Estratégia fácil para o computador escolher uma posição.

    Parâmetros:
    tab(tuple): O tabuleiro atual.
    jog(int): O jogador atual (1 ou -1).

    Retorno:
    int: A posição escolhida pelo computador.
    """
    listaPosicoesJogador = obtem_posicoes_jogador(tab, jog)
    posicoes_adjacentes = ()
    for i in listaPosicoesJogador:
        adjacentes = obtem_posicoes_adjacentes(tab,i)
        for elemento in range(len(adjacentes)): # percorre os elementos da lista das adjacentes
            if obtem_valor(tab, adjacentes[elemento]) == 0 and adjacentes[elemento] not in posicoes_adjacentes:
                posicoes_adjacentes += (adjacentes[elemento],)


    #não é a primeira posição livre, e sim a mais proxima do centro, por isso a ordenação de posições
    if posicoes_adjacentes:
        # if type(posicoes_adjacentes) == tuple and posicoes_adjacentes:
        posicoes_livres = ordena_posicoes_tabuleiro(tab, posicoes_adjacentes) #ordena as posições adjacentes livres 
        return posicoes_livres[0]  # retorna a primeira delas

    #se não tiver posicoes adjacentes livres joga na primeira posicao livre
    listaPosicoesLivres = obtem_posicoes_livres(tab)
    if listaPosicoesLivres:
        listaPosiceosLivresOrdenada = ordena_posicoes_tabuleiro(tab,listaPosicoesLivres)
        return listaPosiceosLivresOrdenada[0]

            
def estrategia_normal(tab, jog, k, nLinhas, nColunas):
    """
    Estratégia normal para o computador escolher uma posição.

    Parâmetros:
    tab(tuple): O tabuleiro atual.
    jog(int): O jogador atual (1 ou -1).
    nLinhas(int): Numero de linhas do tabuleiro
    nColunas(int): Número de colunas do tabuleiro

    Retorno:
    int: A posição escolhida pelo computador através da estratégia.
    """
    listaPosicoesLivre = obtem_posicoes_livres(tab)
    posicaoResposta = 0 
    maximoLPossivel = 0 
    
    
    for posicaoLivre in listaPosicoesLivre:
        tabuleiro_provisorio = cria_tabuleiro_provisorio(tab, posicaoLivre, jog, nLinhas, nColunas)#tabuleiro provisório com a posição livre sendo um jog
        # print()
        for L in range(1, k + 1):
            if verifica_k_linhas(tabuleiro_provisorio, posicaoLivre, jog, L):
                if L > maximoLPossivel:  # Atualiza se encontrar um L maior
                    maximoLPossivel = L
                    posicaoResposta = posicaoLivre

    # Se não encontrar uma jogada ótima para o próprio jogador, tenta bloquear o adversário
    if maximoLPossivel < k:
        adversario = -jog
        for posicaoLivre in listaPosicoesLivre:
            tabuleiro_provisorio = cria_tabuleiro_provisorio(tab, posicaoLivre, adversario, nLinhas, nColunas)
            for L in range(1, k + 1):
                if verifica_k_linhas(tabuleiro_provisorio, posicaoLivre, adversario, L):
                    if L > maximoLPossivel:
                        maximoLPossivel = L
                        posicaoResposta = posicaoLivre

   
    if posicaoResposta == 0 and listaPosicoesLivre:
        posicaoResposta = listaPosicoesLivre[0]

    return posicaoResposta 


def estrategia_normal(tab, jog, k, nLinhas, nColunas):
    """
    Estratégia normal para o computador escolher uma posição.

    Parâmetros:
    tab(tuple): O tabuleiro atual.
    jog(int): O jogador atual (1 ou -1).
    nLinhas(int): Numero de linhas do tabuleiro
    nColunas(int): Número de colunas do tabuleiro

    Retorno:
    int: A posição escolhida pelo computador através da estratégia.
    """
    listaPosicoesLivre = obtem_posicoes_livres(tab)
    posicoesPossiveis = ()  
    maximoLPossivel = 0 

    for posicaoLivre in listaPosicoesLivre:
        tabuleiro_provisorio = cria_tabuleiro_provisorio(tab, posicaoLivre, jog, nLinhas, nColunas)
        
        for L in range(1, k + 1):
            if verifica_k_linhas(tabuleiro_provisorio, posicaoLivre, jog, L): #simula um tabuleiro com a posição livre sendo = ao jog 
                if L > maximoLPossivel:  
                    maximoLPossivel = L
                    posicoesPossiveis = (posicaoLivre,)
                    # print("posicaoLivre:", posicaoLivre, "posicoesPossiveis:", posicoesPossiveis, "L",)  
                elif L == maximoLPossivel:  # se L for igual em mais de uma posição, cria uma lista de posições de L =
                    posicoesPossiveis += (posicaoLivre,)
                    
    # Se não conseguiu achar posição,bloqueia o adversário
    if maximoLPossivel < k: 
        adversario = -jog #faz a mesma logica anterior só que com o outro jogador, pra ver a melhor posição do outro jogdor
        for posicaoLivre in listaPosicoesLivre:
            tabuleiro_provisorio = cria_tabuleiro_provisorio(tab, posicaoLivre, adversario, nLinhas, nColunas)
            
            for L in range(1, k + 1):
                if verifica_k_linhas(tabuleiro_provisorio, posicaoLivre, adversario, L):
                    if L > maximoLPossivel:
                        maximoLPossivel = L
                        posicoesPossiveis = (posicaoLivre,)
                    elif L == maximoLPossivel:
                        posicoesPossiveis += (posicaoLivre,)

    # Critério de desempate, distância de Chebshev
    if posicoesPossiveis != ():
        posicoesOrdenadas = ordena_posicoes_tabuleiro(tab, posicoesPossiveis)
        return posicoesOrdenadas[0]  

    # Senão conseguir em nenhum dos casos, joga na posição livre mais proxima do centro 
    posicoesOrdenadas = ordena_posicoes_tabuleiro(tab, listaPosicoesLivre)
    return posicoesOrdenadas[0]

def cria_tabuleiro_provisorio(tab, posicao_livre, jogador,nLinhas,nColunas):
        # Função destinada a fazer uma copia do tabuleiro passado substituindo a posição livre pelo valor representado pelo jog 
        # Para fazer uma simulação do que aconteceria se substituir a posição livre por uma peça do jog
        novo_tabuleiro = ()
        for i in range(nLinhas):
            nova_linha = ()
            for j in range(nColunas):
                if (i * nColunas + j + 1) == posicao_livre:
                    nova_linha += (jogador,)
                else:
                    nova_linha += (tab[i][j],)
            novo_tabuleiro += (nova_linha,)
        return novo_tabuleiro


def verifica_lvl(lvl):
    """
    Função auxiliar criada para verifcação se a estratégia escolhida existe

    Parâmetros:
    lvl(str): String a ser validada

    Retorno:
    boolean: True se exite estratégia, False se não existir
    """
    
    if lvl != "facil" and lvl != "normal" and lvl != "dificil":
        return False
    return True

def jogo_mnk(cfg, jog, lvl):
    """
    Inicia e controla o fluxo de um jogo mnk

    Parâmetros:
    cfg (tuple): Uma tuplo  contendo três valores:
                 - cfg[0] (int): O número de linhas do tabuleiro.
                 - cfg[1] (int): O número de colunas do tabuleiro.
                 - cfg[2] (int): O número de peças consecutivas k necessárias para vencer.

    jog (int): Inteiro que indica qual cor de peça o jogador humano será

    lvl (str): Nível de dificuldade do computador, podendo ser:
               
    retorno:
    int: Devolve o jogador que venceu, 1 para o jogador que está com as peças pretas e -1 para o jogador que está com as peças brancas
    """
    tabuleiro = tuple(tuple(0 for i in range(cfg[1])) for j in range(cfg[0]))
    
    if not eh_tabuleiro(tabuleiro) or not verifica_jogador(jog) or not verifica_lvl(lvl):
        raise ValueError("jogo_mnk: argumentos invalidos")
    
    rodada = 0
    turno = 1  # O jogador com o valor 1 sempre começa

    if jog == 1:
        simboloJogador = 'X'
    else:
        simboloJogador = 'O'

    print(f"Bem-vindo ao JOGO MNK.\nO jogador joga com '" + simboloJogador + "'.")

    while not eh_fim_jogo(tabuleiro, cfg[2]):
        print(tabuleiro_para_str(tabuleiro))  
        
        if turno == 1:
            if jog == 1:  
                posicaoEscolhida = escolhe_posicao_manual(tabuleiro)
            else:  
                posicaoEscolhida = escolhe_posicao_auto(tabuleiro, 1, cfg[2], lvl)

            tabuleiro = marca_posicao(tabuleiro, posicaoEscolhida, 1)
        else: # Turno do jogador com valor -1 (pode ser pessoa ou computador)
            if jog == -1:  
                posicaoEscolhida = escolhe_posicao_manual(tabuleiro)
            else:
                print("Turno do computador (" + lvl + "):")
                posicaoEscolhida = escolhe_posicao_auto(tabuleiro, -1, cfg[2], lvl)

            tabuleiro = marca_posicao(tabuleiro, posicaoEscolhida, -1)

        if verifica_k_linhas(tabuleiro, posicaoEscolhida, turno, cfg[2]): # Verifica se o jogo terminou após a jogada
            print(tabuleiro_para_str(tabuleiro))
            if turno == 1:
                print("VITORIA")
                if jog == 1:
                    return 1
                return -1
                 
            else:
                print("DERROTA")
                if jog == 1:
                    return 1
                return -1
        turno = -turno
        rodada += 1

    print("EMPATE")
    return 0
