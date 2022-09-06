from .Model import *

class Funcionario(Model):
  def cadastrar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      insert into funcionario 
        (nome, rg, cpf, 
         email, senha, telefone, 
         data_nascimento, sexo, foto_perfil, 
         endereco, dados_bancarios, data_criacao,
         matricula, cargo, nivel_acesso, data_admissao) 
      values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
      (self.nome, self.rg, self.cpf,
       self.email, self.senha, self.telefone,
       self.data_nascimento, self.sexo, self.foto_perfil,
       self.endereco, self.dados_bancarios, self.data_criacao,
       self.matricula, self.cargo, self.nivel_acesso, self.data_admissao) )
    self.conexao.commit()
    curso.close()

  def alterar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      update funcionario 
      set 
        nome = ?, rg = ?, cpf = ?, 
        email = ?, senha = ?, telefone = ?, 
        data_nascimento = ?, sexo = ?, foto_perfil = ?, 
        endereco = ?, dados_bancarios = ?, matricula = ?, cargo = ?, 
        nivel_acesso = ?, data_admissao = ?
      where idfuncionario = ? ''', 
        (self.nome, self.rg, self.cpf,
         self.email, self.senha, self.telefone,
         self.data_nascimento, self.sexo, self.foto_perfil,
         self.endereco, self.dados_bancarios, self.matricula, 
         self.cargo, self.nivel_acesso, self.data_admissao,
         self.idfuncionario) )
    self.conexao.commit()
    curso.close()

  def deletar(self):
    curso = self.conexao.cursor()
    curso.execute('''delete from funcionario where idfuncionario = ?''', (self.idfuncionario,))
    self.conexao.commit()
    curso.close()

  def buscar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        idfuncionario, nome, rg, 
        cpf, email, senha, 
        telefone, data_nascimento, sexo, 
        foto_perfil, endereco, dados_bancarios, 
        data_criacao, matricula, cargo, 
        nivel_acesso, data_admissao
      from 
        funcionario
      where 
        nome like ? ''', 
      ("%"+self.nome+"%",))
    result = curso.fetchall()
    curso.close()
    return result

  def getFuncionarioPorEmail(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from funcionario where email = ?''', (self.email,))
    result = curso.fetchall()
    curso.close()
    return result

  def getFuncionarioPorNome(self):
    curso = self.conexao.cursor()
    curso.execute('''select * from funcionario where nome = ?''', (self.nome,))
    result = curso.fetchone()
    curso.close()
    return result

  def getInfoFuncionario(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        nome, rg, 
        cpf, email, senha, 
        telefone, data_nascimento, sexo, 
        foto_perfil, endereco, dados_bancarios, 
        data_criacao, matricula, cargo, 
        nivel_acesso, data_admissao
      from 
        funcionario
      where 
        idfuncionario = ? ''', 
      (self.idfuncionario,))
    result = curso.fetchone()
    curso.close()
    return result

  def listar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        nome, rg, 
        cpf, email, senha, 
        telefone, data_nascimento, sexo, 
        foto_perfil, endereco, dados_bancarios, 
        data_criacao, matricula, cargo, 
        nivel_acesso, data_admissao
      from 
        funcionario''')
    result = curso.fetchall()
    curso.close()
    return result

  def autenticar(self):
    curso = self.conexao.cursor()
    curso.execute('''
      select 
        nome, idfuncionario, foto_perfil
      from 
        funcionario 
      where 
        nivel_acesso='Admin' and
        email = ? and 
        senha = ? ''', 
      (self.email, self.senha) )
    result = curso.fetchone()
    curso.close()
    return result