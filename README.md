# Agenda


#### Gerar ambiente virtual:

Na pasta raiz do projeto executar

```
python3 -m venv venv
```

Ativar ambiente:

```
source venv/bin/activate
```

Este projeto utiliza: 

- [Django](https://www.djangoproject.com)
- [Venv](https://docs.python.org/3/library/venv.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)



## Lista de Comandos

Executar projeto localmente

```
make run
```
Criar app:

```
make create_app APP=[nome do app]
EX: make create_app APP=contact
```

Gerar migrations:

```
make makemigrations
```

Executar migrations:

```
make migrate
```

Gerar super usuário

```
make createsuperuser
```

ALterar password de  super usuário:

```
make changepassword USERNAME=[nome do super usuário]
EX: make changepassword USERNAME=teste
```

Coletar arquivos estáticos

```
make collectstatic
```