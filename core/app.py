from flask import Flask, request
from flask_restful import Resource, Api
from core.models import Programadores, Habilidades, ProgramadorHabilidades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Ola(Resource):
    def get(self):
        return {'status': 'sucesso',
                'mensagem': 'servidor online'}


class NovoUsuario(Resource):
    @auth.login_required
    def get(self):
        usuarios = Usuarios.query.all()
        res = [{'id': i.id, 'login': i.login, 'senha': i.senha} for i in usuarios]
        return res

    @auth.login_required
    def post(self):
        dados = request.json
        usuario = Usuarios(login=dados['login'], senha=dados['senha'])
        usuario.save()
        return {
            'login': usuario.login,
            'senha': usuario.senha
        }


# retorna lista de devs e cadastra um novo dev
class Devs(Resource):
    def get(self):
        progs = Programadores.query.all()
        res = [{'id': i.id, 'nome': i.nome, 'idade': i.idade, 'email': i.email} for i in progs]
        return res

    def post(self):
        dados = request.json
        devs = Programadores(nome=dados['nome'], idade=dados['idade'], email=dados['email'])
        devs.save()
        res = {
            'nome': devs.nome,
            'idade': devs.idade,
            'email': devs.email
        }
        return res


class Dev(Resource):
    def get(self, id):
        dev = Programadores.query.filter_by(id=id).first()
        return {
            'id': dev.id,
            'nome': dev.nome,
            'idade': dev.idade,
            'email': dev.email
        }

    def put(self, id):
        dados = request.json
        dev = Programadores.query.filter_by(id=id).first()
        if 'nome' in dados:
            dev.nome = dados['nome']
        if 'idade' in dados:
            dev.idade = dados['idade']
        if 'email' in dados:
            dev.email = dados['email']
        dev.save()
        res = {
            'id': dev.id,
            'nome': dev.nome,
            'idade': dev.idade,
            'email': dev.email
        }
        return res

    def delete(self, id):
        dev = Programadores.query.filter_by(id=id).first()
        dev.delete()
        msg = f'{id} deletado com sucesso'
        res = {
            'status': 'sucesso',
            'mensagem': msg
        }
        return res


# retorna lista de skills e cadastra nova skill
class Skills(Resource):
    def get(self):
        skills = Habilidades.query.all()
        res = [{'id': i.id, 'nome': i.nome} for i in skills]
        return res

    def post(self):
        dados = request.json
        skills = Habilidades(nome=dados['nome'])
        skills.save()
        res = {'nome': skills.nome}
        return res


class Skill(Resource):
    def get(self, id):
        skill = Habilidades.query.filter_by(id=id).first()
        res = {
            'id': skill.id,
            'nome': skill.nome
        }
        return res

    def put(self, id):
        dados = request.json
        skill = Habilidades.query.filter_by(id=id).first()
        if 'nome' in dados:
            skill.nome = dados['nome']
        skill.save()
        res = {
            'nome': skill.nome
        }
        return res

    def delete(self, id):
        skill = Habilidades.query.filter_by(id=id).first()
        skill.delete()
        msg = f'{id} deletado com sucesso'
        res = {
            'status': 'sucesso',
            'mensagem': msg
        }
        return res


# retorna skills x devs
class SkillsnDevs(Resource):
    def get(self):
        skdv = ProgramadorHabilidades.query.all()
        res = [{'id': i.id, 'programador': i.programador.nome, 'habilidade': i.habilidade.nome} for i in skdv]
        return res

    def post(self):
        dados = request.json
        devhab = ProgramadorHabilidades(programador_id=dados['programador_id'], habilidade_id=dados['habilidade_id'])
        devhab.save()
        res = {
            'programador_id': devhab.programador_id,
            'habilidade_id': devhab.habilidade_id
        }
        return res


api.add_resource(Ola, '/status/')
api.add_resource(Dev, '/dev/<int:id>/')
api.add_resource(Devs, '/devs/')
api.add_resource(Skill, '/skill/<int:id>/')
api.add_resource(Skills, '/skills/')
api.add_resource(SkillsnDevs, '/todos/')  # skill e pessoas
api.add_resource(NovoUsuario, '/users/')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.128')
