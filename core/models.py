from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///base.db', convert_unicode=True)
db_sesson = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_sesson.query_property()


class Programadores(Base):
    __tablename__ = 'programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(40))

    def __repr__(self):
        return f'Programador {self.nome}'

    def save(self):
        db_sesson.add(self)
        db_sesson.commit()

    def delete(self):
        db_sesson.delete(self)
        db_sesson.commit()


class Habilidades(Base):
    __tablename__ = 'habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True)

    def __repr__(self):
        return f'ID {self.id} - Habilidade {self.nome}'

    def save(self):
        db_sesson.add(self)
        db_sesson.commit()

    def delete(self):
        db_sesson.delete(self)
        db_sesson.commit()


class ProgramadorHabilidades(Base):
    __tablename__ = 'programadorhabilidades'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programadores.id'))
    habilidade_id = Column(Integer, ForeignKey('habilidades.id'))
    programador = relationship('Programadores')
    habilidade = relationship('Habilidades')

    def __repr__(self):
        return f'Programador {self.programador.nome}, Habilidade {self.habilidade.nome}'

    def save(self):
        db_sesson.add(self)
        db_sesson.commit()

    def delete(self):
        db_sesson.delete(self)
        db_sesson.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20), unique=True)

    def __repr__(self):
        return f'login: {self.login}' \
               f'senha: {self.senha}'

    def save(self):
        db_sesson.add(self)
        db_sesson.commit()

    def delete(self):
        db_sesson.delete(self)
        db_sesson.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
