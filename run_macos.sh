#!/bin/bash
# Script para iniciar o sistema de hotelaria no macOS

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}Sistema de Hotelaria - macOS${NC}"
echo -e "${BLUE}================================${NC}\n"

# Ativar ambiente virtual
if [ ! -d "venv" ]; then
    echo -e "${BLUE}Criando ambiente virtual...${NC}"
    python3 -m venv venv
fi

echo -e "${BLUE}Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Instalar dependências se necessário
if ! python -c "import tkcalendar" 2>/dev/null; then
    echo -e "${BLUE}Instalando dependências...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Executar aplicação
echo -e "${GREEN}Iniciando aplicação...${NC}\n"
python main.py

# Desativar ambiente virtual ao sair
deactivate
