## Cargoroo API test

***** Adicionar data para o terminal dia/semana/mes *****

### Run the project with docker: 

- Build the container using docker:
```
docker-compose up --build
```
ps: *the docker compose was added to automate data insertion into the database after migration with a shell script.*


### Run the project virtual env:

1. Create a virtual environment folder and activate it:
```
python3 venv venv && source venv/bin/activate
```
2. Install the dependencies from `requirements.txt`:
```
pip install -r requirements.txt
```
3. Once installed all the dependencies, migrate the changes into the database:
```
python manage.py migrate
```
4. run the project:
```
python manage.py runserver
```
