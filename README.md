## Simples exemplo de Python com banco de Dados SQLite.
# Gerenciador de Alunos usando SQLite em Python

Este é um simples gerenciador de alunos implementado em Python utilizando SQLite para armazenar os dados. O programa permite realizar operações básicas como inserir, remover, atualizar e visualizar informações dos alunos.

## Funcionalidades

- **Inserir Aluno:** Adiciona um novo aluno ao banco de dados.
- **Remover Aluno:** Remove um aluno existente do banco de dados.
- **Atualizar Aluno:** Atualiza as informações de um aluno existente no banco de dados.
- **Listar Alunos:** Exibe a lista de todos os alunos cadastrados no banco de dados.

## Requisitos

- Python 3.x
- SQLite3

## Utilização

1. Clone o repositório ou copie o código para o seu ambiente de trabalho.
2. Execute o código Python.

```bash
python nome_do_arquivo.py
```

## Exemplo de Uso
```python
from database import Database

# Conecta ao banco de dados
db = Database('escola.db')

# Insere novos alunos
db.insert("Karl Franz", 8)
db.insert("Ikkit Klaw", 7.5)

# Lista todos os alunos
print('\nLista de alunos:')
db.fetch()

# Remove um aluno pelo ID
db.remove(1)

# Lista os alunos após remoção
print('\nLista de alunos após remoção:')
db.fetch()

# Atualiza informações de um aluno
print('\nFazendo alteração:')
db.update(2, "Karl Franz", 1)

# Lista os alunos após atualização
print('\nLista de alunos após alteração:')
db.fetch()
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request para sugerir melhorias ou correções.
