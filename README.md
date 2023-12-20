# Kenzie-Buster

Nesse projeto eu criei uma aplicação para gerenciar usuários, filmes e compras, incluindo autenticação e permissões de rotas para diferentes tipos de usuário.

# Rotas 

## Criação de Usuário
- **Endpoint:** `/api/users/`
- **Verbo HTTP:** `POST`
- **Objetivo:** Criação de um novo usuário na base de dados.

## Autenticação de Usuário
- **Endpoint:** `/api/users/login/`
- **Verbo HTTP:** `POST`
- **Objetivo:** Autenticação do usuário.

## Busca de Usuário por ID
- **Endpoint:** `/api/users/<int:user_id>/`
- **Verbo HTTP:** `GET`
- **Objetivo:** Busca de informações sobre um usuário específico.
- **Parâmetro na Rota:** `<int:user_id>`

## Atualização de Usuário por ID
- **Endpoint:** `/api/users/<int:user_id>/`
- **Verbo HTTP:** `PATCH`
- **Objetivo:** Atualização de informações de um usuário específico.
- **Parâmetro na Rota:** `<int:user_id>`

# Rotas API para Filmes

A seguir estão as rotas disponíveis para interação com a API de filmes. Utilize essas rotas para realizar operações diversas, como criação, listagem, busca, atualização e deleção de informações sobre filmes.

## Criação de Filme
- **Endpoint:** `/api/movies/`
- **Verbo HTTP:** `POST`
- **Objetivo:** Criação de um novo filme na base de dados.

## Listagem de Filmes
- **Endpoint:** `/api/movies/`
- **Verbo HTTP:** `GET`
- **Objetivo:** Listagem de todos os filmes disponíveis.

## Busca de Filme por ID
- **Endpoint:** `/api/movies/<int:movie_id>/`
- **Verbo HTTP:** `GET`
- **Objetivo:** Busca de informações detalhadas sobre um filme específico.
- **Parâmetro na Rota:** `<int:movie_id>`

## Deleção de Filme por ID
- **Endpoint:** `/api/movies/<int:movie_id>/`
- **Verbo HTTP:** `DELETE`
- **Objetivo:** Deleção de um filme específico.
- **Parâmetro na Rota:** `<int:movie_id>`

## Criação de Pedido para Filme
- **Endpoint:** `/api/movies/<int:movie_id>/orders/`
- **Verbo HTTP:** `POST`
- **Objetivo:** Criação de um pedido relacionado a um filme específico.
- **Parâmetro na Rota:** `<int:movie_id>`

**Observação:** Substitua `<int:user_id>` e `<int:movie_id>` pelos identificadores únicos do usuário e do filme desejados.

# Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```

## Execução dos testes:


- Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/tarefas/t2/users/t2_user_views_test.py::UserLoginViewsT2Test::test_user_login_without_required_fields
```
--- 

Para executar todos os testes:
```shell
pytest --testdox -vvs
```
