from models import Pessoas


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
    # consulta_pessoas()
    # excluir_pessoa()
    # insere_pessoas()
    # consulta_pessoas()
    pass
