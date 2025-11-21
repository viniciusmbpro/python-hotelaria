# Início Rápido - macOS

## ✅ Projeto Adaptado para macOS!

Todas as correções necessárias já foram aplicadas.

## Como Executar

```bash
./run_macos.sh
```

Ou manualmente:

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar aplicação
python main.py
```

## Login Padrão

```
Email: felipe@gmail.com
Senha: felipe
```

## O que foi corrigido?

✅ Separadores de caminho (Windows → Unix)  
✅ Biblioteca tix removida (incompatível com Python 3.13)  
✅ Arquivos .ico comentados (não suportados nativamente no macOS)  
✅ Image.ANTIALIAS atualizado para Image.Resampling.LANCZOS  
✅ Pillow atualizado para versão 10.0.0+  

## Detalhes Completos

Veja `MACOS_CHANGES.md` para informações detalhadas sobre todas as alterações.
