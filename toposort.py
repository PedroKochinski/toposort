import sys
import networkx as nx
import pygraphviz as pgv

# Função para criar o grafo usando o formato dot como entrada
def criar_grafo(dot):
    grafo = nx.DiGraph(pgv.AGraph(string=dot))
    return grafo

# Função para realizar uma busca em profundidade (DFS) e calcular a ordenação
def dfs_pos_ordem(grafo, vertice, visitados, ordenacao):
    visitados.add(vertice)
    for vizinho in grafo.successors(vertice):
        if vizinho not in visitados:
            dfs_pos_ordem(grafo, vizinho, visitados, ordenacao)
    ordenacao.insert(0, vertice)

# Função para resolver a ordenação topológica a partir da pós-ordem
def ordenacao_topologica_pos_ordem(grafo):
    visitados = set()
    ordenacao = []
    for vertice in grafo.nodes():
        if vertice not in visitados:
            dfs_pos_ordem(grafo, vertice, visitados, ordenacao)
    return ordenacao

def main():
    dot = sys.stdin.read()

    grafo = criar_grafo(dot)
    componentes_conexas = list(nx.weakly_connected_components(grafo))
    ciclos = list(nx.simple_cycles(grafo))

    if ciclos:
        print("Grafo inválido: contém ciclos", file=sys.stderr)
        exit(1)

    if len(componentes_conexas) > 1:
        with open("saida.txt", "w") as arquivo_saida:
            for componente in componentes_conexas:
                subgrafo = grafo.subgraph(componente)
                ordenacao = ordenacao_topologica_pos_ordem(subgrafo)
                ordenacao = list(ordenacao)  # Converter para lista
                ordenacao_str = ' '.join(ordenacao)
                arquivo_saida.write(ordenacao_str + '\n')
    else:
        ordenacao = ordenacao_topologica_pos_ordem(grafo)
        ordenacao = list(ordenacao)  # Converter para lista
        ordenacao_str = ' '.join(ordenacao)
        with open("saida.txt", "w") as arquivo_saida:
            arquivo_saida.write(ordenacao_str)


if __name__ == "__main__":
    main()

