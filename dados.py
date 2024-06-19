import sqlite3

# Conectar ao banco de dados
con = sqlite3.connect("dados.db")

# Criar uma tabela de livros
con.execute('CREATE TABLE livros(\
            id INTEGER PRIMARY KEY,\
            titulo TEXT,\
            autor TEX,\
            editora TEXT,\
            ano_publicacao INT,\
            isbn TEXT)')

# criando tabela de Usuarios
con.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXT,\
            sobrenome TEX,\
            endereco TEXT,\
            email TEXT,\
            telefone TEXT)')

# Criando tabela de emprestimo
con.execute('CREATE TABLE emprestimos(\
            id INTEGER PRIMARY KEY,\
            id_livro INTEGER, \
            id_usuario INTEGER, \
            data_emprestimo TEXT,\
            data_deevolucao TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))') 