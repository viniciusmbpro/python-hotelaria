# Prototipo de um sistema de Hotelaria

* 100% Python

* Arquitetura MVC

* Orientação a Objetos

* Interface Gráfica usando a biblioteca Tkinter do python

* Usando princípios do Singleton e SOLID

* Perfis de funcionários e hóspedes 

## Printscreens
  <img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/login.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/cadastro.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/admin_hospede.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/admin_checkin.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/hospede_reservar.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/hospede_minhas_reservas.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/hospede_config.png"/><img width="50%" style="display: inline-block;" src="https://github.com/viniciusmbezerra/python_hotelaria/blob/main/printscreens/hospede_loja.png"/>

## 1. Inicialização

Todo o projeto está dividido em classes:

    1. Nas Views elas são responsáveis por criar as telas de exibição para o usuário, essas views ativam determinados controllers para realizar operações;

    2. Os Controllers fazem a mediação de todo o sistema, eles são os maestros, por eles passam todas as requisições. Ele recebem um pedido para realizar uma operação e retornam uma resposta consultando ou não os Models;

    3. Os Models por sua vez agem com contato direto no banco de dados, afunilando sua atenção para este único objetivo;

Desse modo qualquer operação faz este percusso:

``View`` -> ``Controller`` -> ``Model``

``View`` <- ``Controller`` <- ``Model``

A primeira chamada é feita a partir do arquivo main.py

## 2. Controllers

```python
#importando o controlador central AppController
from App.Controllers import AppController

#iniciando aplicação
AppController('AppLogin')
```
A classe AppController faz as ``operações centrais`` do sistema seus métodos são responsáveis por ``renderizar telas`` e fazer o processo de ``login e logout de usuários``

```python
class AppController():
    def __init__(self, telaInicial):
        self.Init = globals()["AppInit"](self)
        self.Init.session = {'idusuario':0, 'nome':['','',''], 'foto_perfil':''}
        self.tela = globals()[telaInicial](self.Init)
        self.Init.loop()
        
    def renderTela(self, tela_alvo):
        self.tela.framePrincipal.destroy()
        self.tela = globals()[tela_alvo](self.Init
```

### Todo o projeto roda em cima de uma instância da classe ``AppInit``;
* Ela armazena uma instância do controlador geral ``AppController``;
* Armazena o atributo ``session`` para guardar os dados da sessão do usuário;
* E armazena o atributo ``tela``, que é a tela atual do sistema, ou seja, a ``instância de uma determinada View``;

Ao criar qualquer tela o ``AppController`` passa ``por parâmetro`` a instância da classe ``AppInit``, para que qualquer tela tenha acesso aos atributos dessa classe raiz;

Nos outros Controllers ``todos os métodos estáticos`` que vão ser chamados dentro das Views para realizar a operação desejada;

## 3. Views

Como dito, cada View é uma classe, depois de instanciar a view base do sistema ``AppInit``:

```python
class AppInit():
    def __init__(self, control):
        self.control = control
        self.root = root
        self.config_janela()
        self.config_estilos()
```

* A janela de exibição principal do Tkinter vai estar aberta e todas as outras views vão ser colocadas dentro dessa janela;

* Todas as outras views são frames de exibição do Tkinter;

* Assim, toda troca de tela é feita a partir da ``destruição do frame atual`` e da ``criação do frame alvo``, na chamada do método ``renderTela`` do ``AppController``;

```python
class AppController():
    ...
    def renderTela(self, tela_alvo):
        self.tela.framePrincipal.destroy()
        self.tela = globals()[tela_alvo](self.Init
    ...
```

O perfil de cada usuário tem ``muitas telas``, por isso eles tem um ``arquivo de iniciação`` (que também roda em cima da AppInit), ``que instancia as subtelas``;

    .Views
    --.Admin
    ----AppInitAdmin.py
    --.Hospede
    ----AppInitHopede.py
    --AppInit.py
    --AppLogin.py

Portanto os arquivos prefixados com ``AppInit`` são ``instâncias que contém instâncias de outras telas``.

```python
class AppInitAdmin:
    def __init__(self, Init):
        self.Init = Init
        ...
        #chamando as views
        AppHospede(self.abaHospede, Init)
        AppFuncionario(self.abaFuncionario, Init)
        AppAcomodacao(self.abaAcomodacao, Init)
        AppCategoria(self.abaCategoria, Init)
        AppServico(self.abaServico, Init)
        AppProduto(self.abaProduto, Init)
        AppReserva(self.abaReserva, Init)
        AppCheckin(self.abaCheckin, Init)
        AppCheckin(self.abaCheckin, Init)
        AppCheckout(self.abaCheckout, Init)
        ...
```

Esta view filha recebe como parâmetro o frame a qual ela pertence e a instância de ``AppInit``;

Desse modo elas podem realizar qualquer operação dentro do sistema;

## 4. Models

Todos os models herdam da classe ``Model``:

```python
class Model:
  def __init__(self):
    self.conexao = Banco().conexao

  def validarDados(self, campos, acao):
    ...
    return validado
```

Esta classe abstrai operações que :

1. Criam a ``conexão com o banco``;
2. ``Validam os dados`` nos processos de cadastro e alteração

Desse modo todo ``Model`` já é iniciado com essas habilidades;

Os models são chamados pelos controllers e fazem a operação que lhe for pedida;

[⬆ Go back to the top!](#Prototipo de um sistema de Hotelaria)<br>
