### Setup .env

Customise `.env.sample` and rename it to `.env`

### Setup postgres

```bash
docker build -t my_postgres_image .
docker run --name my_postgres_container -p 5432:5432 -d my_postgres_image
```

In `alembic.ini` use the sqlalchemy.url:

```python
sqlalchemy.url = postgresql://myuser:mypassword@localhost:5432/mydatabase
```

### Setup alembic

```bash
alembic init alembic
```

Set alembic sqlalchemy url:

- In `alembic.ini` under `sqlalchemy.url`
- with .env file with env.py
