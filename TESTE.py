import os

os.system('cls')

print('  ~' * 9)
print('     Biblioteca do Gheyson')
print('  ~' * 9)

# 1.0 Criando a lista
biblioteca = []

nome_arquivo = "bibli.csv"

# Função para carregar a biblioteca a partir do arquivo CSV
def carregar_biblioteca():
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            linhas = arquivo_csv.readlines()
            if len(linhas) < 2:
                print('A biblioteca está vazia. Adicione livros na opção [2].')
            else:
                for linha in linhas[1:]:  # Começa da segunda linha (índice 1)
                    valores = linha.strip().split(',')
                    livro = {
                        'nome': valores[0],
                        'autor': valores[1],
                        'categoria': valores[2],
                        'preco': float(valores[3])
                    }
                    biblioteca.append(livro)
    except FileNotFoundError:
        print(f'O arquivo CSV "{nome_arquivo}" não foi encontrado. Adicione livros na opção [2].')

# Chama a função para carregar a biblioteca no início do programa
carregar_biblioteca()  

# Função que salva no csv os dados da lista:
def salvar_em_csv(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_csv:
        # Escreve o cabeçalho
        arquivo_csv.write("Nome,Autor,Categoria,Preco\n")

        # Escreve os dados
        for livro in lista:
            linha = f"{livro['nome']},{livro['autor']},{livro['categoria']},{livro['preco']:.3f}\n"
            arquivo_csv.write(linha)

# Função que adiciona um livro na lista:
def adicionando_livro():
    while True:
        nome_livro = input('Qual o nome do livro? ')

        autor = input('Quem é o autor? ')

        categoria = input('Escolha pelo código as seguintes opções: \n[1] Ação\n[2] Comédia\n[3] Ficção\n[4] Terror\n[5] Romance\n[6] Drama\n Qual categoria escolhida: ')
        categoria_dic = {
            "1": "Ação",
            "2": "Comédia",
            "3": "Ficção",
            "4": "Terror",
            "5": "Romance",
            "6": "Drama"
        }
        # Tratamento de erro em categoria, caso tenha adicionado algo errado:
        while True:
            if categoria in ['1', '2', '3', '4', '5', '6']:
                categoria = categoria_dic[categoria]
                print('Categoria adicionada')
                break
            else:
                categoria = input('Digite uma resposta válida: ')

        preco = float(input('Qual o preço do livro? '))

        novo_livro = {'nome': nome_livro, 'autor': autor, 'categoria': categoria, 'preco': preco}
        biblioteca.append(novo_livro)
        salvar_em_csv(biblioteca, nome_arquivo)

        # Pergunta se deseja adicionar mais outro livro:
        pergunta = input('Nat, você deseja adicionar mais algum livro? [S/N] ')

        # Tratamento, caso a resposta fuja do esperado (S ou N):
        if pergunta in 'Ss':
            continue
        elif pergunta in 'Nn':
            break
        else:
            while pergunta not in 'SsNn':
                pergunta = input('Ops... A resposta não é válida. Escreva uma resposta válida: [S/N] ')

# Função para excluir um livro com base no código:
def excluir_livro(codigo):
    if codigo >= 0 and codigo < len(biblioteca):
        livro_excluído = biblioteca.pop(codigo)
        salvar_em_csv(biblioteca, nome_arquivo)
        print(f'O livro "{livro_excluído["nome"]}" foi excluído.')
    else:
        print('Código inválido. Nenhum livro foi excluído.')

# Fazendo o filtro por categoria:
def filtro_categoria(categoria_escolhida):
    categoria_encontrada = False
    for livro in biblioteca:
        if livro['categoria'] == categoria_escolhida:
            categoria_encontrada = True
            print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Preço: {livro['preco']:.3f}")
    if not categoria_encontrada:
        print(f"A categoria '{categoria_escolhida}' não foi encontrada na biblioteca.")

# Função para exibir o extrato dos preços:
def exibir_extrato(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo_csv:
            linhas = arquivo_csv.readlines() #linhas = lista que contêm as linhas do arquivo CSV

            if len(linhas) > 1:
                print("\nExtrato dos preços:\n")
                print("=" * 50)
                print("Livro\t\t\tPreço")
                print("-" * 50)

                preco_total = 0 
                
                #linha = string que contém uma linha do arquivo CSV
                for linha in linhas[1:]:
                    dados = linha.strip().split(',') #dados = lista que resulta da divisão (split)
                    nome_livro = dados[0] # dados [0] = nome do livro ... dados [3] = preço do livro
                    preco = float(dados[3]) 
                    preco_total += preco
                    print(f"{nome_livro}\t\tR$ {preco:.2f}")

                print("-" * 50)
                print(f"Total de livros: {len(linhas) - 1}")
                print(f"Soma dos preços: R$ {preco_total:.2f}")
            else:
                print("\nAinda não foi adicionado nenhum livro :( Adicione livros na opção [3].\n")


# Criando o menu:
while True:
    print('Escolha, pelo seu código, as seguintes opções: ')
    print('[1] Listar livros')
    print('[2] Adicionar livro')
    print('[3] Deletar livro')
    print('[4] Filtro de livros por categoria')
    print('[5] Exibir extrato')
    print('[6] Sair')

    # A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
    escolha = input('O que deseja: ')

    # 1.1 Visualização da biblioteca
    if escolha == '1':
        if len(biblioteca) < 1:
            print('Ainda não foi adicionado nenhum livro :(\nAdicione um livro na opção [2]')
            print()
        else:
            print()
            print('=' * 150)
            print(f"{'Código':^30}{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
            print('-' * 150)

            for codigo, livro in enumerate(biblioteca):
                print(f"{codigo:^30}{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
            print('=' * 150)
            print()

    # 1.2 Chamando a função ADICIONANDO_LIVRO:
    elif escolha == '2':
        adicionando_livro()
        print()

    # 1.3 Deletar livro
    elif escolha == '3':
        if len(biblioteca) < 1:
            print('Não há livros para excluir.')
            print()
        else:
            print('Livros disponíveis para exclusão:')
            print()
            print('=' * 150)
            print(f"{'Código':^30}{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
            print('-' * 150)

            for codigo, livro in enumerate(biblioteca):
                print(f"{codigo:^30}{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
            print('=' * 150)
            print()
            codigo = int(input('Digite o código do livro que deseja excluir: '))
            excluir_livro(codigo)
            print()

    # 1.4 Filtrar por categoria
    elif escolha == '4':
        categoria_escolhida = input('Está procurando um livro? \nMe diga a categoria escolhida: ')
        filtro_categoria(categoria_escolhida)

    # 1.5 Exibindo extrato
    elif escolha == '5':
        exibir_extrato("bibli.csv")
        print()

    # 1.6 Saindo do programa
    elif escolha == '6':
        break

print(f"{'Tchau até mais':^30}")
