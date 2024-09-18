# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Defina as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# Crie um diretório para a aplicação
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta que a API usará
EXPOSE 8000

# Execute as migrações e inicie o servidor
#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
CMD ["gunicorn", "ireAPP.wsgi:application", "--bind", "0.0.0.0:8000"]
