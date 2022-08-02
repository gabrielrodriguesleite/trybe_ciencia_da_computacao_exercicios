FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./seu-arquivo.py"]

# docker build -t my-python-app .
# docker run -it --rm --name my-running-app my-python-app


#  ===== construindo e rodando diretamente (sem Dockerfile)=====

# docker run -it --rm --name nome-do-seu-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python seu-arquivo.py

# -v "$PWD":/usr/src/myapp - monta o diretório atual para dentro do contêiner

# -w /usr/src/myapp - muda o WORKDIR para executar o comando no diretório recém montado.