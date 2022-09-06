from .Model import *

class Acomodacao(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        acomodacao (descricao, andar, capacidade, 
                    observacoes, status, fk_idcategoria) 
      values (?,?,?,?,?,?)''', 
      (self.descricao, self.andar, self.capacidade,
      self.observacoes, self.status, self.fk_idcategoria) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update acomodacao 
      set 
        descricao = ?, andar = ?, capacidade = ?, 
        observacoes = ?, status = ?, fk_idcategoria = ?
      where idacomodacao = ? ''', 
        (self.descricao, self.andar, self.capacidade,
         self.observacoes, self.status, self.fk_idcategoria, 
         self.idacomodacao) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from acomodacao where idacomodacao = ?''', (self.idacomodacao,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        a.idacomodacao, a.descricao, a.andar, 
        a.capacidade, a.observacoes, a.status, 
        c.descricao
      from 
        acomodacao a, categoria c 
      where 
        a.fk_idcategoria = c.idcategoria and
        a.descricao like ? ''', 
        ("%"+self.descricao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from acomodacao''')
    result = curso.fetchall()
    curso.close()
    return result

  def getAcomodacaoPorDescricao(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        a.idacomodacao, a.descricao, a.andar, a.capacidade, 
        a.observacoes, a.status, c.descricao, c.valor
      from 
        acomodacao a, categoria c 
      where 
        a.fk_idcategoria = c.idcategoria and
        a.descricao = ?''', 
      (self.descricao,))
    result = curso.fetchone()
    curso.close()
    return result

  def getInfoAcomodacao(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        a.descricao, a.andar, a.capacidade, 
        a.observacoes, a.status, c.descricao, 
        c.valor
      from 
        acomodacao a, categoria c 
      where 
        a.fk_idcategoria = c.idcategoria and
        a.idacomodacao = ?''', 
      (self.idacomodacao,))
    result = curso.fetchone()
    curso.close()
    return result

  def ocupar(self):
    curso = self.conexao.cursor()
    curso.execute('''update acomodacao set status = 'Ocupado' where idacomodacao = ?''', (self.idacomodacao,))
    self.conexao.commit()
    curso.close()

  def desocupar(self):
    curso = self.conexao.cursor()
    curso.execute('''update acomodacao set status = 'Desocupado' where idacomodacao = ?''', (self.idacomodacao,))
    self.conexao.commit()
    curso.close()