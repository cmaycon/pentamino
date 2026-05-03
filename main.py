import sys
from tabuleiro import Tabuleiro
from busca import resolver_dfs, resolver_bfs
from pecas import TODAS_AS_PECAS, gerar_todas_variacoes
from gui import InterfaceAnimada

def configurar_tabuleiro():
    """Lida com a entrada de dados e validação das dimensões."""
    print("=== CONFIGURAÇÃO DO TABULEIRO ===")
    while True:
        try:
            linhas = int(input("Digite o número de linhas (m): "))
            colunas = int(input("Digite o número de colunas (n): "))
            
            area = linhas * colunas
            if area < 5:
                print("Erro: A área do tabuleiro deve ser >= 5. Tente novamente.")
                continue
            if area % 5 != 0:
                print("Aviso: A área não é múltipla de 5. Pode não haver solução perfeita.")
                
            return Tabuleiro(linhas, colunas)
        except ValueError:
            print("Por favor, digite números inteiros válidos.")

def mostrar_variacoes(variacoes):
    """Exibe as opções de rotação/reflexão para o jogador escolher."""
    print("\nVariações disponíveis para esta peça:")
    for idx, var in enumerate(variacoes):
        print(f"[{idx + 1}]")
        for linha in var:
            # Troca os zeros por espaços em branco e 1s por blocos para facilitar a visualização
            print("".join(["██" if x == 1 else "  " for x in linha]))
        print("")

def modo_jogar(tabuleiro):
    """Modo interativo com espelhamento gráfico."""
    print("\n=== MODO JOGAR ===")
    pecas_restantes = TODAS_AS_PECAS.copy()
    
    # --- Abre a janela gráfica para o jogador ---
    print("Abrindo o tabuleiro visual...")
    interface = InterfaceAnimada(tabuleiro.linhas, tabuleiro.colunas, atraso=0)
    interface.janela.title("Modo Jogar - Interativo")
    interface.atualizar(tabuleiro)
    # -----------------------------------------------------
    
    while pecas_restantes:
        print("\nEstado atual do tabuleiro:")
        tabuleiro.exibir()
        print(f"Peças disponíveis: {', '.join(pecas_restantes.keys())}")
        
        peca_escolhida = input("Escolha uma peça (ou 'sair' para encerrar): ").upper()
        if peca_escolhida == 'SAIR':
            print("\nJogo encerrado pelo usuário.")
            interface.janela.destroy() # Fecha a janela gráfica na hora
            return # Sai da função e volta direto para o menu principal
            
        if peca_escolhida not in pecas_restantes:
            print("Peça inválida ou já utilizada!")
            continue
            
        matriz_base = pecas_restantes[peca_escolhida]
        variacoes = gerar_todas_variacoes(matriz_base)
        
        mostrar_variacoes(variacoes)
        
        try:
            escolha_var = int(input(f"Escolha qual variação usar (1 a {len(variacoes)}): ")) - 1
            if escolha_var < 0 or escolha_var >= len(variacoes):
                print("Variação inválida. Tente novamente.")
                continue
                
            matriz_peca = variacoes[escolha_var]
            linha = int(input("Linha inicial para inserir (0 a {}): ".format(tabuleiro.linhas - 1)))
            coluna = int(input("Coluna inicial para inserir (0 a {}): ".format(tabuleiro.colunas - 1)))
        except ValueError:
            print("Entrada inválida. Digite números.")
            continue
            
        if tabuleiro.pode_inserir(matriz_peca, linha, coluna):
            tabuleiro = tabuleiro.inserir_peca(matriz_peca, linha, coluna, peca_escolhida)
            del pecas_restantes[peca_escolhida]
            print("\n✅ Jogada válida!")
            
            # --- Atualiza a tela gráfica com a nova peça ---
            interface.atualizar(tabuleiro)
        else:
            print("\n❌ Jogada inválida! Verifique os limites e sobreposições.")
            
    print("\nFim de jogo. Estado final do tabuleiro:")
    tabuleiro.exibir()
    interface.finalizar() # Trava a janela aberta no final

def modo_resolver(tabuleiro):
    """Modo automático utilizando grafos e buscas."""
    print("\n=== MODO RESOLVER ===")
    print("1. Busca em Profundidade (DFS)")
    print("2. Busca em Largura (BFS)")
    
    escolha = input("Escolha o algoritmo (1 ou 2): ")
    pecas_iniciais = TODAS_AS_PECAS.copy()
    
    # Pergunta se quer animar
    animar = input("Deseja ver a animação da busca? (s/n): ").lower() == 's'
    interface = InterfaceAnimada(tabuleiro.linhas, tabuleiro.colunas, atraso=0.05) if animar else None
    
    if escolha == '1':
        solucao = resolver_dfs(tabuleiro, pecas_iniciais, interface)
    elif escolha == '2':
        solucao = resolver_bfs(tabuleiro, pecas_iniciais, interface)
    else:
        print("Opção inválida.")
        return
        
    if solucao:
        print("\n🏆 Solução Final Encontrada:")
        solucao.exibir()
        if interface:
            interface.finalizar()
    else:
        print("\nO algoritmo não conseguiu encontrar uma solução.")

def main():
    print("Bem-vindo ao Jogo de Pentaminós!")
    tabuleiro = configurar_tabuleiro()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Modo Jogar (Interativo)")
        print("2. Modo Resolver (Automático)")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            modo_jogar(tabuleiro)
        elif opcao == '2':
            modo_resolver(tabuleiro)
        elif opcao == '3':
            print("Encerrando o programa...")
            sys.exit()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()