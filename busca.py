import time
from collections import deque
from avl import ArvoreAVL
from pecas import gerar_todas_variacoes

def encontrar_primeira_celula_vazia(tabuleiro):
    """
    Otimização crucial: Em vez de tentar colocar peças em qualquer lugar,
    buscamos o primeiro espaço vazio (de cima para baixo, esquerda para direita).
    Isso reduz drasticamente a árvore de busca e evita gerar permutações repetidas.
    """
    for i in range(tabuleiro.linhas):
        for j in range(tabuleiro.colunas):
            if tabuleiro.matriz[i][j] == 0:
                return i, j
    return None # Tabuleiro cheio (Solução encontrada!)

def gerar_vizinhos(tabuleiro_atual, pecas_restantes):
    """
    Gera todos os estados seguintes válidos (arestas do grafo).
    """
    vizinhos = []
    celula_vazia = encontrar_primeira_celula_vazia(tabuleiro_atual)
    
    if not celula_vazia:
        return vizinhos # Não há vizinhos se o tabuleiro já está cheio
        
    linha_vazia, coluna_vazia = celula_vazia

    for id_peca, matriz_peca in pecas_restantes.items():
        variacoes = gerar_todas_variacoes(matriz_peca)
        
        for variacao in variacoes:
            for i_offset in range(len(variacao)):
                for j_offset in range(len(variacao[0])):
                    if variacao[i_offset][j_offset] == 1:
                        linha_tentativa = linha_vazia - i_offset
                        coluna_tentativa = coluna_vazia - j_offset
                        
                        if tabuleiro_atual.pode_inserir(variacao, linha_tentativa, coluna_tentativa):
                            novo_tab = tabuleiro_atual.inserir_peca(variacao, linha_tentativa, coluna_tentativa, id_peca)
                            
                            novas_pecas_restantes = pecas_restantes.copy()
                            del novas_pecas_restantes[id_peca]
                            
                            vizinhos.append((novo_tab, novas_pecas_restantes))
    return vizinhos

def resolver_dfs(tabuleiro_inicial, pecas_iniciais):
    """
    Busca em Profundidade (DFS).
    Usa uma Pilha (Stack) - Vai até o fim de um caminho antes de voltar.
    """
    print("Iniciando Busca em Profundidade (DFS)...")
    tempo_inicio = time.time()
    
    # A pilha armazena tuplas: estado_do_tabuleiro, dicionario_de_pecas_restantes
    pilha = [(tabuleiro_inicial, pecas_iniciais)]
    
    estados_visitados = ArvoreAVL()
    num_estados_explorados = 0
    
    while pilha:
        tab_atual, pecas_restantes = pilha.pop()
        assinatura = tab_atual.gerar_assinatura()
        
        # Se a AVL já contém este estado, ignora para evitar redundância
        if estados_visitados.buscar(assinatura):
            continue
            
        estados_visitados.inserir(assinatura)
        num_estados_explorados += 1
        
        # Condição de vitória: se não há mais espaços vazios
        if encontrar_primeira_celula_vazia(tab_atual) is None:
            tempo_fim = time.time()
            print(f"Solução encontrada com DFS em {tempo_fim - tempo_inicio:.4f} segundos!")
            print(f"Estados explorados: {num_estados_explorados}")
            return tab_atual
            
        # Adiciona os vizinhos na pilha
        vizinhos = gerar_vizinhos(tab_atual, pecas_restantes)
        for vizinho_tab, vizinho_pecas in vizinhos:
            pilha.append((vizinho_tab, vizinho_pecas))
            
    print("Nenhuma solução encontrada.")
    return None

def resolver_bfs(tabuleiro_inicial, pecas_iniciais):
    """
    Busca em Largura (BFS).
    Usa uma Fila (Queue) - Explora nível por nível. 
    Encontra a solução com menor profundidade.
    """
    print("Iniciando Busca em Largura (BFS)...")
    tempo_inicio = time.time()
    
    fila = deque([(tabuleiro_inicial, pecas_iniciais)])
    
    estados_visitados = ArvoreAVL()
    num_estados_explorados = 0
    
    while fila:
        tab_atual, pecas_restantes = fila.popleft()
        
        assinatura = tab_atual.gerar_assinatura()
        
        if estados_visitados.buscar(assinatura):
            continue
            
        estados_visitados.inserir(assinatura)
        num_estados_explorados += 1
        
        if encontrar_primeira_celula_vazia(tab_atual) is None:
            tempo_fim = time.time()
            print(f"Solução encontrada com BFS em {tempo_fim - tempo_inicio:.4f} segundos!")
            print(f"Estados explorados: {num_estados_explorados}")
            return tab_atual
            
        vizinhos = gerar_vizinhos(tab_atual, pecas_restantes)
        for vizinho_tab, vizinho_pecas in vizinhos:
            fila.append((vizinho_tab, vizinho_pecas))
            
    print("Nenhuma solução encontrada.")
    return None