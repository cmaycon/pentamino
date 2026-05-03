import tkinter as tk
import time

CORES_PECAS = {
    'F': '#FFA500', 'I': '#00FFFF', 'L': '#0000FF', 'N': '#32CD32',
    'P': '#FF0000', 'T': '#800080', 'U': '#8B4513', 'V': '#FF69B4',
    'W': '#FFFF00', 'X': '#A9A9A9', 'Y': '#98FB98', 'Z': '#FF00FF',
    0:   '#FFFFFF'
}

class InterfaceAnimada:
    def __init__(self, linhas, colunas, atraso=0.05):
        self.janela = tk.Tk()
        self.janela.title("Resolvendo Pentaminó (Animação)...")
        self.tamanho_celula = 40
        self.atraso = atraso
        
        largura = colunas * self.tamanho_celula
        altura = linhas * self.tamanho_celula
        
        self.canvas = tk.Canvas(self.janela, width=largura, height=altura, bg="white")
        self.canvas.pack(padx=20, pady=20)

    def atualizar(self, tabuleiro):
        """Limpa a tela e desenha o estado atual do tabuleiro."""
        self.canvas.delete("all") # Apaga o frame anterior
        
        for i in range(tabuleiro.linhas):
            for j in range(tabuleiro.colunas):
                id_peca = tabuleiro.matriz[i][j]
                cor = CORES_PECAS.get(id_peca, '#000000')
                
                x1 = j * self.tamanho_celula
                y1 = i * self.tamanho_celula
                x2 = x1 + self.tamanho_celula
                y2 = y1 + self.tamanho_celula
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="black")
                if id_peca != 0:
                    self.canvas.create_text(x1 + self.tamanho_celula/2, y1 + self.tamanho_celula/2, 
                                       text=str(id_peca), font=("Arial", 12, "bold"))
        
        self.janela.update() # Força o Tkinter a desenhar imediatamente
        time.sleep(self.atraso) # Pausa para o "olho humano" ver

    def finalizar(self):
        """Mantém a janela aberta no final até o usuário fechar."""
        self.janela.title("Solução Encontrada!")
        self.janela.mainloop()