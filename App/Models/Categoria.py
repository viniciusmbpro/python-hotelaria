from .Model import *

class Categoria(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        categoria (descricao, valor, produtos) 
      values (?,?,?)''', 
      (self.descricao, self.valor, self.produtos) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update categoria 
      set 
        descricao = ?, valor = ?, produtos = ?
      where idcategoria = ? ''', 
        (self.descricao, self.valor, self.produtos, self.idcategoria) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from categoria where idcategoria = ?''', (self.idcategoria,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
        select * from categoria 
        where descricao like ? ''', 
        ("%"+self.descricao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from categoria''')
    result = curso.fetchall()
    curso.close()
    return result

  def getCategoriaPorDescricao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from categoria where descricao = ?''', (self.descricao,))
    result = curso.fetchone()
    curso.close()
    return result

  def getInfoCategoria(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from categoria where idcategoria = ?''', (self.idcategoria,))
    result = curso.fetchone()
    curso.close()
    return result