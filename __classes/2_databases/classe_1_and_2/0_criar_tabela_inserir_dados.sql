-- database: c:\Users\Leôncio Cauê\Desktop\apex_dir\__classes\2_databases\classe_1_and_2\mydatabase.db

-- 1 - Criando tabelas:

-- PRIMARY KEY:
-- Auto incrementa o valor que está no campo
-- Força o campo a não ter um valor null
-- Garante que cada usuário terá um valor único

-- IF NOT EXISTS: 
-- Garante que a tabela apenas será criada
-- caso uma tabela com o nome usuarios não exista

CREATE TABLE IF NOT EXISTS usuarioss (
    -- Campo do tipo int com chave primária
    id INTEGER PRIMARY KEY,
    -- Text é usando para campos str
    nome TEXT
    -- Text é usando para campos do tipo int
    idade INTEGER,
    -- A última coluna da tabela não precisa de vírgula 
    email TEXT
);



-- 2 - Inserindo dados em tabelas:

-- INSERT INTO é o comando SQL para inserir dados em uma tabela
INSERT INTO usuarioss (name, age, email)
-- Ele é seguido pelo VALUE que armazena os valores a serem armazenados
VALUES ('John Doe', 30, 'john@example.com');



-- 3 - Alterando tabelas:

-- ALTER TABLE altera uma tabela
ALTER TABLE usuarioss
-- RENAME TO renomeia a tabela
RENAME TO usuarios;



-- 4 - Resetando tabelas:

-- DELETE FROM deleta todos os rows (linhas) da tabela
DELETE FROM usuarios;
-- VACUUM vai resetar a contabilização do PRIMARY KEY
-- Ele deve ser colocado logo após o comando acima
VACUUM;

-- 5 - Deletando tabelas:

-- DROP TABLE deleta uma tabela permanentemente
DROP TABLE usuarios;