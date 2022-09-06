from .Model import *

class Hospede(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into hospede (nome, rg, cpf, 
                          email, senha, telefone, 
                          data_nascimento, sexo, foto_perfil, 
                          endereco, dados_bancarios, data_criacao) 
      values (?,?,?,?,?,?,?,?,?,?,?,?)''', 
    (self.nome, self.rg, self.cpf,
    self.email, self.senha, self.telefone,
    self.data_nascimento, self.sexo, self.foto_perfil,
    self.endereco, self.dados_bancarios, self.data_criacao) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update hospede 
      set 
        nome = ?, rg = ?, cpf = ?, 
        email = ?, senha = ?, telefone = ?, 
        data_nascimento = ?, sexo = ?, foto_perfil = ?, 
        endereco = ?, dados_bancarios = ? where idhospede = ? ''', 
      (self.nome, self.rg, self.cpf,
      self.email, self.senha, self.telefone,
      self.data_nascimento, self.sexo, self.foto_perfil,
      self.endereco, self.dados_bancarios, self.idhospede) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from hospede where idhospede = ?''', (self.idhospede,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from hospede where nome like ? ''', ("%"+self.nome+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select
        nome, rg, cpf, 
        email, senha, telefone, 
        data_nascimento, sexo, foto_perfil, 
        endereco, dados_bancarios, data_criacao
      from 
        hospede''')
    result = curso.fetchall()
    curso.close()
    return result

  def getHospedePorEmail(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from hospede where email = ?''', (self.email,))
    result = curso.fetchall()
    curso.close()
    return result

  def getHospedePorNome(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from hospede where nome = ?''', (self.nome,))
    result = curso.fetchone()
    curso.close()
    return result

  def getInfoHospede(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select
        nome, rg, cpf, 
        email, senha, telefone, 
        data_nascimento, sexo, foto_perfil, 
        endereco, dados_bancarios, data_criacao
      from 
        hospede 
      where idhospede = ?''', (self.idhospede,))
    result = curso.fetchone()
    curso.close()
    return result

  def autenticar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        nome, idhospede, foto_perfil
      from 
        hospede
      where 
        email = ? and senha = ?''', 
      (self.email, self.senha) )
    result = curso.fetchone()
    curso.close()
    return result