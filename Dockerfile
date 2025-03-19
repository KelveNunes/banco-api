# Imagem base oficial do Python
FROM python:3.12

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependências (requirements.txt) para dentro do container
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt
RUN echo "export PATH=$PATH:/usr/local/bin" >> ~/.bashrc

# Copiar o restante dos arquivos para dentro do container
COPY . /app/

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
