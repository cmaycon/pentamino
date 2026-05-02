import copy

class Tabuleiro:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        # O tabuleiro é uma matriz bidimensional
        # Inicializa tudo com 0 (espaço vazio)
        self.matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
        
    def exibir(self):
        """Imprime o estado atual do tabuleiro no terminal."""
        for linha in self.matriz:
            # Troca o 0 por um ponto '.' para ficar mais fácil de enxergar os espaços vazios
            linha_formatada = [str(celula) if celula != 0 else "." for celula in linha]
            print(" ".join(linha_formatada))
        print("-" * (self.colunas * 2))

    def pode_inserir(self, peca_matriz, linha_inicio, coluna_inicio):
        """
        Valida se a jogada é válida:
        - Sem sobreposição
        - Dentro dos limites
        """
        for i in range(len(peca_matriz)):
            for j in range(len(peca_matriz[0])):
                if peca_matriz[i][j] == 1: 
                    # Verifica se saiu dos limites do tabuleiro (todas as bordas)
                    if (linha_inicio + i >= self.linhas) or (coluna_inicio + j >= self.colunas) or \
                       (linha_inicio + i < 0) or (coluna_inicio + j < 0):
                        return False
                        
                    # Verifica se já tem uma peça lá (sobreposição)
                    if self.matriz[linha_inicio + i][coluna_inicio + j] != 0:
                        return False
        return True

    def inserir_peca(self, peca_matriz, linha_inicio, coluna_inicio, id_peca):
        """
        Insere a peça e retorna um NOVO estado (uma nova instância de Tabuleiro).
        Retornar um novo estado em vez de alterar o atual é crucial para modelar 
        o problema como um grafo na hora da busca[cite: 1].
        """
        # Cria uma cópia totalmente independente do tabuleiro atual
        novo_tabuleiro = Tabuleiro(self.linhas, self.colunas)
        novo_tabuleiro.matriz = [linha[:] for linha in self.matriz]
        
        # Preenche a matriz do novo tabuleiro com o ID (nome/letra) da peça
        for i in range(len(peca_matriz)):
            for j in range(len(peca_matriz[0])):
                if peca_matriz[i][j] == 1:
                    novo_tabuleiro.matriz[linha_inicio + i][coluna_inicio + j] = id_peca
                    
        return novo_tabuleiro
        
    def gerar_assinatura(self):
        """
        Gera uma string única que representa a configuração atual do tabuleiro[cite: 1].
        Essa string será transformada na chave única (hash) que usaremos na 
        Árvore AVL para evitar explorar estados redundantes[cite: 1].
        """
        return str(self.matriz)