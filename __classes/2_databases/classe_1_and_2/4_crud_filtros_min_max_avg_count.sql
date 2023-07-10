-- database: c:\Users\Leôncio Cauê\Desktop\apex_dir\__classes\2_databases\classe_1_and_2\mydatabase.db

-- Selecionando o maior valor na coluna idade:

SELECT * FROM usuarios
WHERE idade = (SELECT MAX(idade) FROM usuarios);

-- Selecionando o menor valor na coluna idade:

SELECT * FROM usuarios
WHERE idade = (SELECT MIN(idade) FROM usuarios);

-- Selecionando a média da coluna idade usando AVG:
-- AVG é para average, que significa média

SELECT AVG(idade) AS average_idade FROM usuarios;

-- Selecionando a quantidade de usuários adultos:

SELECT COUNT(*) AS usuarios_adultos
FROM usuarios WHERE idade > 18;

-- Selecionando a quantidade de usuários não adultos:

SELECT COUNT(*) AS usuarios_menores
FROM usuarios WHERE idade < 18;

-- Contar quantos usuários tem na tabela
SELECT COUNT(*) FROM usuarios;

-- Contar e-mails 
SELECT COUNT(email) FROM usuarios;

-- Calcular a média dos usuários que tem e-mail
SELECT AVG(idade) FROM usuarios 
WHERE email IS NOT NULL;

-- Encontrar todos os usuários onde o nome começa com 'A'
SELECT * FROM usuarios WHERE nome LIKE 'A%';

-- Encontrar todos os usuários onde o nome termina com 'son'
SELECT * FROM usuarios
WHERE nome LIKE '%son';

-- Encontrar todos os usuários que o e-mail possui a palavra 'gmail'
-- em qualquer parte do e-mail
SELECT * FROM usuarios WHERE email LIKE '%gmail%';

-- Encontrar todos os usuários que o nome começa com 'A' e termina com 'son'
SELECT * FROM usuarios WHERE nome LIKE 'A%son';


