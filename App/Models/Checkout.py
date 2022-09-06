from .Model import *

class Checkout(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into checkout 
        (valor_consumo, valor_pago, nota_fiscal, 
        data_criacao, fk_idfuncionario, fk_idreserva)
      values (?,?,?,?,?,?)''', 
      (self.valor_consumo, self.valor_pago, self.nota_fiscal,
      self.data_criacao, self.fk_idfuncionario, self.fk_idreserva) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update checkout 
      set 
        valor_consumo = ?, valor_pago = ?, nota_fiscal = ?, 
        fk_idfuncionario = ?, fk_idreserva = ?
      where idcheckout = ? ''', 
      (self.valor_consumo, self.valor_pago, self.nota_fiscal,
      self.fk_idfuncionario, self.fk_idreserva, self.idcheckout) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from checkout where idcheckout = ?''', (self.idcheckout,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        c.idcheckout, c.data_criacao, c.fk_idreserva, 
        h.idhospede, c.fk_idfuncionario, a.idacomodacao,
        c.valor_consumo, c.valor_pago, c.nota_fiscal 
      from 
        checkout c, hospede h, acomodacao a, reserva r
      where 
        c.fk_idreserva = r.idreserva and
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        h.nome like ? ''', 
        ("%"+self.data_criacao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def getCheckoutPorData_criacao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from checkout where data_criacao = ?''', (self.data_criacao,))
    result = curso.fetchall()
    curso.close()
    return result

  def getInfoCheckout(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        c.idcheckout, c.data_criacao, c.fk_idreserva, 
        h.idhospede, c.fk_idfuncionario, a.idacomodacao,
        c.valor_consumo, c.valor_pago, c.nota_fiscal 
      from 
        checkout c, hospede h, acomodacao a, reserva r
      where 
        c.fk_idreserva = r.idreserva and
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        c.idcheckout = ? ''', 
    (self.idcheckout,))
    result = curso.fetchone()
    curso.close()
    return result

  def getAllToHospede(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        r.idcheckout, r.qtd_hospedes, r.antecipacao, 
        r.entrada_prevista, r.saida_prevista, r.data_criacao, 
        a.descricao, a.andar, a.observacoes, c.descricao, c.valor
      from 
        checkout r, hospede h, acomodacao a, categoria c
      where 
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        a.fk_idcategoria = c.idcategoria and
        r.fk_idhospede = ? and
        r.data_criacao like ?''', 
    (self.fk_idhospede, "%"+self.data_criacao+"%"))
    result = curso.fetchall()
    curso.close()
    return result
