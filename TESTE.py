import os
os.system('cls')

print('  ~' * 9)
print('     Biblioteca do Gheyson')
print('  ~' * 9)

# 1.0 Criando a lista 
biblioteca = []


# 1.3 função ADICIONANDO_LIVRO:
def adicionando_livro():
    nome_arquivo = "bibli.csv"
    cabecalho_ja_escrito = os.path.isfile(nome_arquivo)  # Verifica se o arquivo já existe

    while True:
        nome_livro = input('Qual o nome do livro? ')
        autor = input('Quem é o autor? ')
        categoria = input('Qual a sua categoria? ')
        preco = float(input('Qual o preço do livro? '))

        novo_livro = {'nome': nome_livro, 'autor': autor, 'categoria': categoria, 'preco': preco}
        biblioteca.append(novo_livro)

        # Salvar o livro automaticamente em um arquivo .csv
        with open(nome_arquivo, 'a') as arquivo_csv:
            if not cabecalho_ja_escrito:
                arquivo_csv.write("Nome,Autor,Categoria,Preco\n")
                cabecalho_ja_escrito = True

            linha = f"{novo_livro['nome']},{novo_livro['autor']},{novo_livro['categoria']},{novo_livro['preco']:.2f}\n"
            arquivo_csv.write(linha)
            biblioteca.append(arquivo_csv)

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
nome_arquivo = "bibli.csv"

def atualizar():
    nome_arquivo='bibli.csv'
    with open(nome_arquivo, 'w') as arquivo:
        conteudo=arquivo.read()
        linhas=conteudo.split('\n')
        bibli=[linha.split(',') for linha in linhas]
    while True:
        print("bibilioteca")
        for i,linha in enumerate(bibli):
            print(f'1-)nome do livro,2-)ator,3-)categoria,4-)preço')
            print(f'{i}: {linha[1:]}')
        linha=int(input('digite o numero do livro que deseja mudar:'))
        coluna=int(input('digite a informação que deseja mudar:'))
        novo=input('digite a nova informação:')
        bibli[linha][coluna]=novo
        with open (nome_arquivo, 'w') as arquivo:
            os.remove(nome_arquivo)
            arquivo.write(bibli)
        decisao=input('deseja atualizar mais algum livro [S][N]? ')
        if decisao in 'Nn':
            break
#1.1 Criando o menu:
while True:
    print('Escolha, pelo seu código, as seguintes opções: ')
    print('[1] Listar livros')
    print('[2] Atualizar')
    print('[3] Adicionar livro')
    print('[4] Sair')
    
    #A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
    escolha = input('O que deseja: ')
    
    #1.1Visualização da biblioteca
    if escolha == '1':
        if len(biblioteca) < 1:
                print('Ainda não foi adicionado nenhum livro :(\nAdicione um livro na opção [3]')
                print()
        else:
            print()
            print('='*150)
            print(f"{'Código':^30}{'Livro':^30}{'Autor':^30}{'Preço':^30}")
            print('-'*150)

            for codigo, livro in enumerate(biblioteca):
                print(f"{codigo:^30}{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}")
            print('='*150)
            print()
    #1.2Salvando em arquivo CSV
    elif escolha == '2':
        atualizar()
        print()
        
        
        

        
                
                
                      
    #1.3Chamando a função ADICIONANDO_LIVRO:
    elif escolha == '3':
        adicionando_livro()
        print()
    
    #1.4Saindo do programa
    elif escolha == '4':
        break

print()
print(f"{'Tchauu Até Mais':^30}")