import mysql.connector
from tkinter import messagebox
import customtkinter


class Database:
    def __init__(self):
        self.conex_db = self.conection_db()
        if self.conex_db:
            self.cursor_db = self.conex_db.cursor()
            self.create_tables()

    def conection_db(self):
        """Estabelece conexão com o banco de dados"""
        try:
            conex = mysql.connector.connect(
                user='root',
                host='localhost',
                password='ceub123456',
                database='db_Wixus'
            )
            print("Conexão concluída")
            return conex
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de conexão", f"Erro ao conectar ao MySQL: {err}")
            return None

    def create_tables(self):
        """Cria todas as tabelas necessárias"""
        self.create_db()
        self.create_tb_jogos()
        self.create_tb_user()
        self.create_tb_cart()
        self.create_tb_carrinho_itens()

    def create_db(self):
        """Cria o banco de dados se não existir"""
        try:
            self.cursor_db.execute('''CREATE DATABASE IF NOT EXISTS db_Wixus''')
            self.cursor_db.execute('''USE db_Wixus''')
            print("Database criada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar database: {err}")

    # ------------------------------------------- JOGOS --------------------------------------------------------
    def create_tb_jogos(self):
        """Cria tabela de jogos"""
        try:
            create = '''CREATE TABLE IF NOT EXISTS tb_jogos(
                    id_jogo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    price DECIMAL(9,2),
                    faixa_etaria INT,
                    developer VARCHAR(30) NOT NULL,
                    data_lanc DATE,
                    plataformas VARCHAR(30),
                    genre VARCHAR(50)
                    )'''
            self.cursor_db.execute(create)
            print("Tabela Jogos criada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar tabela de jogos: {err}")

    def insert_jogo(self, dados_jogo):
        """Insere um novo jogo na tabela"""
        try:
            sql = '''INSERT INTO tb_jogos (name, price, faixa_etaria, developer, data_lanc, plataformas, genre)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            self.cursor_db.execute(sql, dados_jogo)
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Jogo inserido com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao inserir jogo: {err}")
            return False

    def buscar_jogo_por_id(self, id_jogo):
        """Busca jogo por ID"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE id_jogo = %s'''
            self.cursor_db.execute(sql, (id_jogo,))
            return self.cursor_db.fetchone()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogo: {err}")
            return None

    def buscar_jogos_por_nome(self, nome):
        """Busca jogos por nome (LIKE)"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE name LIKE %s'''
            self.cursor_db.execute(sql, (f"%{nome}%",))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogos: {err}")
            return []

    def buscar_jogos_por_genero(self, genero):
        """Busca jogos por gênero"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE genre LIKE %s'''
            self.cursor_db.execute(sql, (f"%{genero}%",))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogos por gênero: {err}")
            return []

    def buscar_jogos_por_preco(self, preco_max):
        """Busca jogos com preço menor ou igual ao especificado"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE price <= %s'''
            self.cursor_db.execute(sql, (preco_max,))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogos por preço: {err}")
            return []

    def buscar_jogos_por_produtor(self, produtor):
        """Busca jogos por produtor"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE developer LIKE %s'''
            self.cursor_db.execute(sql, (f"%{produtor}%",))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogos por produtor: {err}")
            return []

    def buscar_jogos_por_idade(self, idade_max):
        """Busca jogos com faixa etária menor ou igual à especificada"""
        try:
            sql = '''SELECT * FROM tb_jogos WHERE faixa_etaria <= %s'''
            self.cursor_db.execute(sql, (idade_max,))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar jogos por idade: {err}")
            return []

    def atualizar_jogo(self, id_jogo, campo, novo_valor):
        """Atualiza um campo específico de um jogo"""
        try:
            sql = f'''UPDATE tb_jogos SET {campo} = %s WHERE id_jogo = %s'''
            self.cursor_db.execute(sql, (novo_valor, id_jogo))
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Jogo atualizado com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao atualizar jogo: {err}")
            return False

    def deletar_jogo(self, id_jogo):
        """Remove um jogo do banco de dados"""
        try:
            sql = '''DELETE FROM tb_jogos WHERE id_jogo = %s'''
            self.cursor_db.execute(sql, (id_jogo,))
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Jogo removido com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao remover jogo: {err}")
            return False

    # ------------------------------------------- USUÁRIOS --------------------------------------------------------
    def create_tb_user(self):
        """Cria tabela de usuários"""
        try:
            create = '''CREATE TABLE IF NOT EXISTS tb_user(
                    id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    idade INT NOT NULL,
                    pais VARCHAR(50),
                    status VARCHAR(50),
                    developer BOOL DEFAULT FALSE
                    )'''
            self.cursor_db.execute(create)
            print("Tabela User criada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar tabela de usuários: {err}")

    def insert_usuario(self, dados_usuario):
        """Insere um novo usuário na tabela"""
        try:
            sql = '''INSERT INTO tb_user (nome, idade, pais, status, developer)
                     VALUES (%s, %s, %s, %s, %s)'''
            self.cursor_db.execute(sql, dados_usuario)
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao inserir usuário: {err}")
            return False

    def buscar_usuario_por_id(self, id_user):
        """Busca usuário por ID"""
        try:
            sql = '''SELECT * FROM tb_user WHERE id_user = %s'''
            self.cursor_db.execute(sql, (id_user,))
            return self.cursor_db.fetchone()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar usuário: {err}")
            return None

    def buscar_usuarios_por_nome(self, nome):
        """Busca usuários por nome"""
        try:
            sql = '''SELECT * FROM tb_user WHERE nome LIKE %s'''
            self.cursor_db.execute(sql, (f"%{nome}%",))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar usuários: {err}")
            return []

    def atualizar_usuario(self, id_user, campo, novo_valor):
        """Atualiza um campo específico de um usuário"""
        try:
            sql = f'''UPDATE tb_user SET {campo} = %s WHERE id_user = %s'''
            self.cursor_db.execute(sql, (novo_valor, id_user))
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao atualizar usuário: {err}")
            return False

    def deletar_usuario(self, id_user):
        """Remove um usuário do banco de dados"""
        try:
            sql = '''DELETE FROM tb_user WHERE id_user = %s'''
            self.cursor_db.execute(sql, (id_user,))
            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao remover usuário: {err}")
            return False

    # ------------------------------------------- CARRINHO --------------------------------------------------------
    def create_tb_cart(self):
        """Cria tabela de carrinhos"""
        try:
            create = '''CREATE TABLE IF NOT EXISTS tb_cart(
                    id_cart INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_user INT NOT NULL,
                    preco_total DECIMAL(9,2) DEFAULT 0,
                    forma_pagamento VARCHAR(30),
                    FOREIGN KEY (id_user) REFERENCES tb_user(id_user)
                    )'''
            self.cursor_db.execute(create)
            print("Tabela Cart criada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar tabela de carrinho: {err}")

    def create_tb_carrinho_itens(self):
        """Cria tabela de itens do carrinho"""
        try:
            create = '''CREATE TABLE IF NOT EXISTS tb_carrinho_itens(
                    id_item INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_cart INT NOT NULL,
                    id_jogo INT NOT NULL,
                    quantidade INT NOT NULL,
                    preco_unitario DECIMAL(9,2) NOT NULL,
                    FOREIGN KEY (id_cart) REFERENCES tb_cart(id_cart),
                    FOREIGN KEY (id_jogo) REFERENCES tb_jogos(id_jogo)
                    )'''
            self.cursor_db.execute(create)
            print("Tabela Itens do Carrinho criada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar tabela de itens do carrinho: {err}")

    def criar_carrinho(self, id_user):
        """Cria um novo carrinho para um usuário"""
        try:
            sql = '''INSERT INTO tb_cart (id_user) VALUES (%s)'''
            self.cursor_db.execute(sql, (id_user,))
            self.conex_db.commit()
            return self.cursor_db.lastrowid
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar carrinho: {err}")
            return None

    def adicionar_ao_carrinho(self, id_cart, id_jogo, quantidade):
        """Adiciona um item ao carrinho"""
        try:
            # Primeiro obtém o preço do jogo
            sql_preco = '''SELECT price FROM tb_jogos WHERE id_jogo = %s'''
            self.cursor_db.execute(sql_preco, (id_jogo,))
            preco = self.cursor_db.fetchone()[0]

            # Verifica se o item já está no carrinho
            sql_check = '''SELECT id_item, quantidade FROM tb_carrinho_itens 
                           WHERE id_cart = %s AND id_jogo = %s'''
            self.cursor_db.execute(sql_check, (id_cart, id_jogo))
            item = self.cursor_db.fetchone()

            if item:
                # Atualiza a quantidade se o item já existir
                nova_quantidade = item[1] + quantidade
                sql_update = '''UPDATE tb_carrinho_itens SET quantidade = %s 
                               WHERE id_item = %s'''
                self.cursor_db.execute(sql_update, (nova_quantidade, item[0]))
            else:
                # Adiciona novo item ao carrinho
                sql_insert = '''INSERT INTO tb_carrinho_itens 
                                (id_cart, id_jogo, quantidade, preco_unitario) 
                                VALUES (%s, %s, %s, %s)'''
                self.cursor_db.execute(sql_insert, (id_cart, id_jogo, quantidade, preco))

            # Atualiza o preço total do carrinho
            self.atualizar_total_carrinho(id_cart)

            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Item adicionado ao carrinho!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao adicionar ao carrinho: {err}")
            return False

    def remover_do_carrinho(self, id_cart, id_jogo, quantidade):
        """Remove um item do carrinho"""
        try:
            # Verifica se o item está no carrinho
            sql_check = '''SELECT id_item, quantidade FROM tb_carrinho_itens 
                          WHERE id_cart = %s AND id_jogo = %s'''
            self.cursor_db.execute(sql_check, (id_cart, id_jogo))
            item = self.cursor_db.fetchone()

            if item:
                if item[1] > quantidade:
                    # Reduz a quantidade se ainda houver itens
                    nova_quantidade = item[1] - quantidade
                    sql_update = '''UPDATE tb_carrinho_itens SET quantidade = %s 
                                   WHERE id_item = %s'''
                    self.cursor_db.execute(sql_update, (nova_quantidade, item[0]))
                else:
                    # Remove o item completamente se a quantidade for igual ou maior
                    sql_delete = '''DELETE FROM tb_carrinho_itens WHERE id_item = %s'''
                    self.cursor_db.execute(sql_delete, (item[0],))

                # Atualiza o preço total do carrinho
                self.atualizar_total_carrinho(id_cart)

                self.conex_db.commit()
                messagebox.showinfo("Sucesso", "Item removido do carrinho!")
                return True
            else:
                messagebox.showwarning("Aviso", "Item não encontrado no carrinho!")
                return False
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao remover do carrinho: {err}")
            return False

    def atualizar_total_carrinho(self, id_cart):
        """Atualiza o preço total do carrinho"""
        try:
            sql = '''UPDATE tb_cart c
                     SET preco_total = (
                         SELECT COALESCE(SUM(ci.quantidade * ci.preco_unitario), 0)
                         FROM tb_carrinho_itens ci
                         WHERE ci.id_cart = c.id_cart
                     )
                     WHERE c.id_cart = %s'''
            self.cursor_db.execute(sql, (id_cart,))
            self.conex_db.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao atualizar total do carrinho: {err}")

    def ver_carrinho(self, id_cart):
        """Retorna todos os itens de um carrinho"""
        try:
            sql = '''SELECT j.id_jogo, j.name, ci.quantidade, ci.preco_unitario, 
                            (ci.quantidade * ci.preco_unitario) as total_item
                     FROM tb_carrinho_itens ci
                     JOIN tb_jogos j ON ci.id_jogo = j.id_jogo
                     WHERE ci.id_cart = %s'''
            self.cursor_db.execute(sql, (id_cart,))
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao ver carrinho: {err}")
            return []

    def finalizar_compra(self, id_cart, forma_pagamento):
        """Finaliza a compra e limpa o carrinho"""
        try:
            # Atualiza a forma de pagamento
            sql_update = '''UPDATE tb_cart 
                           SET forma_pagamento = %s 
                           WHERE id_cart = %s'''
            self.cursor_db.execute(sql_update, (forma_pagamento, id_cart))

            # Limpa o carrinho
            sql_clear = '''DELETE FROM tb_carrinho_itens WHERE id_cart = %s'''
            self.cursor_db.execute(sql_clear, (id_cart,))

            self.conex_db.commit()
            messagebox.showinfo("Sucesso", "Compra finalizada com sucesso!")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao finalizar compra: {err}")
            return False

    # ------------------------------------------- GERAL --------------------------------------------------------
    def listar_todos_jogos(self):
        """Retorna todos os jogos cadastrados"""
        try:
            sql = '''SELECT * FROM tb_jogos'''
            self.cursor_db.execute(sql)
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao listar jogos: {err}")
            return []

    def listar_todos_usuarios(self):
        """Retorna todos os usuários cadastrados"""
        try:
            sql = '''SELECT * FROM tb_user'''
            self.cursor_db.execute(sql)
            return self.cursor_db.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao listar usuários: {err}")
            return []

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados"""
        try:
            if hasattr(self, 'cursor_db') and self.cursor_db:
                self.cursor_db.close()
            if hasattr(self, 'conex_db') and self.conex_db and self.conex_db.is_connected():
                self.conex_db.close()
                print("Conexão encerrada")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao fechar conexão: {err}")


if __name__ == '__main__':
    # Testes básicos
    db = Database()
    try:
        # Teste de inserção de jogo
        dados_jogo = ("The Witcher 3", 99.90, 18, "CD Projekt Red", "2015-05-19", "PC,PS4,XBOX", "RPG")
        db.insert_jogo(dados_jogo)

        # Teste de busca
        resultado = db.buscar_jogo_por_id(1)
        print(resultado)

    finally:
        db.fechar_conexao()
