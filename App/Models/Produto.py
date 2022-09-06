from .Model import *

class Produto(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        produto (descricao, preco, estoque) 
      values (?,?,?)''', 
      (self.descricao, self.preco, self.estoque) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update produto 
      set 
        descricao = ?, preco = ?, estoque = ?
      where idproduto = ? ''', 
        (self.descricao, self.preco, self.estoque, self.idproduto) )
    self.conexao.commit()
    curso.close()

  def alterarEstoque(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update produto 
      set 
        estoque = ?
      where idproduto = ? ''', 
        (self.estoque, self.idproduto) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from produto where idproduto = ?''', (self.idproduto,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
        select * from produto 
        where descricao like ? ''', 
        ("%"+self.descricao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from produto''')
    result = curso.fetchall()
    curso.close()
    return result

  def getProdutoPorDescricao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from produto where descricao = ?''', (self.descricao,))
    result = curso.fetchall()
    curso.close()
    return result

  def getInfoProduto(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from produto where idproduto = ?''', (self.idproduto,))
    result = curso.fetchone()
    curso.close()
    return result