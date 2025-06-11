# Etapa base: usa imagem Python leve
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia dependências primeiro (aproveita cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta padrão do FastAPI/Uvicorn
EXPOSE 8000

# Comando de inicialização do servidor FastAPI
CMD ["uvicorn", "bot_nuxo.bot_whatsapp.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
