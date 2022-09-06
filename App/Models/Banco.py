import sqlite3

class Banco():

  def __init__(self):
    self.conexao = sqlite3.connect("hotelaria.db")
    self.criar_tabelas()

  def criar_tabelas(self):
    curso = self.conexao.cursor()
    curso.execute('''
      CREATE TABLE IF NOT EXISTS hospede
      (
        idhospede INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome VARCHAR(100),
        rg VARCHAR(7),
        cpf VARCHAR(11),
        email VARCHAR(100),
        senha VARCHAR(100),
        telefone VARCHAR(45),
        data_nascimento DATE,
        sexo VARCHAR(45),
        foto_perfil VARCHAR(100),
        endereco VARCHAR(100),
        dados_bancarios VARCHAR(100),
        data_criacao DATETIME
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS funcionario
      (
        idfuncionario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome VARCHAR(100),
        rg VARCHAR(7),
        cpf VARCHAR(11),
        email VARCHAR(100),
        senha VARCHAR(100),
        telefone VARCHAR(45),
        data_nascimento DATE,
        sexo VARCHAR(45),
        foto_perfil VARCHAR(100),
        endereco VARCHAR(100),
        dados_bancarios VARCHAR(100),
        data_criacao DATETIME,
        matricula VARCHAR(100),
        cargo VARCHAR(100),
        nivel_acesso VARCHAR(45),
        data_admissao DATETIME
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS servico
      (
        idservico INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descricao VARCHAR(100),
        preco FLOAT,
        status VARCHAR(45)
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS produto
      (
        idproduto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descricao VARCHAR(100),
        preco FLOAT,
        estoque INTEGER
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS categoria
      (
        idcategoria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descricao VARCHAR(100),
        valor FLOAT,
        produtos VARCHAR(100)
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS acomodacao
      (
        idacomodacao INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descricao VARCHAR(100),
        andar VARCHAR(20),
        capacidade INTEGER,
        observacoes VARCHAR(255),
        status VARCHAR(50),
        fk_idcategoria INTEGER NOT NULL,
        CONSTRAINT fk_acomodacao_categoria1
          FOREIGN KEY(fk_idcategoria)
          REFERENCES categoria(idcategoria)
          ON DELETE CASCADE
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS reserva
      (
        idreserva INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        qtd_hospedes INTEGER,
        hospedes INTEGER,
        entrada_prevista DATETIME,
        saida_prevista DATETIME,
        data_criacao DATETIME,
        antecipacao FLOAT,
        status VARCHAR(100),
        valor FLOAT,
        servicos VARCHAR(100),
        produtos VARCHAR(100),
        fk_idhospede INTEGER NOT NULL,
        fk_idacomodacao INTEGER NOT NULL,
        CONSTRAINT fk_reserva_hospede1
          FOREIGN KEY(fk_idhospede)
          REFERENCES hospede(idhospede)
          ON DELETE CASCADE,
        CONSTRAINT fk_reserva_acomodacao1
          FOREIGN KEY(fk_idacomodacao)
          REFERENCES acomodacao(idacomodacao)
          ON DELETE CASCADE
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS checkin
      (
        idcheckin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        data_criacao DATETIME,
        fk_idfuncionario INTEGER NOT NULL,
        fk_idreserva INTEGER NOT NULL,
        CONSTRAINT fk_checkin_funcionario1
          FOREIGN KEY(fk_idfuncionario)
          REFERENCES funcionario(idfuncionario)
          ON DELETE CASCADE,
        CONSTRAINT fk_checkin_reserva1
          FOREIGN KEY(fk_idreserva)
          REFERENCES reserva(idreserva)
          ON DELETE CASCADE
      );
    ''')
    curso.execute('''
      CREATE TABLE IF NOT EXISTS checkout
      (
        idcheckout INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        valor_consumo FLOAT,
        valor_pago FLOAT,
        nota_fiscal VARCHAR(100),
        data_criacao DATETIME,
        fk_idfuncionario INTEGER NOT NULL,
        fk_idreserva INTEGER NOT NULL,
        CONSTRAINT fk_checkout_funcionario1
          FOREIGN KEY(fk_idfuncionario)
          REFERENCES funcionario(idfuncionario)
          ON DELETE CASCADE,
        CONSTRAINT fk_checkout_reserva1
          FOREIGN KEY(fk_idreserva)
          REFERENCES reserva(idreserva)
          ON DELETE CASCADE
      );
    ''')
    self.conexao.commit()
    curso.close()
  