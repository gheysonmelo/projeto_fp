import os

os.system('cls')

print('  ~' * 9)
print('     Biblioteca do Gheyson')
print('  ~' * 9)

# Criando a lista e definindo uma variável para o nome do arquivo
biblioteca = []
nome_arquivo = "bibli.csv"

# Função para carregar a biblioteca a partir do arquivo CSV
def carregar_biblioteca():
    try:
        # Abre o arquivo CSV para leitura
        with open(nome_arquivo, 'r') as arquivo_csv:
            linhas = arquivo_csv.readlines()
            # 2 porque a primeira linha é o cabeçalho
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
        while True:
            if categoria in ['1', '2', '3', '4', '5', '6']:
                categoria = categoria_dic[categoria]
                break
            else:
                # Tratamento de erro em categoria, caso tenha adicionado algo errado:
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

# Função para excluir um livro com base no código
def excluir_livro(codigo):
    if codigo >= 0 and codigo < len(biblioteca):
        livro_excluído = biblioteca.pop(codigo)
        salvar_em_csv(biblioteca, nome_arquivo)
        print(f'O livro "{livro_excluído["nome"]}" foi excluído.')
    else:
        print('Código inválido. Nenhum livro foi excluído.')

# Fazendo o filtro por categoria
def filtro_categoria(categoria_escolhida):
    categoria_encontrada = False
    for livro in biblioteca:
        if livro['categoria'] == categoria_escolhida:
            categoria_encontrada = True
            print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Preço: {livro['preco']:.3f}")
    if not categoria_encontrada:
        print(f"A categoria '{categoria_escolhida}' não foi encontrada na biblioteca.")

# Criando o menu:
while True:
    print('Escolha, pelo seu código, as seguintes opções: ')
    print('[1] Listar livros')
    print('[2] Adicionar livro')
    print('[3] Deletar livro')
    print('[4] Filtro de livros por categoria')
    print('[5] Sair')

    # A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
    escolha = input('O que deseja: ')

    # 1 - Visualização da biblioteca
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

    # 2 - Adicionar livro:
    elif escolha == '2':
        adicionando_livro()
        print()

    # 3 - Deletar livro
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

    # 4 - Filtrar por categoria
    elif escolha == '4':
        categoria_escolhida = input('Está procurando um livro? \nMe diga a categoria escolhida: ')
        filtro_categoria(categoria_escolhida)

    # 5 - Sair do programa
    elif escolha == '5':
        break

print(f"{'Tchau Até Mais':^30}")
