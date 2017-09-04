from pymongo import MongoClient
#conexao com o BD mongo
cliente = MongoClient('localhost:27017')
#conexao com o BD da aplicacao, caso nao exista o mongo cria automaticamente
db = cliente.TesteSPA
#classe para manipulacao com o a collection de usuario
class Usuarios():
    def retornar_usuarios(self):
        try:
            
            return db.usuario.find({})
           

        except Exception as e:
            raise e
#classe para manipulacao com o a collection de produtos
class Produtos():
    def retornar_produtos(self):
        return db.produto.find({})
#classe para criar o BD e Collections, alem de dar a carga para testar a API
#so executa quando o scrip e rodado diretamente
class Criar_BD_Padrao():
    dados = {
                "produto":[{"descricao": "Nescau", "preco": "5,79"},
                {"descricao": "Leite de Coco", "preco": "2,59"},
                {"descricao": "Maionese Hellmans", "preco": "6,89"}, 
                {"descricao": "Detergente em Po Omo", "preco": "2,79"}],
                "usuario":[{"nome": "admin", "senha": "admin"}]
            }            

            

    def cadastrar_usuario(self):
        
        for i in self.dados:
            
            for a in self.dados[i]:
                if i == 'produto':
                    db.produto.insert(a)
                else:
                    db.usuario.insert(a)    

    
#caso a aplicacao seja executada, criar o BD e as Collections
if __name__=='__main__':
    try:
        carga_db = Criar_BD_Padrao()
        carga_db.cadastrar_usuario()
    except Exception as e:
        raise e
    
    
