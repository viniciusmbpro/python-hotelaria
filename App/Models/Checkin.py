from .Model import *

class Checkin(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        checkin (data_criacao, fk_idfuncionario, fk_idreserva)
      values (?,?,?)''', 
      (self.data_criacao, self.fk_idfuncionario, self.fk_idreserva) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update checkin 
      set 
        fk_idfuncionario = ?, fk_idreserva = ?
      where idcheckin = ? ''', 
        (self.fk_idfuncionario, self.fk_idreserva, self.idcheckin) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from checkin where idcheckin = ?''', (self.idcheckin,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        c.idcheckin, c.data_criacao, c.fk_idreserva, 
        h.idhospede, c.fk_idfuncionario, a.idacomodacao
      from 
        checkin c, hospede h, acomodacao a, reserva r
      where 
        c.fk_idreserva = r.idreserva and
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        h.nome like ? ''', 
        ("%"+self.data_criacao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def getCheckinPorData_criacao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from checkin where data_criacao = ?''', (self.data_criacao,))
    result = curso.fetchall()
    curso.close()
    return result

  def getInfoCheckin(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        c.idcheckin, c.data_criacao, c.fk_idreserva, 
        h.idhospede, c.fk_idfuncionario, a.idacomodacao
      from 
        checkin c, hospede h, acomodacao a, reserva r
      where 
        c.fk_idreserva = r.idreserva and
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        c.idcheckin = ? ''', 
    (self.idcheckin,))
    result = curso.fetchone()
    curso.close()
    return result

  def getAllToHospede(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        r.idcheckin, r.qtd_hospedes, r.antecipacao, 
        r.entrada_prevista, r.saida_prevista, r.data_criacao, 
        a.descricao, a.andar, a.observacoes, c.descricao, c.valor
      from 
        checkin r, hospede h, acomodacao a, categoria c
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
