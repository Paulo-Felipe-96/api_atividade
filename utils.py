from models import Pessoas, Usuarios


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


def insere_pessoas():
    pessoa = Pessoas(nome='Suzana', idade='29')
    print('Registro inserido com sucesso')
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome='Suzana').first()
    # print(f'{pessoa.nome}, {pessoa.idade}')


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Suzana').first()
    pessoa.delete()


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.idade = 10
    pessoa.save()


if __name__ == '__main__':
    # insere_usuario('paulo', '123')
    # insere_usuario('suzana', '321')
    # consulta_pessoas()
    # excluir_pessoa()
    # insere_pessoas()
    consulta_usuarios()
