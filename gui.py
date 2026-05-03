import tkinter as tk

# Um dicionário para dar uma cor diferente para cada peça do Pentaminó
CORES_PECAS = {
    'F': '#FFA500', # Laranja
    'I': '#00FFFF', # Ciano
    'L': '#0000FF', # Azul
    'N': '#32CD32', # Verde Lima
    'P': '#FF0000', # Vermelho
    'T': '#800080', # Roxo
    'U': '#8B4513', # Marrom
    'V': '#FF69B4', # Rosa
    'W': '#FFFF00', # Amarelo
    'X': '#A9A9A9', # Cinza
    'Y': '#98FB98', # Verde Claro
    'Z': '#FF00FF', # Magenta
    0:   '#FFFFFF'  # Branco (Espaço Vazio)
}

def exibir_interface_grafica(tabuleiro, titulo="Solução Pentaminó"):
    """
    Cria uma janela Tkinter e desenha o estado final do tabuleiro.
    """
    janela = tk.Tk()
    janela.title(titulo)
    janela.resizable(False, False) # Impede de redimensionar a janela
    
    tamanho_celula = 40 # Tamanho de cada "quadradinho" em pixels
    largura_canvas = tabuleiro.colunas * tamanho_celula
    altura_canvas = tabuleiro.linhas * tamanho_celula
    
    # Cria a tela de pintura (Canvas)
    canvas = tk.Canvas(janela, width=largura_canvas, height=altura_canvas, bg="white")
    canvas.pack(padx=20, pady=20) # Adiciona uma margem
    
    # Percorre a matriz do seu código e desenha os blocos
    for i in range(tabuleiro.linhas):
        for j in range(tabuleiro.colunas):
            id_peca = tabuleiro.matriz[i][j]
            cor = CORES_PECAS.get(id_peca, '#000000') # Preto se der algum erro
            
            # Calcula as coordenadas do retângulo
            x1 = j * tamanho_celula
            y1 = i * tamanho_celula
            x2 = x1 + tamanho_celula
            y2 = y1 + tamanho_celula
            
            # Desenha o quadrado
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="black")
            
            # Escreve a letra da peça no meio do quadrado (se não for vazio)
            if id_peca != 0:
                canvas.create_text(x1 + tamanho_celula/2, y1 + tamanho_celula/2, 
                                   text=str(id_peca), font=("Arial", 12, "bold"))
                
    # Inicia o loop da janela para ela não fechar sozinha
    janela.mainloop()