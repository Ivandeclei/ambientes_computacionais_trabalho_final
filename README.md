# ambientes_computacionais_trabalho_final
Solução de Problema do Rosalind "Matching a Spectrum to a Protein"

# Nome: Ivandeclei Mendes da costa
# Link: [ROSALIND - Brasil | Combinando um espectro a uma proteína](link)

## Problema

O espectro completo de uma cadeia ponderada *s* é o multiconjunto *S[s]* contendo os pesos de cada prefixo e sufixo de *s*.

**Dado:** Um inteiro positivo *n* seguido de uma coleção de *n* cordas proteicas *s1, s2, ..., sn* e um multiconjunto *R* de números positivos (correspondendo ao espectro completo de alguma cadeia proteica desconhecida).

**Retornar:** A multiplicidade máxima de *R⊖S[sk]* assumiu todas as cordas *sk*, seguido pela cadeia de caracteres *sk* para os quais ocorre essa multiplicidade máxima (Você pode gerar qualquer valor se existirem várias soluções).

## Conjunto de dados de exemplo

4\
GSDMQS\
VWICN\
IASWMQS\
PVSMGAD\
445.17838\
115.02694\
186.07931\
314.13789\
317.1198\
215.09061


**Saída de amostra**

3\
IASWMQS


## Entendendo o problema

O “espectro completo de uma cadeia ponderada (s)” refere-se ao conjunto de todos os pesos possíveis que podem ser derivados dos prefixos e sufixos da cadeia (s).

**Cadeia Ponderada:** Uma cadeia ponderada é uma sequência de elementos onde cada elemento tem um peso associado.

**Prefixos e Sufixos:** Prefixos são subcadeias que começam no primeiro elemento e terminam em qualquer ponto da cadeia. Sufixos são subcadeias que começam em qualquer ponto da cadeia e terminam no último elemento.

**Multiconjunto (*S[s])*:** Um multiconjunto é semelhante a um conjunto, mas permite múltiplas ocorrências do mesmo elemento. (*S[s]*) contém os pesos de todos os prefixos e sufixos possíveis de (*s*).

**Pesos:** O peso de um prefixo ou sufixo é a soma dos pesos dos elementos que compõem o prefixo ou sufixo.

Portanto, o espectro completo é uma coleção que representa todas as combinações possíveis de pesos que você pode obter ao considerar cada subcadeia possível de (*s*), tanto do início (prefixos) quanto do fim (sufixos).

**Cálculo do Espectro Completo (*S[sk]*)**: Para cada corda proteica *sk* na lista fornecida do enunciado, deve-se calcular o seu espectro completo. Isso significa enumerar todos os possíveis substrings, tanto prefixos quanto sufixos, e calcular seus pesos.

**Subtração do Espectro Completo do Multiconjunto *R*:** Após calcular o espectro completo de cada corda proteica, subtraímos esse espectro completo do multiconjunto *R*. Isso resulta em um conjunto de diferenças, onde cada diferença representa os pesos presentes em *R*, mas ausentes no espectro completo da corda proteica *sk*.

**Cálculo da Multiplicidade Máxima da Diferença:** Para cada diferença obtida no passo anterior, precisamos calcular sua multiplicidade, ou seja, quantas vezes essa diferença ocorre no conjunto *R*. A multiplicidade máxima é o maior número de ocorrências entre todas as diferenças calculadas.

**Identificação da Corda Correspondente à Multiplicidade Máxima:** Uma vez que se determina a multiplicidade máxima, torna-se necessário identificar a corda proteica correspondente a essa multiplicidade máxima. Isso significa encontrar a corda *sk* para a qual a diferença entre o seu espectro completo e o conjunto *R* tem a maior multiplicidade.

**Retorno da Resposta:** Retorna à multiplicidade máxima encontrada, juntamente com a corda proteica correspondente. Se houver várias soluções com a mesma multiplicidade máxima, pode-se escolher qualquer uma delas para retornar como resposta.


## Como Executar o Programa Python

Para executar o programa Python com o nome `TrabalhoFinal.py`, siga estas etapas:

1. **Abra o Terminal ou Prompt de Comando:**
   - No Windows, você pode abrir o Prompt de Comando.
   - No macOS ou Linux, você pode abrir o Terminal.

2. **Navegue até o Diretório do Arquivo:**
   Use o comando `cd` para mudar para o diretório onde o arquivo `TrabalhoFinal.py` está localizado. Por exemplo:
   ```bash
   cd caminho/para/o/diretorio

3. **Execução**
    Rode o comando  `python TrabalhoFinal.py`
