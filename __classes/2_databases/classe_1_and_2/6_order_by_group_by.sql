-- database: c:\Users\Leôncio Cauê\Desktop\apex_dir\__classes\2_databases\classe_1_and_2\mydatabase.db

-- ORDER BY and GROUP BY: 
   -- by significa 'por', em português. Ou seja, ordene por coluna x, agrupe por coluna y

-- ORDER BY ordena nossos resultados se beaseando em um coluna
-- Ordenando por nome de forma crescente (ASC)
SELECT nome, email, idade
FROM usuarios
ORDER BY nome ASC;

-- Ordenando por idade de forma decrescente com (DESC)
SELECT nome, email, idade
FROM usuarios
ORDER BY idade DESC;

-- Neste exemplo, a consulta seleciona os campos nome, email e idade da tabela usuarios
-- e os ordena em ordem crescente primeiro pelo campo email e, em seguida, pelo campo nome
SELECT nome, email, idade
FROM usuarios
ORDER BY email ASC, nome ASC;

-- Neste exemplo, a consulta agrupa os usuários por idade e conta quantos usuários existem em cada grupo.
-- O resultado será uma lista das idades distintas presentes na tabela usuarios junto com a contagem total 
-- de usuários em cada idade.
SELECT idade, COUNT(*) AS total FROM usuarios
GROUP BY idade;

-- Contando o número de usuários para cada idade presente na tabela
SELECT idade, COUNT(*) FROM usuarios
GROUP BY idade;

-- Calcular a média da idade para cada grupo de idade
SELECT idade, AVG(idade) FROM usuarios
GROUP BY idade;
