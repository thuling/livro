import sqlite3

# Conectar ao banco de dados
def connect():
  conn = sqlite3.connect("dados.db")
  return conn

# funcao para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
  conn = connect()
  conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) \
              VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
  conn.commit()
  conn.close()

# Funcao para inserir usuarios
def insert_user(nome, sobrenome, endereco, email, telefone):
  conn = connect()
  conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES(?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
  conn.commit()
  conn.close()


# Funcao para exibir os livros
def exibir_livros():
  conn = connect()
  livros = conn.execute("SELECT * FROM livros").fetchall()
  conn.close()

  if not livros:
    print("Nenhum livro encontrado na biblioteca.")
    return
  
  print("Livros na biblioteca: ")
  for livro in livros:
    print(f"ID: {livro[0]}")
    print(f"Titulo: {livro[1]}")
    print(f"Autor: {livro[2]}")
    print(f"Editora: {livro[3]}")
    print(f"Ano de publicação: {livro[4]}")
    print(f"ISBN: {livro[5]}")
    print ("\n")

# Funcao para realizar imprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
  conn = connect()
  conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)VALUES(?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
  conn.commit()
  conn.close()

# Funcao para exibir todos os livros emprestados
def get_books_on_loan():
  conn = connect()
  result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.id, emprestimos.data_emprestimo, emprestimos.data_devolucao FROM livros \
                        INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                        INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                        WHERE emprestimos.data_devolucao IS NULL").fetchall()
  conn.close()
  return result

# Funcao para atualizar a data de devolucao do emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
  conn = connect()
  conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
  conn.commit()
  conn.close()

# insert_book("Dom quixote", "Miguel", "Edito1", 1607, "123456")
# insert_user("Joao", "Silva", "Rua dos cao", "joaocao@gmail.com", "+55 1235667")
# insert_loan(1, 1, "2022-01-01", None)
livros_emprestados = get_books_on_loan()

print(livros_emprestados)

update_loan_return_date(2, "16-05-2024")
# exibir_livros()