class NoAVL:
    def __init__(self, chave):
        self.chave = chave 
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """Operação principal de inserção exigida pelo escopo"""
        if not self.buscar(chave): 
            self.raiz = self._inserir_recursivo(self.raiz, chave)

    def buscar(self, chave):
        """Operação principal de busca para verificar se o estado já foi visitado"""
        return self._buscar_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        # Inserção normal de Árvore Binária de Busca
        if not no:
            return NoAVL(chave)
        elif chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        else:
            no.direita = self._inserir_recursivo(no.direita, chave)

        # Atualiza a altura do nó ancestral
        no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))

        # Obtém o fator de balanceamento para checar se desbalanceou
        fator = self._obter_balanceamento(no)

        # Realiza as Rotações se houver desbalanceamento
        # Caso Esquerda-Esquerda
        if fator > 1 and chave < no.esquerda.chave:
            return self._rotacao_direita(no)
        # Caso Direita-Direita
        if fator < -1 and chave > no.direita.chave:
            return self._rotacao_esquerda(no)
        # Caso Esquerda-Direita
        if fator > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        # Caso Direita-Esquerda
        if fator < -1 and chave < no.direita.chave:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return False
        if no.chave == chave:
            return True
        if chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        return self._buscar_recursivo(no.direita, chave)

    def _obter_altura(self, no):
        if not no: return 0
        return no.altura

    def _obter_balanceamento(self, no):
        if not no: return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        
        # Realiza a rotação
        y.esquerda = z
        z.direita = T2
        
        # Atualiza as alturas
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))
        return y

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        
        # Realiza a rotação
        y.direita = z
        z.esquerda = T3
        
        # Atualiza as alturas
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))
        return y