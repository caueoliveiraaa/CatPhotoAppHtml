-- Criar tabela Usuarios com mesmas colunas que Programadores
-- Inserir 10 linhas com dados válidos



-- Obter uma lista dos programadores juntamente com os usuários 
-- correspondentes com base em seus endereços de email.

SELECT Programadores.nome AS Programador, Programadores.email as Email_pro, usuarios.nome AS Usuario,
FROM Programadores INNER JOIN Usuarios
ON Programadores.email = Usuarios.email;

-- Neste exemplo acima, o Inner Join é utilizado para combinar as tabelas 
-- "Programadores" e "usuarios" com base no campo "email". 
-- A consulta retorna uma lista que mostra o nome do programador 
-- e o nome correspondente do usuário com o mesmo endereço de email
-- mostrando também os emails que são iguais

-- Realizando o mesmo com a idade
SELECT Programadores.nome AS Programador, usuarios.nome AS Usuario, Programadores.idade as idade
FROM Programadores INNER JOIN usuarios 
ON Programadores.idade = usuarios.idade;

-- Agora, vamos supor que você deseja obter uma lista de todos 
-- os programadores e, se houver, o nome do usuário correspondente
--  com base no endereço de email

SELECT Programadores.nome AS Programador, usuarios.nome AS Usuario
FROM Programadores LEFT JOIN usuarios
ON Programadores.email = usuarios.email;

-- Neste exemplo, o Left Join é utilizado para combinar as tabelas 
-- "Programadores" e "Usuários" com base no campo "email". 
-- A consulta retornará todos os programadores, independentemente de haver 
-- um correspondente na tabela "Usuarios". Se não houver um usuário correspondente,
-- o campo "Usuá=ario" será preenchido com NULL.


-- |--- EX 1 ---| 
-- Suponha que você queira obter uma lista dos programadores juntamente com os usuários 
-- correspondentes com base na idade. A consulta deve retornar apenas os programadores 
-- que possuem um usuário correspondente. Se o resultado final não trouxer 5 linhas ao menos,
-- insira mais dados manualmente via insert into para que o resultado retorne mais linhas.

SELECT Programadores.nome AS Programador, usuarios.nome AS Usuario
FROM Programadores INNER JOIN usuarios 
ON Programadores.idade = usuarios.idade;




-- |--- EX 2 ---|
-- Criar tabela Contatos com mesmas colunas que Usuarios + coluna telefone (e outras se desejado)
-- Insira 20 linhas na tabela Contatos e repita o exercícios anterior
-- trocando a tabela usuarios pela tabela contatos



-- |--- EX 3 ---|
-- Agora, suponha que você queira obter uma lista dos Usuarios juntamente 
-- com os contatos correspondentes com base no id.
-- Vamos inserir a coluna ativo em ambas as tabelas do tipo boolean (pesquisar como inserir boolean)
-- Metade das linhas das duas tabelas tem que estar com o ativo sendo true, e a outra metade false
-- A consulta deve retornar apenas os usuarios que possuem um id na tabela 
-- contatos correspondente ao id da tabela usuarios.
-- Após o ON, adicione um where no final para adicionar ao filtro também
-- apenas as idades que são maiores que 18 e menores que 30
-- No Final ordene por nome 

SELECT usuarios.nome AS Usuario,
usuarios.id AS id_correspondente
Programadores.nome AS Programador
FROM Programadores INNER JOIN usuarios
ON Programadores.id = usuarios.id;



-- |--- EX 4 --|
-- Repetir exercício 3 com a tabela contatos








