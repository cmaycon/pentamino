# 🧩 Jogo de Pentaminós: Solucionador com Interface Gráfica

Este projeto é uma implementação avançada em Python do clássico quebra-cabeça dos Pentaminós. Ele foi desenvolvido com foco na aplicação prática de Estruturas de Dados e Algoritmos Complexos, incluindo **Modelagem em Grafos**, algoritmos de **Busca (DFS e BFS)**, **Árvores Balanceadas (AVL)** para otimização de memória e renderização visual via **Tkinter**.

## 🚀 Funcionalidades

O sistema oferece dois modos principais de operação, ambos com suporte visual:

*   **🎮 Modo Jogar (Interativo com Espelho Visual):** O usuário resolve o quebra-cabeça digitando os comandos no terminal, enquanto uma interface gráfica atualiza o tabuleiro em tempo real. O sistema valida rigorosamente as jogadas, impedindo sobreposições e a inserção de peças fora dos limites.
*   **🤖 Modo Resolver (Automático com Animação):** Atua como o "cérebro" do sistema, utilizando inteligência artificial clássica para encontrar a solução do tabuleiro sozinho.
    *   **Busca em Profundidade (DFS):** Rápida e com baixo consumo de memória. Altamente recomendada para tabuleiros maiores (ex: 6x10 ou 5x12).
    *   **Busca em Largura (BFS):** Explora nível por nível. Excelente para demonstrar a explosão combinatória do problema.
    *   **Visualização Animada:** Permite assistir ao algoritmo testando peças e fazendo *backtracking* ao vivo na tela.
    *   **Otimização por AVL:** Utiliza uma Árvore AVL desenvolvida do zero para armazenar "hashes" (assinaturas) dos estados já visitados, evitando processamento redundante.

## 📁 Estrutura do Projeto

Para garantir a modularidade e a organização, o código foi dividido em pequenos módulos independentes:

*   `main.py`: O coração do projeto. Lida com os menus e o fluxo principal.
*   `gui.py`: Responsável por renderizar a grade, colorir as peças e animar a tela usando a biblioteca nativa `tkinter`.
*   `pecas.py`: Contém as matrizes das 12 peças oficiais e a lógica matemática para gerar suas rotações e reflexões.
*   `tabuleiro.py`: Gerencia a grade de jogo internamente e valida fisicamente as jogadas.
*   `avl.py`: Implementação matemática da Árvore Binária de Busca Balanceada (AVL).
*   `busca.py`: Contém a inteligência do algoritmo, gerador de vizinhos (arestas do grafo) e a lógica de DFS/BFS.

## ⚙️ Como Executar

**Pré-requisitos:** Você precisa ter o [Python 3.x](https://www.python.org/downloads/) instalado. **Nenhuma biblioteca externa é necessária** (o Tkinter já vem embutido no Python), dispensando o uso de instaladores como o `pip`.

1.  Abra o terminal (ou Prompt de Comando).
2.  Navegue até a pasta onde os arquivos do projeto estão salvos.
3.  Execute o comando:
    ```bash
    python main.py
    ```

## 🕹️ Como Jogar (Modo Interativo)

1.  No menu principal, escolha a opção **1**.
2.  Uma janela gráfica em branco será aberta. **Deixe-a visível**, mas continue digitando os comandos na tela do seu terminal.
3.  O sistema listará as peças disponíveis. Digite a letra da peça desejada.
4.  O sistema mostrará todas as variações (rotações/espelhamentos) daquela peça. Digite o número correspondente à variação.
5.  **Coordenadas:** Informe a Linha e a Coluna onde o *canto superior esquerdo* da peça será posicionado. *(Lembre-se: os índices começam no Zero)*.
6.  Ao confirmar, a jogada será validada e a peça aparecerá magicamente colorida na janela gráfica!
7.  Para desistir e voltar ao menu, digite **`sair`** a qualquer momento na escolha de peças. A janela gráfica será encerrada com segurança.

## 🧠 Solucionador e Dicas de Desempenho (⚠️ IMPORTANTE)

O problema dos Pentaminós possui **crescimento exponencial**. O desempenho do algoritmo depende diretamente do tamanho do tabuleiro e das opções que você escolhe. Siga este guia para a melhor experiência:

### 1. A Maldição da Animação (Use com moderação)
*   **Para ver a animação funcionando:** Crie um tabuleiro pequeno (ex: **3x5**) e limite as peças no código. O algoritmo animará os testes em tempo real sem travar.
*   **Para resolver o jogo completo (6x10 ou 5x12):** Quando o sistema perguntar se você deseja ver a animação, **responda NÃO (`n`)**. Desenhar pixels coloridos na tela repetidamente é um processo físico muito mais lento do que fazer cálculos matemáticos puros na CPU. Animar um tabuleiro gigante fará com que o programa demore dias para terminar. Sem a animação, ele focará 100% do processamento na busca.

### 2. DFS vs BFS
*   **Sempre priorize a DFS (Opção 1) para tabuleiros grandes.** A Busca em Profundidade consome muito pouca memória RAM, pois explora um caminho até o fim antes de voltar.
*   **Cuidado com a BFS (Opção 2).** A Busca em Largura guarda todas as possibilidades simultaneamente na fila. Em tabuleiros grandes, ela gerará milhões de matrizes em poucos segundos, esgotando a memória RAM do seu computador e causando lentidão ou travamento (erro `KeyboardInterrupt` ao forçar a parada).