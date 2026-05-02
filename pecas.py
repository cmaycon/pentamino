def rotacionar_90_graus(matriz):
    """
    Rotaciona a matriz 90 graus no sentido horário.
    Usa a combinação de zip (para transpor) e reversed.
    """
    return [list(linha) for linha in zip(*matriz[::-1])]

def refletir_matriz(matriz):
    """
    Reflete a matriz horizontalmente (como um espelho).
    """
    return [linha[::-1] for linha in matriz]

def gerar_todas_variacoes(peca_matriz):
    """
    Gera todas as variações únicas (rotações e reflexões) de uma peça.
    Retorna uma lista de matrizes.
    """
    variacoes = []
    assinaturas_vistas = set()
    
    matriz_atual = peca_matriz
    
    for _ in range(4):
        # Tenta a rotação atual
        assinatura = str(matriz_atual)
        if assinatura not in assinaturas_vistas:
            variacoes.append(matriz_atual)
            assinaturas_vistas.add(assinatura)
            
        # Tenta a reflexão da rotação atual
        matriz_refletida = refletir_matriz(matriz_atual)
        assinatura_refletida = str(matriz_refletida)
        if assinatura_refletida not in assinaturas_vistas:
            variacoes.append(matriz_refletida)
            assinaturas_vistas.add(assinatura_refletida)
            
        # Rotaciona para a próxima iteração do loop
        matriz_atual = rotacionar_90_graus(matriz_atual)
        
    return variacoes

TODAS_AS_PECAS = {
    'F': [[0, 1, 1],
          [1, 1, 0],
          [0, 1, 0]],
    'I': [[1, 1, 1, 1, 1]],
    'L': [[1, 0, 0, 0],
          [1, 1, 1, 1]],
    'N': [[0, 0, 1, 1],
          [1, 1, 1, 0]],
    'P': [[1, 1],
          [1, 1],
          [1, 0]],
    'T': [[1, 1, 1],
          [0, 1, 0],
          [0, 1, 0]],
    'U': [[1, 0, 1],
          [1, 1, 1]],
    'V': [[1, 0, 0],
          [1, 0, 0],
          [1, 1, 1]],
    'W': [[1, 0, 0],
          [1, 1, 0],
          [0, 1, 1]],
    'X': [[0, 1, 0],
          [1, 1, 1],
          [0, 1, 0]],
    'Y': [[0, 1, 0, 0],
          [1, 1, 1, 1]],
    'Z': [[1, 1, 0],
          [0, 1, 0],
          [0, 1, 1]]
}