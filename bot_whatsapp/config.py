# Arquivo de configuração para o projeto
# Será implementado conforme necessário

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da aplicação
APP_NAME = "Nuxo Bot"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
PORT = int(os.getenv("PORT", "8000"))

# Configurações do WhatsApp (serão adicionadas posteriormente)
# WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY", "")
# WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "")
