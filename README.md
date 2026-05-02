# 🧩 Jogo de Pentaminós: Interativo e Solucionador

Este projeto é uma implementação em Python do clássico quebra-cabeça dos Pentaminós. Ele foi desenvolvido com foco na aplicação prática de Estruturas de Dados e Algoritmos Complexos, incluindo **Modelagem em Grafos**, algoritmos de **Busca (DFS e BFS)** e **Árvores Balanceadas (AVL)** para otimização de memória.

## 🚀 Funcionalidades

O sistema oferece dois modos principais de operação:

*   **🎮 Modo Jogar (Interativo):** Permite ao usuário tentar resolver o quebra-cabeça manualmente. O sistema valida rigorosamente as jogadas, impedindo sobreposições e a inserção de peças fora dos limites do tabuleiro. O jogador pode escolher a peça e qual de suas rotações/reflexões deseja usar.
*   **🤖 Modo Resolver (Automático):** Atua como o "cérebro" do sistema, utilizando inteligência artificial clássica para encontrar a solução do tabuleiro sozinho.
    *   **Busca em Profundidade (DFS):** Rápida e com baixo consumo de memória. Altamente recomendada para tabuleiros maiores (ex: 6x10 ou 5x12).
    *   **Busca em Largura (BFS):** Explora nível por nível. Excelente para demonstrar a explosão combinatória do problema.
    *   **Otimização por AVL:** Utiliza uma Árvore AVL desenvolvida do zero para armazenar "hashes" (assinaturas) dos estados já visitados, evitando loops infinitos e processamento redundante.

## 📁 Estrutura do Projeto

Para garantir a modularidade e a organização, o código foi dividido em 5 arquivos independentes:

*   `main.py`: O coração do projeto. Lida com os menus, entrada do usuário e o fluxo do jogo.
*   `pecas.py`: Contém as matrizes das 12 peças oficiais e a lógica matemática para gerar suas rotações e reflexões.
*   `tabuleiro.py`: Gerencia a grade de jogo, imprime o estado visual e valida fisicamente as jogadas.
*   `avl.py`: Implementação matemática da Árvore Binária de Busca Balanceada (AVL).
*   `busca.py`: Contém a inteligência do algoritmo, gerador de vizinhos (arestas do grafo) e a lógica de DFS/BFS.

## ⚙️ Como Executar

**Pré-requisitos:** Você precisa ter o [Python 3.x](https://www.python.org/downloads/) instalado na sua máquina. Nenhuma biblioteca externa é necessária.

1.  Abra o terminal (ou Prompt de Comando).
2.  Navegue até a pasta onde os arquivos do projeto estão salvos.
3.  Execute o comando abaixo:
    ```bash
    python main.py
    ```

## 🕹️ Como Jogar (Modo Interativo)

1.  Ao iniciar o programa, defina o tamanho do tabuleiro (linhas e colunas). A área total deve ser maior ou igual a 5.
2.  Escolha a opção **1** no menu principal.
3.  O sistema listará as letras das peças disponíveis. Digite a letra da peça que deseja usar.
4.  O sistema mostrará todas as variações (rotações/espelhamentos) daquela peça. Digite o número correspondente à variação desejada.
5.  **Atenção às Coordenadas:** Informe a Linha e a Coluna onde o *canto superior esquerdo* da matriz da peça será posicionado.
    *   **Lembrete:** Na programação, os índices começam no **Zero**. Para colocar uma peça no topo esquerdo absoluto do tabuleiro, digite Linha `0` e Coluna `0`.
6.  Se a jogada for válida, o tabuleiro será atualizado. Caso contrário, o sistema avisará sobre limites ou sobreposições.

## 🧠 Solucionador e Explosão Combinatória

O problema dos Pentaminós possui **crescimento exponencial**. Existem milhares de formas de organizar apenas algumas peças. 

*   **Para testes rápidos:** Crie um tabuleiro 3x5 e restrinja as peças no código (ex: U, Y, P) para ver o algoritmo resolvendo em milissegundos.
*   **Para o desafio real:** Crie um tabuleiro padrão 6x10 ou 5x12 (que utilizam todas as 12 peças, somando 60 blocos). 
    *   **⚠️ Aviso:** Neste cenário, utilize **sempre** a Busca em Profundidade (DFS). A Busca em Largura (BFS) tentará armazenar milhões de matrizes simultâneas na RAM e travará o seu computador devido à exaustão de memória.