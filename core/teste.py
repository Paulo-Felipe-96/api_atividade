from core import models


def insert_p():
    programador = models.Programadores(nome='Suzana Gonçalves Martins', idade='29',
                                       email='suzana.g.martins@hotmail.com')
    print('Registro inserido')
    programador.save()


def consulta_p():
    # programador = models.Programadores.query.all()
    # print(programador)
    programador = models.Programadores.query.filter_by(nome='Paulo').first()
    print(f'{programador.nome}, {programador.email}, idade {programador.idade}')


def insert_h():
    habilidade = models.Habilidades(nome='Flutter')
    print('Registro inserido')
    habilidade.save()


def consulta_h():
    habilidade = models.Habilidades.query.all()
    print(habilidade)


def insert_ph():
    proghab = models.ProgramadorHabilidades(programador_id=1, habilidade_id=2)
    print('Registrado')
    proghab.save()


def consulta_ph():
    proghab = models.ProgramadorHabilidades.query.all()
    print(proghab)


if __name__ == '__main__':
    insert_ph()
    consulta_ph()
