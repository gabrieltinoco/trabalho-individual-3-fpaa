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
            return True  # Encontrou um Caminho Hamiltoniano

        # 3. Recursão: Tenta visitar todos os vizinhos
        for vizinho in self.adj[v]:
            if vizinho not in visitado:
                # Chama recursivamente para o vizinho
                if self.buscar_caminho_util(vizinho, visitado):
                    return True  # Propaga o sucesso

        # 4. Backtrack: Se nenhum vizinho levou a uma solução
        # Remove o vértice atual do caminho e desmarca como visitado
        self.caminho.pop()
        visitado.remove(v)

        return False  # Indica que este caminho falhou

    def encontrar_caminho_hamiltoniano(self):
        """
        Função principal que tenta encontrar o caminho a partir de cada vértice.
        """
        visitado = set()

        # Tenta começar de cada vértice
        for inicio in range(self.V):
            self.caminho = []  # Reseta o caminho para cada nova tentativa
            visitado.clear()  # Limpa os visitados

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
    g1.adicionar_aresta(1, 3)  # Adicionando mais algumas arestas
    g1.adicionar_aresta(1, 4)
    g1.encontrar_caminho_hamiltoniano()  # Deve encontrar (ex: 0, 1, 2, 3, 4)

    print("\n--- Teste 2 ---")
    # Exemplo 2: Grafo que NÃO TEM um caminho
    g2 = Grafo(4)
    g2.adicionar_aresta(0, 1)
    g2.adicionar_aresta(0, 2)
    g2.adicionar_aresta(0, 3)
    g2.encontrar_caminho_hamiltoniano()  # Não deve encontrar