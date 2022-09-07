## TrackPAD API

### Rodar o projeto com docker: 

```
docker-compose up --build
```


### Rodar o projeto com virtual env:

1. Crie um virtual environment e ative o mesmo:
```
python3 venv venv && source venv/bin/activate
```
2. Instale as dependencias de `requirements.txt`:
```
pip install -r requirements.txt
```
3. Uma vez instalada as dependencias acione o banco de dados baseado nas migrações.
```
python manage.py migrate
```
4. Rode o projeto:
```
python manage.py runserver
```

### O que foi feito:
- Criado modelo e endpoint para cadastrar os motoristas com seus consecutivos dados.
- Criado um endpoit `Route` com `origin`, `destination` detalhes do endereço e a distancia.
- Criado dois filtros para saber se o motorista esta com o caminhão carregado `is_loaded` ou se o mesmo tem o proprio caminhão `has_truck`.
- Criado um endpoint chamado `terminal/` no qual detalha quantos motoristas criaram rotas no dia, semana e no mes: `trucks_per_day`, `trucks_per_week`, `trucks_per_month`. 
Exemplo: `api/terminal/?trucks_per_day=2022-09-07` no qual ira retornar os dados de quantos motoristas passaram pelo terminal.
- Motoristas podem fazer update dos seus dados.
- Criado testes unitarios para partes relevantes do sistema.

### Processo de adição de dados

1 truck-driver
2 create two addresses
3 create route
4 check terminal

### Melhorias para serem implementadas
- Tratamento de exceções no view `TerminalViewSet`.
- Expiração de rota ao desativa-la `.../route/?is_active=false` no endipoint `route` dando um parecer de retorno ao motorista.
- Adição de logica na pasta services.