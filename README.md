***
Esse projeto baseia em um blog de notícias onde ao se registrar o usuário vai ter a capacidade de relatar notícias utilizando um CRUD que é baseado em na api NY TIMES API. Esse projetos tem 4 funções principais: autenticação de usários utilizando a biblioteca AllAuth Django, CRUD de notícias para que o usuário registrado possa fazer a  sua própria notícia, um buscador de notícia do New York Times para trazer as notícias do momento utilizando NY TIME API e finalmente para a tradução das notícias do New York Times utilizei a biblioteca do google translate.

O projeto não está totalmente pronto por causa de quedas de internet na hora da produção do projeto mas, está próximo do resultado final, para finalmente iniciar o projeto siga os seguintes passos:

```
# Clonando o Projeto

# Abra seu git bash em uma pasta vazia e digite os seguintes comandos

git init # para iniciar o repositório local

git clone https://github.com/devluizmatheus/wsBackend-Fabrica25.1.git # para copiar no repositório local

# logo em seguida faça esse comando para abrir no seu vscode

cd wsBackend-Fabrica25.1

code .
```

para iniciar o projeto faça os seguintes passos

```
# Para ambiente virtual

python -m venv env #Obs: a versão do projeto é a 3.12.8

env/scripts/activate

# Para instalar as depêndencias e iniciar o projeto de fato

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate
```

