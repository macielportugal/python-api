# Python API

## Resumo

API que permitir o cadastro de usuário e envio de imagem com analise da foto.

## Requisitos
* <a href="https://www.docker.com/">Docker</a>
* <a href="https://docs.docker.com/compose/">Docker Compose</a>

## Instalação
```bash
git clone git@github.com:macielportugal/python-api.git
cd python-api
docker-compose build
docker-compose up -d
```

## Uso
O sistema pode se gerenciado por chamadas HTTP <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

### API

#### Usuários

Listagem de usuários:

```bash
curl -X GET http://127.0.0.1:5000/users
```

Registro de usuário:

```bash
curl -X POST  http://127.0.0.1:5000/registration  -H "Content-Type:application/json"  -d '{"username": "fulano", "password": 123456 }'
```

Login de usuário:

```bash
curl -X POST  http://127.0.0.1:5000/login  -H "Content-Type:application/json"  -d '{"username": "fulano", "password": 123456 }'
```

#### Enviar imagem

Enviar imagem:

```bash
curl -X POST  http://127.0.0.1:5000/send/image  -H "Authorization: Bearer cff0071b78232725662b7726c5de2809c90749d5" -F "image=@/home/user/teste.jpg"
```

## Ambiente de desenvolvimento

Criação de ambiente de desenvolvimento

```bash
docker-compose build
docker-compose up -d
```

## Ambiente de Produção

#### Docker

```bash
docker-compose build
docker-compose -f production.yml up -d
```

#### WSGI Server

```bash
python3 -m virtualenv virt
source virt/bin/activate
export APP_CONFIG_FILE=config/production.py
gunicorn -w 4 -b 0.0.0.0:5000 routes:app
```

#### Amazon

```bash
cd app/
cp config/development.py config/production.py
docker-compose exec web python3 -m pip freeze > requirements.txt
eb init -p python-3.6 python-api --region us-east-2
eb init
eb create python-api-env
```

## Testes

Os testes cobrem todas as etapas da API.

Arquivo com os testes app/tests.py

```bash
docker-compose exec web pytest tests.py
```
