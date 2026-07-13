# 📝 Blog App — Flask + SQL

Aplicação web desenvolvida em Flask com persistência de dados via SQL, construída durante o curso Ocean Tech School.

## Sobre o projeto

Aplicação CRUD (criar, ler, atualizar, deletar posts) usando Flask como framework backend e um banco de dados relacional estruturado via schema SQL próprio.

## Tecnologias

- Python / Flask
- SQL (schema relacional)
- HTML/CSS (templates Jinja)

## Estrutura

```
ots_python_web/
├── app.py            # Rotas e lógica principal da aplicação
├── posts.py          # Lógica de manipulação de posts
├── esquema.sql        # Definição do banco de dados
├── requirements.txt   # Dependências do projeto
├── templates/          # Camada de apresentação (Jinja)
└── static/              # Arquivos estáticos (CSS, imagens)
```

## Como executar

```bash
# Clone o repositório
git clone https://github.com/caahpaiva/ots_python_web.git

# Acesse a pasta
cd ots_python_web

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
flask run
```

## Aprendizados

Prática de arquitetura MVC simples, modelagem de banco de dados relacional e integração entre backend Python e SQL.

## Autora

Feito por **Caah Paiva**

[LinkedIn](https://www.linkedin.com/in/caahpaiva) · [GitHub](https://github.com/caahpaiva)
