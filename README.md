# PUC Minas - Fundamentos de Projeto e Análise de Algoritmos
## Trabalho Individual 3: Caminho Hamiltoniano

**Curso:** Engenharia de Software<br>
**Professor:** [João Paulo Carneiro Aramuni](https://github.com/joaopauloaramuni)<br>
**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos<br>


## Objetivo

Desenvolver um programa em Python que implemente o algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado

## O que é o Algoritmo para Caminho Hamiltonian?

Um Caminho Hamiltoniano em um grafo é um caminho que visita cada vértice
exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria
dos grafos e está associado a problemas de alta complexidade computacional,
como o Problema do Caixeiro Viajante. Este projeto tem como objetivo
implementar uma abordagem para determinar se um Caminho Hamiltoniano
existe em um grafo e, em caso afirmativo, encontrá-lo.

## 1. Descrição do projeto

Este projeto consiste na implementação de um algoritmo em Python para encontrar um Caminho Hamiltoniano em um grafo não orientado. Um Caminho Hamiltoniano é definido como um caminho em um grafo que visita cada vértice exatamente uma vez.

O problema de encontrar tal caminho é um problema clássico na teoria dos grafos e é classificado como NP-Completo.

### Lógica da Implementação

O algoritmo foi implementado utilizando a linguagem Python no arquivo `main.py` e segue uma abordagem de **backtracking (retrocesso)**.

A lógica "linha a linha" pode ser resumida da seguinte forma:

1.  **Estrutura de Dados:** O grafo é representado por uma classe `Grafo`, que armazena o número de vértices (`V`) e uma lista de adjacência (`adj`) para representar as conexões (arestas).

2.  **Função Principal (`encontrar_caminho_hamiltoniano`):**
    * Esta função serve como ponto de entrada. Ela inicializa as estruturas necessárias: um `set` chamado `visitado` (para rastrear vértices já incluídos no caminho) e uma lista `caminho` (para armazenar a ordem dos vértices).
    * Como o Caminho Hamiltoniano pode começar em qualquer vértice, esta função itera por todos os vértices do grafo (de `0` a `V-1`) e tenta iniciar a busca recursiva a partir de cada um deles.
    * Se a função recursiva (`buscar_caminho_util`) retornar `True`, significa que um caminho foi encontrado, e ele é impresso no console.
    * Se o loop terminar sem sucesso, uma mensagem informa que nenhum caminho existe.

3.  **Função Recursiva (`buscar_caminho_util`):**
    * Esta é a função central que implementa o backtracking.
    * **Passo 1 (Adicionar):** O vértice atual (`v`) é adicionado à lista `caminho` e marcado no conjunto `visitado`.
    * **Passo 2 (Base de Sucesso):** A função verifica se o comprimento do `caminho` é igual ao número total de vértices (`self.V`). Se for, todos os vértices foram visitados, e um Caminho Hamiltoniano foi encontrado. A função retorna `True`.
    * **Passo 3 (Recursão):** A função itera por todos os `vizinhos` do vértice atual `v`. Se um `vizinho` ainda **não** foi visitado:
        * Ela faz uma chamada recursiva para `buscar_caminho_util` usando esse `vizinho` como novo vértice.
        * Se essa chamada recursiva retornar `True`, significa que um caminho válido foi encontrado a partir daquele vizinho, então o `True` é propagado para cima (retornado para a chamada anterior).
    * **Passo 4 (Backtrack):** Se o loop `for` (Passo 3) terminar sem que nenhum vizinho leve a uma solução (ou seja, todas as chamadas recursivas retornaram `False`), significa que o vértice atual `v` não pode fazer parte do caminho *a partir deste ponto*. O algoritmo então "retrocede":
        * O vértice `v` é removido da lista `caminho` (`self.caminho.pop()`).
        * O vértice `v` é removido do conjunto `visitado` (`visitado.remove(v)`).
        * A função retorna `False`, sinalizando para a chamada anterior que este ramo da busca falhou.

### Algoritmo com Exlicações

```python
# main.py

class Grafo:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(num_vertices)]
        self.caminho = []

    def adicionar_aresta(self, u, v):
        # Para grafos não orientados
        self.adj[u].append(v)
        self.adj[v].append(u)

    def buscar_caminho_util(self, v, visitado):
        """
        Função recursiva de backtracking para encontrar o caminho.
        """
        # 1. Adiciona o vértice atual ao caminho e marca como visitado
        self.caminho.append(v)
        visitado.add(v)

        # 2. Base de Sucesso: Se o caminho contém todos os vértices
        if len(self.caminho) == self.V:
            return True # Encontrou um Caminho Hamiltoniano

        # 3. Recursão: Tenta visitar todos os vizinhos
        for vizinho in self.adj[v]:
            if vizinho not in visitado:
                # Chama recursivamente para o vizinho
                if self.buscar_caminho_util(vizinho, visitado):
                    return True # Propaga o sucesso

        # 4. Backtrack: Se nenhum vizinho levou a uma solução
        # Remove o vértice atual do caminho e desmarca como visitado
        self.caminho.pop()
        visitado.remove(v)
        
        return False # Indica que este caminho falhou

    def encontrar_caminho_hamiltoniano(self):
        """
        Função principal que tenta encontrar o caminho a partir de cada vértice.
        """
        visitado = set()

        # Tenta começar de cada vértice
        for inicio in range(self.V):
            self.caminho = [] # Reseta o caminho para cada nova tentativa
            visitado.clear() # Limpa os visitados

            if self.buscar_caminho_util(inicio, visitado):
                print("Caminho Hamiltoniano encontrado:")
                print(self.caminho)
                return True

        print("Nenhum Caminho Hamiltoniano existe neste grafo.")
        return False

# --- Exemplo de Teste ---
# Teste com grafos pequenos, como sugerido 
if __name__ == "__main__":
    
    # Exemplo 1: Grafo que TEM um caminho
    print("--- Teste 1 ---")
    g1 = Grafo(5)
    g1.adicionar_aresta(0, 1)
    g1.adicionar_aresta(1, 2)
    g1.adicionar_aresta(2, 3)
    g1.adicionar_aresta(3, 4)
    g1.adicionar_aresta(1, 3) # Adicionando mais algumas arestas
    g1.adicionar_aresta(1, 4)
    g1.encontrar_caminho_hamiltoniano() # Deve encontrar (ex: 0, 1, 2, 3, 4)

    print("\n--- Teste 2 ---")
    # Exemplo 2: Grafo que NÃO TEM um caminho
    g2 = Grafo(4)
    g2.adicionar_aresta(0, 1)
    g2.adicionar_aresta(0, 2)
    g2.adicionar_aresta(0, 3)
    g2.encontrar_caminho_hamiltoniano() # Não deve encontrar
```

## 2. Como executar o projeto

Para executar o projeto em seu ambiente local, siga os passos abaixo:

1.  Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/gabrieltinoco/trabalho-individual-3-fpaa.git
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd trabalho-individual-3-fpaa
    ```

3.Execute o arquivo `main.py` usando Python 3:
    ```bash
    python main.py
    ```
    (Ou `python3 main.py`, dependendo da sua configuração de ambiente)

## 3. Relatório Técnico

Este relatório apresenta as análises sobre o algoritmo implementado.

### 1. Análise da complexidade computacional.

**Classes P, NP, NP-Completo e NP-Difícil**.

O problema do Caminho Hamiltoniano se enquadra nas seguintes classes de complexidade:

*Classe NP (Nondeterministic Polynomial time):** O problema **está em NP**. A justificativa é que, embora *encontrar* um caminho seja difícil, *verificar* uma solução (um "certificado") é rápido. Se recebermos um suposto caminho, podemos verificar em tempo polinomial ( $O(V)$ , onde $V$ é o número de vértices) se ele é válido, ou seja, se ele contém todos os vértices exatamente uma vez e se todas as arestas no caminho existem no grafo.

* **Classe NP-Difícil (NP-Hard):** O problema é **NP-Difícil**. Um problema é NP-Difícil se ele for pelo menos tão difícil quanto qualquer problema em NP. O problema do Caminho Hamiltoniano é redutível a partir de outros problemas NP-Completos (como o Problema de Satisfatibilidade Booleana - SAT) e também pode ser usado como base para problemas mais complexos.

* **Classe NP-Completo:** Como o problema está em **NP** e também é **NP-Difícil**, ele é classificado como **NP-Completo**.

* **Relação com o Problema do Caixeiro Viajante (TSP):** O Problema do Caixeiro Viajante (TSP) pergunta qual é o *caminho mais curto* que visita todas as cidades (vértices) e retorna à origem. O problema do Caminho Hamiltoniano pode ser visto como um subproblema ou uma simplificação do TSP (onde queremos apenas saber se *existe* um caminho, sem nos preocupar com o custo ou em retornar à origem). Como o TSP é NP-Difícil, isso reforça a classificação do Caminho Hamiltoniano como um problema computacionalmente difícil.

* **Classe P:** Não se sabe se o problema está na classe **P** (problemas resolvíveis em tempo polinomial). Se um algoritmo de tempo polinomial fosse encontrado para o Caminho Hamiltoniano, isso provaria que $P = NP$, que é o maior problema em aberto da ciência da computação.

### 2. Análise da complexidade assintótica de tempo 

* **Complexidade Temporal:** A complexidade de tempo do algoritmo de backtracking implementado é, no pior caso, $O(V!)$ (V fatorial), onde $V$ é o número de vértices.

* **Determinação da Complexidade:** O método utilizado foi a análise da árvore de recursão. A função `encontrar_caminho_hamiltoniano` pode iniciar a busca a partir de $V$ vértices. Em cada chamada recursiva (`buscar_caminho_util`), o algoritmo tenta visitar todos os vizinhos não visitados.
    * No pior caso (como um grafo completo), a primeira chamada tem $V-1$ opções de vizinhos.
    * A segunda chamada recursiva terá $V-2$ opções.
    * A terceira terá $V-3$ opções, e assim por diante.
    * Isso leva a uma árvore de busca cujo número de folhas (possíveis caminhos) é da ordem de $V \times (V-1) \times (V-2) \times ... \times 1$, o que define a complexidade fatorial $O(V!)$.

### 3. Aplicação do Teorema Mestre 

* **É possível aplicar o Teorema Mestre?** Não, não é possível aplicar o Teorema Mestre ao algoritmo de backtracking para o Caminho Hamiltoniano.

* **Justificativa:** O Teorema Mestre é uma ferramenta para analisar a complexidade de algoritmos de "dividir para conquistar" que seguem uma recorrência específica da forma $T(n) = aT(n/b) + f(n)$.
    * $a$: número de subproblemas (deve ser constante).
    * $n/b$: tamanho de cada subproblema (o problema original $n$ é dividido por um fator $b$).
    
    Nosso algoritmo de backtracking não se encaixa nesse modelo:
    1.  O tamanho do subproblema não é $n/b$; ele diminui em 1 ( $T(n)$ depende de $T(n-1)$).
    2.  O número de subproblemas ( $a$) não é constante; ele depende do número de vizinhos não visitados do vértice atual, variando em cada etapa da recursão.

### 4. Análise dos casos de complexidade 

* **Pior Caso:** $O(V!)$. Ocorre em grafos muito densos (como um grafo completo), onde, a partir de qualquer vértice, existem muitos caminhos possíveis. O algoritmo é forçado a explorar um número fatorial de permutações antes de encontrar uma solução ou determinar que nenhuma existe.

* **Melhor Caso:** $O(V)$. Ocorre em um cenário ideal. Por exemplo, se o grafo for simplesmente um caminho linear (ex: 0-1-2-3-4) e a busca começar no vértice `0`. O algoritmo encontrará o caminho de primeira, sem nunca precisar retroceder (backtrack).

* **Caso Médio:** A análise do caso médio é extremamente complexa, mas a complexidade permanece exponencial. O desempenho depende muito da densidade (número de arestas) e da estrutura do grafo.

* **Impacto no Desempenho:** A diferença entre os casos é extrema. O melhor caso $O(V)$ é rápido e eficiente. No entanto, o pior caso $O(V!)$ torna o algoritmo completamente inviável para grafos de tamanho moderado (ex: com $V > 20$ , $V!$ é um número astronomicamente grande). Isso demonstra na prática por que problemas NP-Completos são considerados "difíceis" ou "intratáveis" computacionalmente.
