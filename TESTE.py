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

# Listar a biblioteca:
def visualizar_biblioteca():
        print()
        print('=' * 150)
        print(f"{'Código':^30}{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
        print('-' * 150)

        for codigo, livro in enumerate(biblioteca):
            print(f"{codigo:^30}{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
        print('=' * 150)
        print()

# Função que adiciona um livro na lista:
def adicionando_livro():
    while True:
        nome_livro = input('Qual o nome do livro? ')

        autor = input('Quem é o autor? ')

        categoria = input('Escolha pelo código as seguintes opções: \n[1] Ação\n[2] Comédia\n[3] Ficção\n[4] Terror\n[5] Romance\n[6] Drama\nQual categoria escolhida: ')
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

        while True:
            try:
                preco = float(input('Qual o preço do livro? R$'))
                break
            except ValueError:
                print('Precisamos de um valor numérico para o preço ')

        novo_livro = {'nome': nome_livro, 'autor': autor, 'categoria': categoria, 'preco': preco}
        biblioteca.append(novo_livro)
        salvar_em_csv(biblioteca, nome_arquivo)

        # Pergunta se deseja adicionar mais outro livro:
        pergunta = input('Nat, você deseja adicionar mais algum livro? [S/N] ')

        # Tratamento, caso a resposta fuja do esperado (S ou N):
        # Tratamento para garantir uma resposta válida:
        while pergunta.lower() not in ['s', 'n']:
            pergunta = input('Ops... A resposta não é válida. Escreva uma resposta válida: [S/N] ')

            if pergunta.lower() in ['s', 'n']:
                break

        if pergunta.lower() == 's':
            continue
        elif pergunta.lower() == 'n':
            break
            
        

# Função para excluir um livro com base no código:
def excluir_livro(codigo):

    if codigo >= 0 and codigo < len(biblioteca):
        livro_excluído = biblioteca.pop(codigo)
        salvar_em_csv(biblioteca, nome_arquivo)
        print(f'O livro "{livro_excluído["nome"]}" foi excluído.')
                
    else:
        print('Código inválido. Nenhum livro foi excluído.')

# Função de filtragem
def filtros():
    print('Dê uma olhadinha geral, fica mais fácil de se lembrar :)')
    print()
    if len(biblioteca) < 1:
            print('Ainda não foi adicionado nenhum livro :(\nAdicione um livro na opção [2]')
            print()
    else:
        visualizar_biblioteca()
    
    while True:
        print('Escolha, pelo código, as seguintes opções: ')
        print('[1] Filtrar pelo nome')
        print('[2] Filtrar pelo autor')
        print('[3] Filtrar pela categoria')
        print('[4] Filtrar pelo preço\n')

        # A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
        escolha = input('Insira o código do filtro desejado: ')

        # 1 - Filtrar pelo nome
        if escolha == '1':
            nome_escolhido = input('\nDigite o nome do livro que você está procurando: ')
            filtro_nome(nome_escolhido)
            break

        # 2 - Filtrar pelo autor
        elif escolha == '2':
            autor_escolhido = input('\nDigite o nome do autor do livro que você está procurando: ')
            filtro_autor(autor_escolhido)
            break

        # 3 - Filtrar pela categoria
        elif escolha == '3':
            print('Escolha, pelo código, a categoria de livro que você deseja procurar: ')
            print('[1] Ação')
            print('[2] Comédia')
            print('[3] Ficção')
            print('[4] Terror')
            print('[5] Romance')
            print('[6] Drama\n')
            categoria_escolhida = input('Pelo código, qual a categoria escolhida para filtrar: ')
            
            if categoria_escolhida == '1':
                categoria_escolhida = 'Ação'
            elif categoria_escolhida == '2':
                categoria_escolhida = 'Comédia'
            elif categoria_escolhida == '3':
                categoria_escolhida = 'Ficção'
            elif categoria_escolhida == '4':
                categoria_escolhida = 'Terror'
            elif categoria_escolhida == '5':
                categoria_escolhida = 'Romance'
            elif categoria_escolhida == '6':
                categoria_escolhida = 'Drama'
            else:
                # Tratamento de erro em categoria, caso tenha adicionado algo errado:
                while categoria_escolhida not in ['1', '2', '3', '4', '5', '6']:
                    categoria_escolhida = input('Ops... A resposta não é válida. Escreva uma resposta válida: ')
            
            filtro_categoria(categoria_escolhida)
            break

        # 4 - Filtrar pelo preço
        elif escolha == '4':
            preco_escolhido = float(input('Qual o preço do livro que você está procurando? R$ '))
            filtro_preco(preco_escolhido)
            break

#  Filtro pelo nome
def filtro_nome(nome_escolhido):
    nome_encontrado = False
    print(f"{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
    print('=' * 150)
    for livro in biblioteca:
        if nome_escolhido.lower() in livro['nome'].lower():
            nome_encontrado = True
            print(f"{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
    if not nome_encontrado:
        print(f"Nenhum livro contendo '{nome_escolhido}' foi encontrado na biblioteca.")
    print('=' * 150)

#  Filtro pelo autor
def filtro_autor(autor_escolhido):
    autor_encontrado = False
    print(f"{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
    print('=' * 150)
    for livro in biblioteca:
        if autor_escolhido.lower() in livro['autor'].lower():
            autor_encontrado = True
            print(f"{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
    if not autor_encontrado:
        print(f"Nenhum livro com o autor '{autor_escolhido}' foi encontrado na biblioteca.")
    print('=' * 150)

#  Filtro por categoria
def filtro_categoria(categoria_escolhida):
    categoria_encontrada = False
    print(f"{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
    print('=' * 150)
    for livro in biblioteca:
        if livro['categoria'] == categoria_escolhida:
            categoria_encontrada = True
            print(f"{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
    if not categoria_encontrada:
        print(f"A categoria '{categoria_escolhida}' não foi encontrada na biblioteca.")
    print('-' * 150)

# Filtro por preço
def filtro_preco(preco_escolhido):
    preco_encontrado = False
    print(f"{'Livro':^30}{'Autor':^30}{'Preço':^30}{'Categoria':^30}")
    print('=' * 150)
    print("Livros com o preço escolhido: ")
    for livro in biblioteca:
        if livro['preco'] == preco_escolhido:
            preco_encontrado = True
            print(f"{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}{livro['categoria']:^30}")
    if not preco_encontrado:
        print(f"Nenhum livro com o preço {preco_escolhido} R$ foi encontrado na biblioteca.")
    print('=' * 150)

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
    print('[4] Filtro de listagem de livros')
    print('[5] Exibir extrato')
    print('[6] Sair')

    # A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
    escolha = input('O que deseja: ')

    # 1 - Visualização da biblioteca
    if escolha == '1':
        visualizar_biblioteca()

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
            print()
            print('Livros disponíveis para exclusão:')
            print()
            
            visualizar_biblioteca()

            while True: # Tratamento de erro: Opção não inteiro

                try:
                    codigo = int(input('Digite o código do livro que deseja excluir: '))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um valor numérico válido.")
                    
            excluir_livro(codigo)
            print()

    # 4 - Filtrar por categoria
    elif escolha == '4':
        filtros()
        print()

    # 5 - Exibir Extrato
    elif escolha == '5':
        exibir_extrato("bibli.csv")
        print()

    # 6 - Saindo do programa
    elif escolha == '6':
        break

print(f"{'Tchau até mais':^30}")

os.system('cls')
