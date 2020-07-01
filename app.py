from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth
import json

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


# usuarios = {
#     'paulo': '123'
# }


# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return usuarios.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': f'{nome} não encontrada'
            }
        return response

    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        msg = f'{nome} deletado com sucesso'
        return {
            'status': 'sucesso',
            'mensagem': msg
        }


class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<nome>')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividade, '/atividades/')
if __name__ == '__main__':
    app.run(debug=True)
