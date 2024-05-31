'''
    # Nome: Ivandeclei Mendes da costa
    # Problema: https://rosalind.info/problems/prsm/

'''

# Função para calcular a multiplicidade entre dois conjuntos
def calcular_multiplicidade(conjunto_R, conjunto_S):
    # Retorna o tamanho da interseção entre os dois conjuntos, 
    # o intersection é usado para definir elementos em comum
    # len é utilizado para calcular a quantidade
    return len(conjunto_R.intersection(conjunto_S))

# Função para gerar o espectro completo de uma proteína
def espectro_completo(proteina, pesos_aminoacidos):
    # Conjunto para armazenar os pesos das sub-sequências
    pesos = set()
    
    # Comprimento da proteína
    n = len(proteina)  

    # Gera todas as subsequências circulares possíveis para garantir que todas as possiveis 
    # subsequencias de uma proteina sejam consideradas.
    for i in range(n):
        for j in range(1, n):
            # Forma a sub-sequência circular 
            #A soma i + j é calculada e é feita uma correção caso a soma seja maior que o comprimento da proteína ((i + j) - n). 
            # Isso garante que a subsequência circule de volta ao início da proteína quando ultrapassa o seu final.
            subsequencia = proteina[i:i+j] + proteina[:max(0, (i+j) - n)]
            # Calcula o peso da sub-sequência
            #  retorna uma lista de pesos moleculares dos aminoácidos presentes na subsequência.
            # A função sum() soma todos os elementos desta lista, resultando no peso total da subsequência.
            peso = sum(pesos_aminoacidos[aa] for aa in subsequencia)
            # Adiciona o peso ao conjunto de pesos
            pesos.add(peso)
    
    #soma dos pesos moleculares de todos os aminoácidos na sequência da proteína, resultando em o peso total da proteína
    # Adiciona o peso total da proteína completa ao conjunto
    peso_total = sum(pesos_aminoacidos[aa] for aa in proteina)
    pesos.add(peso_total)
    
    return pesos

# Função principal para resolver o problema
def main(local_arquivo):
    try:
        with open(local_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            # Remove possíveis linhas vazias
            linhas = [linha for linha in linhas if linha.strip()]
            
            # Convertendo as últimas 6 linhas para o conjunto de referência R
            conjunto_R = set(map(float, linhas[-6:]))
            
            # Convertendo as linhas intermediárias para as proteínas
            proteinas = [linha.strip() for linha in linhas[:-6]]
            
            # Pesos dos aminoácidos 
            pesos_aminoacidos = {
                'G': 57.02146, 'A': 71.03711, 'S': 87.03203, 'P': 97.05276,
                'V': 99.06841, 'T': 101.04768, 'C': 103.00919, 'I': 113.08406,
                'L': 113.08406, 'N': 114.04293, 'D': 115.02694, 'Q': 128.05858,
                'K': 128.09496, 'E': 129.04259, 'M': 131.04049, 'H': 137.05891,
                'F': 147.06841, 'R': 156.10111, 'Y': 163.06333, 'W': 186.07931
            }

            # Inicialização das variáveis para armazenar o resultado final
            max_multiplicidade = 0
            proteina_resposta = ""

            # Loop sobre todas as proteínas do conjunto
            for proteina in proteinas:
                # Verifica se todos os aminoácidos na proteína têm pesos associados
                if all(aa in pesos_aminoacidos for aa in proteina):
                    # Gera o espectro completo da proteína
                    conjunto_S = espectro_completo(proteina, pesos_aminoacidos)
                    # Calcula a multiplicidade entre R e S
                    # Sendo R os 6 ultimos numeros da entrada e 
                    # S os pesos de cada referencia circular
                    multiplicidade = calcular_multiplicidade(conjunto_R, conjunto_S)
                    # Atualiza o máximo de multiplicidade e a proteína correspondente se necessário
                    if multiplicidade > max_multiplicidade:
                        max_multiplicidade = multiplicidade
                        proteina_resposta = proteina

        # Retorna a máxima multiplicidade e a proteína correspondente
        return max_multiplicidade, proteina_resposta
    except FileNotFoundError:
        print("Arquivo não encontrado.")


local_arquivo = "dados_entrada.txt"
maxima_multiplicidade, proteina_correspondente = main(local_arquivo)
print(f'Multiplicidade máxima: {maxima_multiplicidade}')
print(f'Proteína com máxima multiplicidade: {proteina_correspondente}')
