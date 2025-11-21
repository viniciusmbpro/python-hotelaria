# Alterações para Compatibilidade com macOS

Este documento descreve todas as alterações realizadas para tornar o sistema de hotelaria compatível com macOS.

## Problemas Corrigidos

### 1. Separadores de Caminho (✓)
**Problema:** O código usava `\\` (barras invertidas) específicas do Windows para separar caminhos.

**Solução:** Substituímos todas as ocorrências de `\\imagens\\` por `/imagens/` em 21 arquivos Python.

**Arquivos afetados:**
- Controllers: `HospedeController.py`, `FuncionarioController.py`
- Views/Admin: `AppInitAdmin.py`, `AppConfigAdmin.py`, `AppHospede.py`, `AppFuncionario.py`, etc.
- Views/Hospede: `AppInitHospede.py`, `AppConfig.py`, `AppCadastro.py`, `AppHome.py`, etc.

### 2. Arquivos de Ícone .ico (✓)
**Problema:** O método `iconbitmap()` não funciona com arquivos `.ico` no macOS (formato Windows).

**Solução:** Comentamos todas as chamadas de `iconbitmap()` em 14 arquivos, adicionando comentários explicativos.

**Nota:** Os ícones da janela não serão exibidos no macOS, mas a aplicação funciona normalmente.

### 3. Biblioteca tix (✓)
**Problema:** A biblioteca `tix` (Tk Interface Extension) não está disponível no Python 3.13 do macOS.

**Solução:** 
- Substituímos `tix.Tk()` por `Tk()` padrão em `AppInit.py`
- Comentamos todos os imports `from tkinter import tix` em 10 arquivos

**Arquivos afetados:**
- `AppInit.py`, `AppLogin.py`
- Views/Admin: `AppInitAdmin.py`, `AppConfigAdmin.py`, `AppLojasAdmin.py`
- Views/Hospede: todos os arquivos principais

### 4. Image.ANTIALIAS Depreciado (✓)
**Problema:** `Image.ANTIALIAS` foi depreciado no Pillow 10.0.0+

**Solução:** Substituímos todas as ocorrências por `Image.Resampling.LANCZOS` em 10 arquivos.

### 5. Versão do Pillow (✓)
**Problema:** Pillow 9.2.0 não é compatível com Python 3.13.

**Solução:** Atualizamos `requirements.txt` para usar `Pillow >= 10.0.0`

## Arquivos de Configuração Criados

### `run_macos.sh`
Script bash para facilitar a execução do projeto no macOS:
```bash
./run_macos.sh
```

Funcionalidades:
- Cria ambiente virtual se não existir
- Ativa o ambiente virtual
- Instala dependências automaticamente
- Executa a aplicação

### Scripts de Correção Utilizados
- `fix_paths_mac.py` - Corrigiu separadores de caminho
- `fix_iconbitmap_mac.py` - Comentou chamadas iconbitmap
- `fix_antialias_mac.py` - Substituiu Image.ANTIALIAS
- `fix_tix_imports.py` - Comentou imports de tix

## Como Executar no macOS

### Opção 1: Usando o script (Recomendado)
```bash
./run_macos.sh
```

### Opção 2: Manual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py
```

## Login Padrão
```
Email: felipe@gmail.com
Senha: felipe
```

## Dependências Atualizadas
- `tkcalendar == 1.5.0`
- `Pillow >= 10.0.0` (anteriormente 9.2.0)
- `babel` (dependência automática do tkcalendar)

## Compatibilidade Testada
- ✅ macOS com Python 3.13
- ✅ Interface Tkinter funcional
- ✅ Banco de dados SQLite funcionando
- ✅ Carregamento de imagens (PNG/GIF)

## Observações Importantes

1. **Ícones da janela:** Não serão exibidos no macOS devido à incompatibilidade do formato .ico
2. **Fullscreen:** O modo fullscreen funciona corretamente no macOS
3. **Performance:** Pode haver pequenas diferenças visuais devido às diferenças entre Windows e macOS Tkinter

## Estrutura de Arquivos Mantida
Toda a estrutura MVC original foi preservada:
- `App/Models/` - Modelos e banco de dados
- `App/Views/` - Interface gráfica
- `App/Controllers/` - Lógica de negócio
- `main.py` - Ponto de entrada

## Suporte
Este projeto agora suporta:
- ✅ Windows (original)
- ✅ Linux (branch for-linux)
- ✅ macOS (main branch com correções)
