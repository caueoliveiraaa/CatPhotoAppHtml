# Importando bibliotecas Python
import sqlite3
import os

# Limpar terminal
os.system('cls')

# Conectar com base de dados
conexao = sqlite3.connect('mydatabase.db')
print('Conexão com banco de dados criada com sucesso!')
cursor = conexao.cursor()

# Mensagem para CRUD
opcoes = '\nEscholha uma operação abaixo:'
opcoes += '\n1 - Selecionar'
opcoes += '\n2 - Deletar'
opcoes += '\n3 - Atualizar'
opcoes += '\n4 - Inserir'
opcoes += '\n5 - Sair'
opcoes += '\nInforme a opção: '

# While que rodará o programa
while True:
    # Selecionar o tipo de operação
    operacao = input(opcoes) 

    # Verificar a operação selecionada 
    if operacao == '1':
        os.system('cls')
        cursor.execute(f'''
            SELECT * FROM usuarios 
        ''')

        # Atribuir resultado do SELECT a uma variável com fetchall
        resultados = cursor.fetchall()

        # Mostrar resultado retornado do SQL com um laço for
        for linha in resultados:
            print(linha)

    elif operacao == '2':
        # Ler id da coluna a deletar
        id_linha = input('Informe o ID da coluna a deletar: ')             
        id_linha = int(id_linha)
        os.system('cls')

        # Deletar linha onde o id bate como id informado
        cursor.execute(f'''
            DELETE FROM usuarios 
            WHERE id = {id_linha};
        ''')

        print(f'Linha {id_linha} excluída com sucesso!')
    
    elif operacao == '3':
        # Ler id da coluna a atualizar
        id_linha = input('Informe o ID da coluna a alterar: ')             
        
        os.system('cls')
        id_linha = int(id_linha)

        # Ler os dados novos
        nome_novo = input('Informe o novo nome do usuário: ')             
        email_novo = input('Informe o novo e-mail do usuário: ')             
        idade_nova = input('Informe a nova idade do usuário: ')             
        idade_nova = int(idade_nova)

        # Validar os dados e inserir os mesmos caso sejam válidos
        if len(nome_novo) > 3 and idade_nova > 0 and '@' in email_novo:
            cursor.execute(f'''
                UPDATE usuarios 
                SET nome = '{nome_novo}', idade = {idade_nova}, email = '{email_novo}' 
                WHERE id = {id_linha};
            ''')
            
            print(f'Dados atualizados com sucesso em id = {id_linha}!')
        else:
            print('Informe dados válidos para serem atualizados!')

    elif operacao == '4':
        # Ler os dados novos
        nome_novo = input('Informe o nome do usuário: ')             
        email_novo = input('Informe o e-mail do usuário: ')             
        idade_nova = input('Informe a idade do usuário: ')             
        
        os.system('cls')
        idade_nova = int(idade_nova)

        # Validar os dados e inserir os mesmos caso sejam válidos
        if len(nome_novo) > 3 and idade_nova > 0 and '@' in email_novo:
            cursor.execute(f'''
                INSERT INTO usuarios (nome, idade, email)
                VALUES ('{nome_novo}', {idade_nova}, '{email_novo}');
            ''')
            
            print(f'Dados {nome_novo}, {idade_nova}, e {email_novo} inseridos com sucesso!')
        else:
            print('Informe dados válidos para serem inseridos!')

    elif operacao == '5':
        print('Programa parou.')
        break

    else:
        print('Informe uma operação válida.')
    
# Comitar mudanças e finalizar programa
conexao.commit()
print('Dados comitados com sucesso!')
conexao.close()
print('Conexão com base de dados fechada com sucesso.')