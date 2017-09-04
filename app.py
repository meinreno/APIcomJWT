#!/usr/bin/python
from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required
from werkzeug.security import safe_str_cmp
from models.model import Usuarios, Produtos
from flask_cors import CORS
import datetime

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = []
#funcao para alimentar os usuario
def login_usuario():
    ListarUsuario = Usuarios()
    lista_de_usuario = ListarUsuario.retornar_usuarios()
    for u in lista_de_usuario:
        
        users.append(User(str(u["_id"]), u["nome"], u["senha"]),)
login_usuario()


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}
#funcao requisitada pelo JWT
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
#funcao requisitada pelo JWT
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
#funcao evitar problemas com a seguranca do navegador pelo fato de enviar solicitacao para um dominio diferente
CORS(app)
#Retorna erros no terminal
app.debug = True
#Configuracao necessaria para rodar o JWT
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#Tempo para expirar o Token JWT
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60)
#Montado o sitema de Autenticacao para JWT
jwt = JWT(app, authenticate, identity)
#Funcao para listar todos os produtos 
@app.route('/listar_produtos', methods=["GET"])
#funcao que verifica o token passado por header
@jwt_required()
def produtos():
    #Conectar com o banco de dados e retorna um lista de produtos
    produtos_db = Produtos()
    lista_de_produto = []
    
    for i in produtos_db.retornar_produtos():
        
        lista_temp = {"Descricao": i["descricao"].encode("utf-8"), "Preco": i["preco"].encode("utf-8")}
        lista_de_produto.append(lista_temp)
    print lista_de_produto
    #envia os produtos por JSON
    return jsonify(lista_de_produto), {'Content-Type': 'application/json'}



#Funcao para executar a aplicacao
if __name__ == '__main__':
    app.run()