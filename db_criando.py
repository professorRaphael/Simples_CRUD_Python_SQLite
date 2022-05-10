import sqlite3

class Database:
    def __init__(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS escola(
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        nota FLOAT)''')
            self.conn.commit()
        except Exception as e:
            print("Erro na criação da tabela: ", e)

    def fetch(self):
        try:
            self.cursor.execute('SELECT id_aluno, nome, nota FROM escola')
            item = self.cursor.fetchall()
            for linha in item:
                print(linha)
        except sqlite3.Error as e:
            print("Erro ao buscar o aluno: ", e)

    def insert(self, nome, nota):
        try:
            cursor = self.conn.cursor()
            self.cursor.execute(
                'INSERT INTO escola (nome, nota) VALUES (?, ?)', (nome, nota))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Erro ao inserir o aluno: ", e)
        finally:
            if cursor:
                cursor.close()

    def remove(self, id_aluno):
        try:
            cursor = self.conn.cursor()
            self.cursor.execute(
                'DELETE FROM escola WHERE id_aluno = ?', (id_aluno, ))
            self.conn.commit()
            self.conn.execute('VACUUM')
        except sqlite3.Error as e:
            print('Erro ao excluir aluno: ', e)
        finally:
            if cursor:
                cursor.close()

    def update(self, id_aluno, nome, nota):
        try:
            cursor = self.conn.cursor()
            update_query = '''UPDATE escola set nome = ?, nota = ? WHERE id_aluno = ?'''
            dado = (nome, nota, id_aluno)
            self.cursor.execute(update_query, dado)
            self.conn.commit()
            print('Atualizado com sucesso.')
        except sqlite3.Error as e:
            print('Erro ao alterar aluno: ', e)
        finally:
            if cursor:
                cursor.close()

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':    
    #Banco de dados local db = Database("RAD_Python/Aula_03_05_AV1/Aula/escola.db")
    db = Database(':memory:')
    db.insert("Karl Franz", 8)
    db.insert("Ikkit Klaw", 7.5)
    db.insert("Balthasar Gelt", 9)
    db.insert("Mannfred von Carstein", 4)
    db.insert("Teclis", 10)
    db.insert("Tyrion", 9.5)
    db.insert("Gotrek Gurnisson", 0)
    db.insert("Felix Jaeger", 2)
    db.insert("Malekith ", 10)
    db.insert("Morathi ", 7)
    db.insert("Alarielle ", 8.5)
    db.insert("Hellebron ", 7.5)

    print('\nLista de alunos:')
    db.fetch()

    db.remove(1)

    print('\nLista de alunos apos remoção: ')
    db.fetch()
    print('\nFazendo alteração: ')
    db.update(2, "Karl Franz", 1)

    print('\nLista de alunos apos alteração:')
    db.fetch()