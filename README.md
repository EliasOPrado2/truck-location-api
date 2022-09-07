## TrackPAD API

### Rodar o projeto com docker: 

1. Crie um arquivo `.env` no root e adicione o seguinte dado para autenticação do geopy:
```
USER_AGENT = "qualqueremail@realemail.com"
```

2. Ligue o container:
```
docker-compose up --build
```


### Rodar o projeto com virtual env:

1. Crie um arquivo `.env` no root e adicione o seguinte dado para autenticação do geopy:
```
USER_AGENT = "qualqueremail@realemail.com"
```
2. Crie um virtual environment e ative o mesmo:
```
python3 venv venv && source venv/bin/activate
```
3. Instale as dependencias de `requirements.txt`:
```
pip install -r requirements.txt
```
4. Uma vez instalada as dependencias acione o banco de dados baseado nas migrações.
```
python manage.py migrate
```
5. Rode o projeto:
```
python manage.py runserver
```

### Processo de adição de dados

1. criar truck-driver `/api/truck-drivers/`:
```JSON
{
    "name": "John Doe",
    "age": 32,
    "sex": 0,
    "has_truck": true,
    "cnh_type": "1",
    "is_loaded": true,
    "truck_type": 1
}
```
2. create two addresses `/api/addresses/`:
```JSON
{
    "address": "Rua valdemar de paula ferreira",
    "neighborhood": "Jardim presidente dutra",
    "city": "guarulhos",
    "state": "Sao Paulo",
    "postcode": "",
    "country": "Brasil"
}
```
E..
```JSON
{
    "address": "Avenida paulista  66",
    "neighborhood": "bela vista",
    "city": "Sao Paulo",
    "state": "SP",
    "postcode": "01310-000",
    "country": "Brasil"
}
```
ps: *latitude e longitude de cada sera calculada com ajuda do `geopy`*

3. Criar uma rota `/api/truck-drivers/{truckdrives_pk}/routes/`:
```JSON
{
    "origin": 1,
    "destination": 2
}
```
- distancia sera calculada com ajuda do `geopy` e `is_active`sera setado para True.
ps: *nao e permitido adicionar o mesmo `address` para origin e destination.*

4. check terminal:
Aqui se pode checar os motoristas que passaram no terminal pelo dia, semana e mes usando query parameters como:

- `/api/terminal/?trucks_per_day=YYYY-MM-DD`
- `/api/terminal/?trucks_per_week=YYYY-MM-DD`
- `/api/terminal/?trucks_per_month=MM`

O calculo e feito sobre rotas criadas.


### O que foi feito:
- Criado modelo e endpoint para cadastrar os motoristas com seus consecutivos dados.
- Criado um endpoit `Route` com `origin`, `destination` detalhes do endereço e a distancia.
- Criado dois filtros para saber se o motorista esta com o caminhão carregado `is_loaded` ou se o mesmo tem o proprio caminhão `has_truck`.
- Criado um endpoint chamado `terminal/` no qual detalha quantos motoristas criaram rotas no dia, semana e no mes: `trucks_per_day`, `trucks_per_week`, `trucks_per_month`. 
Exemplo: `api/terminal/?trucks_per_day=2022-09-07` no qual ira retornar os dados de quantos motoristas passaram pelo terminal.
- Motoristas podem fazer update dos seus dados.
- Criado testes unitarios para partes relevantes do sistema.

### Melhorias que nao deu para implementar a tempo.
- Tratamento de exceções no view `TerminalViewSet`.
- Expiração de rota ao desativa-la `.../route/?is_active=false` no endipoint `route` dando um parecer de retorno ao motorista.
- Adição de logica na pasta services.
- Adicionar testes mais profundos.
- Não foi testado o endpoint `terminal/` por conta de mocagem de data e tempo. Caso queira testar os mesmo adicione os seguintes testes no final do arquivo `core\tests\test_api.py` e adicione no lugar de `'YYYY-MM-DD` a data atual de criação dos objetos como "na hora/dia que os testes forem feitos".

```python 
def test_terminal_trucks_per_day(self):
    response = self.client.get("/api/terminal/", {"trucks_per_day": 'YYYY-MM-DD'})
    trucks_per_day = response.data['trucks_per_day']
    self.assertGreater(trucks_per_day, 0)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_terminal_trucks_per_week(self):
    print(self.route.created_at)
    response = self.client.get("/api/terminal/", {"trucks_per_week": 'YYYY-MM-DD'})
    trucks_per_week = response.data['trucks_per_week']
    print(trucks_per_week)
    self.assertGreater(trucks_per_week, 0)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_terminal_trucks_per_month(self):
    print(self.route.created_at)
    response = self.client.get("/api/terminal/", {"trucks_per_month": 'MM'})
    trucks_per_month = response.data['trucks_per_month']
    print(trucks_per_month)
    self.assertGreater(trucks_per_month, 0)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```