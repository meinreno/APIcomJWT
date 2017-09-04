# API com Autenticação JWT

Funções:
- Login com verificação de usuario em BD e retorno de Token em JWT
- Retorna em JSON lista de produtos

# Solicitações na API
Login:
- Recebe um JSON{"username":"exemplo", "password":"exemplo"} verifica em Banco de dados.
- Se o Usuario autenticar, retorna um Token em JWT, com Tempo de Vida de 1 minuto

Produtos:
- Recebe um solicitação GET junto com o Token no Header, a API compara o token recebido, com o que consta no BD e retorna os produtos. Em caso negativo, retorna erro.

# Aplicações e Bibliotecas que devem ser instaladas:
- mongodb - Bando de Dados baseado em Bibliotecas
''' apt-get install -y mongodb-org '''

- Flask - MicroFramework baseado em Python
''' pip install Flask '''

- flask_jwt - Utilizado para criar o Token JWT
''' pip install flask-jwt '''

- flask_cors - Utilizado para comunicação com o navegador, evitando o bloqueio de segurança dos navegadores quando realizado a requisição de um navegador fora do dominio.
''' pip install flask-cors '''

- pymongo - Ferramenta para comunicar com o MongoDB
''' pip install pymongo '''

# Instalação: 
- Apos as instalações das bibliotecas Auxiliares e da Principal(Flask), copiar todos os aquivos em uma pasta.
- Dentro da raiz do projeto, executar o script models/model.py, para criar o banco de dados padrão em MongoDB.
''' python models/model.py '''

- para executar o projeto:
''' python app.py '''



# Versoes de Aplicações Utilizadas:
- Python = 2.7.13
- pymongo = 3.4.0
- Flask = 0.12.2
- Flask-Cors = 3.0.3
- Flask-JWT = 0.3.2
- MongoDB = 3.2.11
- Debian = 9 (stretch)
    
