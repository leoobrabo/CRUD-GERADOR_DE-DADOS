import random
from time import sleep
from ultilidades import apresentar_programa, vermelho, verde, azul, amarelo, separar_por_linha

lista_nomes = ['Leonardo', 'Rita', 'Heraclito', 'Luciene', 'Eric']

lista_emails = ['leonardomotta2020@hotmail.com', 'leomotta2000@gmail.com',
                'teste@gmail.com', 'usuario@gmail.com', 'teste@hotmail.com']

lista_telefones = ['99999-0000', '98888-0000',
                   '97777-0000', '96666-0000', '95555-0000']

lista_cidades = ['Brasilia', 'São Paulo',
                 'Rio de Janeiro', 'Minas Gerais', 'Goias']

lista_estados = ['DF', 'SP', 'RJ', 'MG', 'GO']


def salvar_arquivo(dados):
    with open('dados.txt', 'a', encoding='utf-8') as arquivo:
        conteudo = f'{dados}\n'
        arquivo.writelines(conteudo)


def escolha_aleatoria():
    aleatorio = random.randint(0, 4)
    return aleatorio


def aviso_de_licenca():
    amarelo('Funcionalidade para assinantes')
    vermelho('Entre em contato com o administrador')
    azul('leonardomotta2010@hotmail.com')
    sleep(2)


def menu():

    while True:
        verde(
            'Ultilize uma ou mais opções separadas por virgula para gerar dados aleatorios')
        separar_por_linha()
        print('')
        verde('[1] - Para gerar Nomes')
        verde('[2] - Para gerar emails')
        verde('[3] - Para gerar telefones')0
        verde('[4] - Para gerar cidades')
        verde('[5] - Para gerar estados')
        verde('[6] - Voltar')
        print('')
        aleatorio = escolha_aleatoria()
        escolha = input('Digite a Opção Desejada: ')

        if escolha == '6':
            amarelo('Abrindo Tela Inicial')
            break

        escolhas = escolha.split(',')

        salvar = input('Deseja salvar as opções (s/n) ')
        separar_por_linha()

        for i in escolhas:
            if i == '1':
                nome = lista_nomes[aleatorio]
                if salvar == 's':
                    verde(nome)

                    salvar_arquivo(nome)
                else:
                    azul(nome)

            elif i == '2':
                email = lista_emails[aleatorio]
                if salvar == 's':
                    verde(email)

                    salvar_arquivo(email)
                else:
                    azul(email)

            elif i == '3':
                telefone = lista_telefones[aleatorio]
                if salvar == 's':
                    verde(telefone)

                    salvar_arquivo(telefone)
                else:
                    azul(telefone)

            elif i == '4':
                cidade = lista_cidades[aleatorio]
                if salvar == 's':
                    verde(cidade)

                    salvar_arquivo(cidade)
                else:
                    azul(cidade)

            elif i == '5':
                estado = lista_estados[aleatorio]
                if salvar == 's':
                    verde(estado)

                    salvar_arquivo(estado)
                else:
                    azul(estado)

            else:
                vermelho('Opção Invalida')
                separar_por_linha()

            separar_por_linha()


def apresentar_menu():
    separar_por_linha()
    verde('[1] - Ultilizar o Gerador de dados')
    amarelo('[2] - Editar dados existente')
    vermelho('[3] - Excluir um dado')
    amarelo('[4] - Criar dado')
    vermelho('[5] - Sair')
    opcao = input('Digite uma opção: ')
    separar_por_linha()
    return opcao


if __name__ == '__main__':
    apresentar_programa()
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            menu()
        if opcao == '2':
            aviso_de_licenca()

        if opcao == '3':

            aviso_de_licenca()

        if opcao == '4':
            aviso_de_licenca()

        if opcao == '5':
            amarelo('Encerrando aplicação')
            break
