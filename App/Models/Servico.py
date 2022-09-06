from .Model import *

class Servico(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        servico (descricao, preco, status) 
      values (?,?,?)''', 
      (self.descricao, self.preco, self.status) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update servico 
      set 
        descricao = ?, preco = ?, status = ?
      where idservico = ? ''', 
        (self.descricao, self.preco, self.status, self.idservico) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from servico where idservico = ?''', (self.idservico,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
        select * from servico 
        where descricao like ? ''', 
        ("%"+self.descricao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from servico''')
    result = curso.fetchall()
    curso.close()
    return result

  def getServicoPorDescricao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from servico where descricao = ?''', (self.descricao,))
    result = curso.fetchall()
    curso.close()
    return result

  def getInfoServico(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from servico where idservico = ?''', (self.idservico,))
    result = curso.fetchone()
    curso.close()
    return result