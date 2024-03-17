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



## Lista de Comandos

Executar projeto localmente

```
make run
```
Criar app:
- make create_app APP=[nome do app]
- Exemplo:

```
make create_app APP=contact
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

- make changepassword USERNAME=[nome do super usuário]
- Exemplo:

```
make changepassword USERNAME=teste
```

Coletar arquivos estáticos

```
make collectstatic
```