
-- Somando todas as idades 
SELECT SUM(idade) AS soma_das_idades
FROM Programadores;

-- Somando todos os ids
SELECT SUM(id) AS soma_dos_ids
FROM Programadores;


-- Selecionando idades entre 25 3 25
SELECT * FROM Programadores
WHERE idade BETWEEN 25 AND 35;


-- Selecionando ids entre 25 3 25
SELECT *FROM Programadores
WHERE idade BETWEEN 10 AND 20;


--  | -- EX -- |
-- Se não houverem dados para obter os dados dos exercícios
-- inserir manualmente com inert into

-- Selecionar os programadores com idades entre 25 e 30 anos:
SELECT * FROM Programadores
WHERE idade BETWEEN 25 AND 30;

-- Calcular a soma total das idades de todos os usuarios:
SELECT SUM(idade) AS SomaDasIdades FROM usuarios;

-- Selecionar os programadores com salários entre 5000 e 7000:
SELECT * FROM Programadores
WHERE salario BETWEEN 5000 AND 7000;

-- Calcular a soma total dos salários de todos os programadores:
SELECT SUM(salario) AS SomaDosSalarios FROM Programadores;

-- Selecionar os usuarios com ids entre 10 e 15:
SELECT * FROM usuarios
WHERE id BETWEEN 10 AND 15;

-- Calcular a soma total das horas trabalhadas por todos os programadores:
SELECT SUM(horas_trabalhadas) AS TotalHorasTrabalhadas
FROM Programadores;

-- Selecionar os programadores com idade entre 10 e 18:
SELECT *FROM Programadores
WHERE bonus BETWEEN 1000 AND 2000;

-- Calcular a soma total das idades da tabela contatos:
SELECT SUM(idade) AS total_idade
FROM contatos;

-- Selecionar os contatos com idades maiores que 18 mas menores que 30:
SELECT * FROM contatos
WHERE projetos_concluidos BETWEEN 5 AND 10;

