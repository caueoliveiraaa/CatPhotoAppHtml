# CLASS 5:
        Structure:
        1 - Classe
        2 - Atributo
        3 - Método
        4 - Objeto
        5 - Exercícios

# Exercícios:
        1 - Classe Conta Bancária:
        Crie uma classe chamada ContaBancaria que simule uma conta bancária simples.
        A classe deve ter os atributos titular, saldo e numero. Crie métodos para depositar (depositar(valor))
        e sacar (sacar(valor)) dinheiro da conta, além de um método para exibir o saldo atual (exibir_saldo()).

        2 - Classe Livro:
        Crie uma classe chamada Livro que represente um livro.
        A classe deve ter os atributos titulo, autor e ano. Crie um método para exibir as informações do livro (exibir_informacoes()).

        3 - Classe Carro:
        Crie uma classe chamada Carro que simule um carro. A classe deve ter os atributos marca, modelo e ano.
        Crie métodos para ligar (ligar()), desligar (desligar()) e exibir as informações do carro (exibir_informacoes()).

        4 - Classe Agenda:
        Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter um atributo para armazenar uma lista de contatos.
        Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).

        5 - Classe Triângulo:
        Crie uma classe chamada Triangulo que represente um triângulo. A classe deve ter os atributos lado1, lado2 e lado3.
        Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()), calcular o perímetro (calcular_perimetro())
        e exibir o tipo do triângulo com base nos lados (tipo_triangulo()).

        6 - Classe Aluno:
        Crie uma classe chamada Aluno que represente um aluno. A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
        Crie métodos para calcular a média (calcular_media()) e exibir o status do aluno com base na média (exibir_status()).

        7 - Classe Banco:
        Crie uma classe chamada Banco que represente um banco. A classe deve ter atributos para armazenar uma lista de contas bancárias.
        Crie métodos para adicionar (criar_conta(titular, saldo_inicial)), remover (encerrar_conta(numero)), exibir o total de saldo de todas as contas (total_saldo()).


# Class 6:
	Structure:
        1 - Conceito de encapsulamento
        2 - Public, private, protected e default
        3 - Get e Set
        4 - Construtor
        5 - Exercícios
        6 - Upload

# Exercícios:
        1 - Classe Produto:
        Crie uma classe chamada Produto que represente um produto em uma loja. A classe deve ter os atributos: nome (private), preco (protected)
        e codigo (public). Crie um construtor para inicializar esses atributos e métodos get_nome(), get_preco() e set_preco(novo_preco) para
        acessar e modificar o preço.

        2 - Classe Pessoa:
        Crie uma classe chamada Pessoa com o atributo nome (public). Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.

        3- - Classe Conta Bancária com Protected:
        Expanda o exercício da classe ContaBancaria do exercício anterior. Agora, torne o atributo saldo protected. Crie métodos get_saldo() e set_saldo(novo_saldo)
        para acessar e modificar o saldo.

        4 - Classe Funcionário:
        Crie uma classe chamada Funcionario com os atributos nome (private), salario (protected) e cargo (public). Crie métodos para definir o nome
        (set_nome(novo_nome)), obter o nome (get_nome()), calcular aumento de salário (aumentar_salario(aumento)) e exibir informações completas do
        funcionário (exibir_informacoes()).

        5 - Classe Triângulo com Getters e Setters:
        Expanda o exercício da classe Triangulo. Torne os atributos lado1, lado2 e lado3 private. Crie métodos get_lado1(), get_lado2() e get_lado3()
        para acessar os lados e métodos set_lado1(novo_lado), set_lado2(novo_lado) e set_lado3(novo_lado) para modificar os lados. No método eh_valido(),
        verifique se os lados formam um triângulo válido.

        6 - Classe Livro com Construtor:
        Refaça o exercício da classe Livro. Crie um construtor que aceite os parâmetros titulo, autor e ano. Crie métodos get_titulo(), get_autor()
        e get_ano() para acessar esses atributos.

        7 - Classe Veículo:
        Crie uma classe chamada Veiculo com os atributos marca (protected), modelo (protected) e ano (private). Crie um construtor para inicializar 
        esses atributos. Implemente métodos get_marca(), get_modelo() e exibir_informacoes().

        8 - Classe Escola:
        Crie uma classe chamada Escola. Defina um atributo alunos como private (uma lista vazia no construtor). Crie métodos para adicionar
        (adicionar_aluno(aluno)), remover (remover_aluno(aluno)) e exibir a lista de alunos (exibir_alunos()).

        9 - Classe Animal com Default Visibility:
        Crie uma classe chamada Animal. Defina um atributo especie com visibilidade default. Crie métodos get_especie() e set_especie(nova_especie)
        para manipular esse atributo.

        10 - Classe Hotel com Getters e Setters:
        Crie uma classe chamada Hotel. Defina um atributo nome (private) e estrelas (public). Crie métodos get_nome(), set_nome(novo_nome) e get_estrelas()
        para acessar e modificar esses atributos.
