-- VIEWS: São 'tabelas virtuais' 
-- Em SQLite, uma view (visão) é uma tabela virtual
-- derivada de uma ou mais tabelas existentes. 
-- Ela se comporta como uma tabela regular, mas seu conteúdo
--  é gerado dinamicamente com base na definição da visão. 
-- As views permitem simplificar consultas complexas, encapsular lógica 
-- e fornecer uma interface consistente para os dados.

-- Criando uma wiew ProgramadoresView 
CREATE VIEW ProgramadoresView AS
SELECT id, nome, idade, email, linguagem FROM Programadores

-- Utilizando a view ProgramadoresView 
SELECT * FROM ProgramadoresView

-- Para deletar a view
DROP VIEW ProgramadoresView;

-- Criando uma view ProgramadoresUsuariosEmail
CREATE VIEW ProgramadoresUsuariosEmail AS
SELECT Programadores.nome AS Programador,
Programadores.email AS EmailMatch,
usuarios.nome AS Usuario
FROM Programadores LEFT JOIN usuarios
ON Programadores.email = usuarios.email;

-- Utilizando a view ProgramadoresUsuariosEmail
SELECT * FROM ProgramadoresUsuariosEmail;




-- Adicione a coluna status a tabela contatos
-- Preencha todas as linhas com valores 1 e 0 de forma aleatória
-- 1 representa que o contato é ativo, 0 é inativo
-- Crie uma view chamada "ProgramadoresAtivos" que mostrará
-- apenas os programadores que estão ativos.

CREATE VIEW ContatosAtivos AS
SELECT * FROM contatos
WHERE status = 1;

-- Selecione a view criada
SELECT * FROM ContatosAtivos




-- Crie uma view chamada "ProgramadoresPorLinguagem"
-- que agrupará os programadores por linguagem de programação, 
-- mostrando a contagem de programadores para cada linguagem.

-- Selecione a view criada



-- Crie uma view chamada SomaIdAndIdade que realizará
-- um select dando um sum na idade e no salario
-- e mostrando eles como soma_salario e soma_idade

-- Selecione a view criada



--- Crie uma view que realizará um select na tabela Programadores
-- e um left join na tabela usuários com base nos ids que são iguais  


-- Selecione a view criada
