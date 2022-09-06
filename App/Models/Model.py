from .Banco import *

class Model:
  def __init__(self):
    self.conexao = Banco().conexao

  def validarDados(self, campos, acao):
    validado = True
    if acao == "Cadastrar":
      for campo in campos:
        curso = self.conexao.cursor()
        curso.execute(f'''select * from {str.lower(self.__class__.__name__)} where {campo} = "{self.__dict__[campo]}" ''')
        result = curso.fetchone()
        curso.close()
        if result:
          validado = False
    elif acao == "Alterar":
      for campo in campos:
        curso = self.conexao.cursor()
        curso.execute(f'''select * from {str.lower(self.__class__.__name__)} where {campo} = "{self.__dict__[campo]}" ''')
        result = curso.fetchone()
        curso.close()
        if len(str(result))<2:
          validado = False
    array = list(self.__dict__.values())
    del(array[0])
    del(array[-1])
    for dado in array:
      if len(str(dado)) < 3:
        validado = False
    return validado