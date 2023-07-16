-- Revisando comandos CREATE/DROP, DELETE, INSERT, WHERE, LIKE,
-- SELECT, AND, UPDATE, MIN, MAX, AVG, COUNT, etc.

-- Criar tabela
CREATE TABLE Programadores (
  id INTEGER PRIMARY KEY,
  nome TEXT(40),
  idade INT,
  email TEXT(40)
);


-- Deletar tabela
DROP TABLE Programadores;

SELECT * FROM Programadores;

SELECT COUNT(*) as quantidade_linhas
FROM Programadores;


-- Inserir e filtra dados
INSERT INTO Programadores (nome, idade, email)
VALUES ('Eliot', 25, 'robot@gmail.com');

SELECT * FROM Programadores
WHERE nome = 'Eliot';

UPDATE Programadores
SET nome = 'Mr. Robot', idade = 40
WHERE nome = 'Eliot'
AND idade = 25;

SELECT * FROM Programadores
WHERE email = 'robot@gmail.com'
AND idade = 40
AND nome = 'Mr. Robot';

-- Adicionar coluna nova
ALTER TABLE Programadores
ADD COLUMN linguagem TEXT(40);

SELECT * FROM Programadores;

-- Inserir novos valores
UPDATE Programadores
SET linguagem = 'Python'
WHERE nome = 'Mr. Robot';

INSERT INTO Programadores (nome, idade, email, linguagem)
VALUES ('Steve Jobs', 70, 'jobs@gmail.com', 'Lua');

INSERT INTO Programadores (nome, idade, email, linguagem)
VALUES ('Mark Z.', 150, 'meta@gmail.com', 'JavaScript');

INSERT INTO Programadores (nome, idade, email, linguagem)
VALUES ('Bill Gates', 100, 'office@gmail.com', 'C++');

-- Deletar linha 
DELETE FROM Programadores
WHERE id = 1;


-- |--##-- EX: --##--|
-- Seleciona o maior e menor valor
SELECT MAX(idade), MIN(idade) FROM Programadores

-- Selecionar a média da coluna idade
SELECT AVG(idade) FROM Programadores


-- Selecionar linhas onde o nome começam com B
SELECT * FROM Programadores
WHERE nome LIKE 'B%';
-- Selecionar linhas onde o nome termina com s
SELECT * FROM Programadores
WHERE nome LIKE '%s';
-- Selecionar linhas onde o nome tem 'll' 
SELECT * FROM Programadores
WHERE nome LIKE '%ll%';


-- ORDER BY and GROUP BY: 
-- by significa 'por', em português. Ou seja, ordene por coluna x, agrupe por coluna y

-- ORDER BY ordena nossos resultados se beaseando em uma coluna
-- ordenando por nome (ASC)
SELECT nome, email, idade, linguagem
FROM Programadores
ORDER BY nome ASC;

SELECT nome, email, idade, linguagem
FROM Programadores
ORDER BY nome DESC;

-- Ordenando por idade de forma decrescente com (DESC)
SELECT nome, email, idade, linguagem
FROM Programadores
ORDER BY idade DESC;

SELECT nome, email, idade, linguagem
FROM Programadores
ORDER BY idade ASC;

-- |--##-- EX: --##--|
-- Ordene a coluna email da tabela Programadores

SELECT email FROM Programadores
ORDER BY email ASC;


-- GROUP BY:
-- Neste exemplo, a consulta agrupa os usuários por idade
-- e conta quantos usuários existem em cada grupo.
SELECT *, COUNT(idade) AS quantidade_por_idade FROM Programadores
GROUP BY idade;

-- Mostrando a quantidade de de cada idade na coluna idade 
SELECT idade, COUNT(*) AS total_idade
FROM Programadores
GROUP BY idade;

-- Selecionar nome e idade e quantas vezes 
-- cada idade aparece na coluna idade
SELECT nome, idade, COUNT(*) AS total_idade
FROM Programadores
WHERE idade > 18
GROUP BY idade;



--  |--##-- EX: --##--|
-- Insirir um programador que tenha a idade menor ou igual a 18
-- Selecione o nome, a idade e o email de todas as pessoas na tabela com idade menor ou igual a 18
-- agrupando pela idade e mostrando a quantidade da idade como total_idade

INSERT INTO Programadores (nome, idade, email, linguagem)
VALUES ('Brock', 15, 'gmail@', 'Python');

SELECT nome, idade, COUNT(idade) AS total_idade
FROM Programadores
WHERE idade < 18
GROUP BY idade;



--  |--##-- EX: --##--|

-- Criar a coluna salario_dev na tabela Programadores e inserir salários diferentes
-- para todos as linhas. Em seguida, selecionar os dados ordenando por id e 
-- Mostrando a média da coluna salario_dev


-- Criar mais 5 colunas em uma das tabelas e inserir os dados manualmente com insert into


-- Selecionar a maior idade, e o menor id da tabela Programadores


-- Selecionar todas as colunas da tabela Programadores e ordenar pelo nome em ordem aufabética


-- Selecionar o nome e a idade da tabela Programadores, agrupando pela idade 
-- mostrando a mesma como total_idade_grup apenas onde a idade é maior ou igual a 18


-- Selecionar todas as colunas da tabela Programadores e ordenando por id em ordem decrescente


-- Criar uma tabela nova, inserir 20 linhas e 8 colunas na tabela
-- Refazer todos os exercícios desse arquivo com a tabela criada
