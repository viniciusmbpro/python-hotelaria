from .Model import *

class Reserva(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into 
        reserva (qtd_hospedes, hospedes, antecipacao, entrada_prevista,
                 saida_prevista, data_criacao, status, valor,
                 servicos, produtos, fk_idhospede, fk_idacomodacao)
      values (?,?,?,?,?,?,?,?,?,?,?,?)''', 
        (self.qtd_hospedes, self.hospedes, self.antecipacao, 
        self.entrada_prevista, self.saida_prevista, self.data_criacao, 
        self.status, self.valor, self.servicos, self.produtos, self.fk_idhospede, 
        self.fk_idacomodacao) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update 
        reserva 
      set 
        qtd_hospedes = ?, hospedes = ?, antecipacao = ?, entrada_prevista = ?,
        saida_prevista = ?, data_criacao = ?, status = ?, valor = ?,
        servicos = ?, produtos = ?, fk_idhospede = ?, fk_idacomodacao = ?
      where idreserva = ? ''', 
        (self.qtd_hospedes, self.hospedes, self.antecipacao, 
        self.entrada_prevista, self.saida_prevista, self.data_criacao, 
        self.status, self.valor, self.servicos, self.produtos, self.fk_idhospede, 
        self.fk_idacomodacao) )
    self.conexao.commit()
    curso.close()

  def alterarConsumo(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update 
        reserva 
      set 
        servicos = ?, produtos = ?
      where idreserva = ? ''', 
        (self.servicos, self.produtos, self.idreserva) )
    self.conexao.commit()
    curso.close()

  def alterarStatus(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update 
        reserva 
      set 
        status = ?
      where 
        idreserva = ? ''', 
        (self.status, self.idreserva) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from reserva where idreserva = ?''', (self.idreserva,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        r.idreserva, r.qtd_hospedes, r.antecipacao, r.entrada_prevista, 
        r.saida_prevista, r.data_criacao, h.nome, a.descricao, r.valor, r.status
      from 
        reserva r, hospede h, acomodacao a, categoria c
      where 
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        a.fk_idcategoria = c.idcategoria and
        r.data_criacao like ? ''', 
        ("%"+self.data_criacao+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        idreserva, qtd_hospedes, antecipacao, status,
        entrada_prevista, saida_prevista, data_criacao
      from 
        reserva''')
    result = curso.fetchall()
    curso.close()
    return result

  def getReservaPorData_criacao(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from reserva where data_criacao = ?''', (self.data_criacao,))
    result = curso.fetchone()
    curso.close()
    return result

  def getInfoReserva(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        r.qtd_hospedes, r.antecipacao, r.entrada_prevista, 
        r.saida_prevista, r.data_criacao, h.nome, a.descricao, 
        r.valor, r.servicos, r.produtos, r.fk_idacomodacao
      from 
        reserva r, hospede h, acomodacao a
      where 
        r.fk_idhospede = h.idhospede and
        r.fk_idacomodacao = a.idacomodacao and
        r.idreserva = ?''', 
    (self.idreserva,))
    result = curso.fetchone()
    curso.close()
    return result

  def getAllToHospede(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        r.idreserva, r.qtd_hospedes, r.antecipacao, r.status,
        r.entrada_prevista, r.saida_prevista, r.data_criacao, 
        a.descricao, a.andar, a.observacoes, c.descricao, r.valor
      from 
        reserva r, hospede h, acomodacao a, categoria c
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

  def getAllToAcomodacao(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        entrada_prevista, saida_prevista, status
      from 
        reserva
      where 
        fk_idacomodacao = ?''', 
    (self.fk_idacomodacao,))
    result = curso.fetchall()
    curso.close()
    return result

  def getHospedePorDataReserva(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        h.nome, r.data_criacao, r.idreserva
      from 
        reserva r, hospede h
      where 
        r.fk_idhospede = h.idhospede and
        r.data_criacao = ?''', 
    (self.data_criacao,))
    result = curso.fetchone()
    curso.close()
    return result
