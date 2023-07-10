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

SELECT COUNT(*) AS usuarios_adultos
FROM usuarios WHERE idade < 18;